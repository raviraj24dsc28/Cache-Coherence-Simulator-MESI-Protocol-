import random

states = ["M", "E", "S", "I"]

class Cache:
    def __init__(self, cpu_id):
        self.cpu_id = cpu_id
        self.lines = {}  # addr -> state

    def access(self, addr, op, system):
        state = self.lines.get(addr, "I")

        if op == "R":  # Read
            if state in ["M", "E", "S"]:
                result = "HIT"
            else:
                system.broadcast("BusRd", self.cpu_id, addr)
                self.lines[addr] = "S"
                result = "MISS"
            print(f"CPU{self.cpu_id} READ {hex(addr)} -> {result}")

        elif op == "W":  # Write
            if state == "M":
                result = "HIT"
            else:
                system.broadcast("BusRdX", self.cpu_id, addr)
                self.lines[addr] = "M"
                result = "MISS"
            print(f"CPU{self.cpu_id} WRITE {hex(addr)} -> {result}")

        return result

class System:
    def __init__(self, num_cpus):
        self.caches = [Cache(i) for i in range(num_cpus)]

    def broadcast(self, msg, sender, addr):
        for c in self.caches:
            if c.cpu_id != sender and addr in c.lines:
                if msg == "BusRdX":
                    c.lines[addr] = "I"
                if msg == "BusRd" and c.lines[addr] == "M":
                    c.lines[addr] = "S"

    def print_states(self, addr):
        print("  Cache states for address", hex(addr))
        for c in self.caches:
            state = c.lines.get(addr, "I")
            print(f"    CPU{c.cpu_id}: {state}")
        print("-" * 40)

# ---------------- Simulation ----------------
sys = System(2)

ops = [("R", 0x1), ("W", 0x1), ("R", 0x1), ("W", 0x2)]

for i, (op, addr) in enumerate(ops):
    cpu = sys.caches[i % 2]
    cpu.access(addr, op, sys)
    sys.print_states(addr)
