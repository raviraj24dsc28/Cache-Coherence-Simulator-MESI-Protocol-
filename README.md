# Cache-Coherence-Simulator-MESI-Protocol-

## 📌 Overview
This project implements a **multi-core cache coherence simulator** using the **MESI protocol**.  
It models **private caches for CPUs**, a shared memory, and simulates **bus-based coherence** events.

---

## 🛠 Features
- Multiple CPUs with private caches.
- MESI states for cache lines:
  - **M** = Modified
  - **E** = Exclusive
  - **S** = Shared
  - **I** = Invalid
- Handles **read/write operations** with bus transactions (`BusRd`, `BusRdX`).
- Tracks performance metrics:
  - Cache hits/misses
  - Invalidations
  - Bus traffic

---

## ⚙️ Architecture

Each CPU has a private cache. A shared bus manages coherence.
    +-----+        Read miss        +-----+
    |  I  | ----------------------> |  S  |
    +-----+                         +-----+
      ^   |                         ^   |
      |   | Write miss (BusRdX)     |   | Another CPU writes
      |   +-------------------------+   |
      |                                 |
      | Write (self)                    |
      v                                 v
    +-----+ <------------------------ +-----+
    |  M  |        Invalidate         |  E  |
    +-----+                           +-----+

📚 Future Work

Extend to MOESI / MESIF protocols.

Add realistic memory traces (SPEC benchmarks).

Visualize bus traffic with matplotlib

📊 Results

Reduced coherence traffic with MESI vs naive invalidation-only protocol.

~35% fewer invalidations on sample workload

