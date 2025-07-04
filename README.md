⚠️ NOTE: This repository is dedicated to the foundational theory (ENT) only.

# Emergent Necessity Theory (ENT) Simulations

This repository contains Python validation scripts for the theoretical framework presented in:

**AlShehail, A. (2025). A Unified Theory of Awareness Thresholds, Structural Evolution, and τ-Dynamics**

## Simulation Files

1. `quantum_validation.py`  
   - Validates Theorem 3 (κ<sub>R</sub> threshold) using IBM-Q Lima qubit decoherence
   - Output: `quantum_kappaR.png`

2. `protein_validation.py`  
   - Computes biological ∇N (Eq 5) for Chignolin folding (PDB 5AWL)
   - Output: `protein_folding.png`

3. `neural_validation.py`  
   - Analyzes HCP resting-state data for τ-complexity (Eq 1)
   - Output: `hcp_analysis.png`

4. `iit_correlation.py`  
   - Generates κ<sub>R</sub> ∝ Φ correlation plot (Eq 7)
   - Output: `iit_correlation.png`

## Installation
```bash
pip install numpy matplotlib scipy qiskit qiskit-ibm-runtime nilearn

----
To launch the MUES engine or view its simulation papers, use:  
→ https://github.com/MUESdummy/Mues-Engine  
→ https://muesdummy.github.io/Mues-Engine/


