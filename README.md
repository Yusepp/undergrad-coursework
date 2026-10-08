# Undergrad Coursework (UB)

Consolidated coursework from my undergrad years at Universitat de Barcelona.
The original per-course repositories were merged here (one folder each) and
deleted, to keep my GitHub profile focused. Repos marked *(fork)* were forks
of course/upstream material; only the state at consolidation time is kept.

| Folder | Origin | Content |
|---|---|---|
| `AI` | `Yusepp/AI` | Intro AI coursework |
| `Computer-Vision` | `Yusepp/Computer-Vision` | Computer vision practicums P1–P6 (notebooks) |
| `Parcial1TNUI` | `Yusepp/Parcial1TNUI` | Course midterm material |
| `SO2` | `Yusepp/SO2` | Operating Systems II practicums P2–P5 (C) — see note below |
| `prac0_SD` | `Yusepp/prac0_SD` *(fork of UB-GEI-SD)* | Distributed Systems starter (JAXB) |
| `Software-Distribuido` | `Yusepp/Software-Distribuido` | Distributed software coursework |
| `PP` | `Yusepp/PP` | Parallel programming (Programación Paralela) |
| `NOAA-API` | `Yusepp/NOAA-API` | Small API to fetch NOAA weather datasets |
| `TFG-API` | `Yusepp/TFG-API` | Final degree project: Django database API |
| `ml_ub` | `Yusepp/ml_ub` *(fork of ssegui/ml_ub)* | Machine Learning course @ UB |
| `practicalAI` | `Yusepp/practicalAI` *(fork of GokuMohandas/Made-With-ML)* | Practical ML notes |

Notes on consolidation:
- `.ipynb_checkpoints/`, `.git/`, editor lockfiles and OS artifacts were dropped.
- `SO2/`: the `src/base_dades/` dataset (~677 MB) was byte-identical in
  P2/P3/P4/P5, so a single copy is kept under `SO2/P2/src/base_dades/`
  and referenced by the other practicums.
- History of the original repos was not preserved (working-tree snapshot);
  per-repo history lived in the deleted repos.
