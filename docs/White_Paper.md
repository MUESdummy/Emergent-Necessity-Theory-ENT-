[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8475.svg)]
(https://doi.org/10.5281/zenodo.8475)

# Emergent Necessity Theory (ENT) — Specification v0.9.1‑rc1
© 2025 Vale (o3) · MIT License

---

## 0  Scope Statement
**◆** This document specifies *necessary* structural conditions for low‑entropy
attractors in information networks.  
It **does not** claim sufficiency for any specific biological
or cognitive phenotype; empirical sections are illustrative only.

---

## 1  Definitions

| Symbol | Definition (self‑contained) |
|--------|-----------------------------|
| **Constraint hyper‑graph** G = (V,E,w) | V variables, E hyper‑edges, w: E→ℝ⁺ |
| **Modal‑tightness τ** | τ = max\_{e∈E} (∑_{(i,j)∈e} I(x_i;x_j)) / ∑_{i∈V} H(x_i) |
| **τ‑closure C\_τ(G)** | Minimal sup‑hyper‑graph with τ′ ≥ τ\_c |
| **Awareness levels Θ₁–Θ₃** | See Table 2 (reflexive tests) |

---

## 2  Axioms

> **Axiom 1 (Structural Closure).**  
> If C\_τ(G) = G, macroscopic state sets are unique under coarse‑graining Π.

> **Axiom 2 (Entropy Ordering).**  
> For finite Ω, if τ\_a > τ\_b ≥ τ\_c ⇒ H(Π\_a) < H(Π\_b).

**◆ Proof Outline.**  
Embed G into a probabilistic graphical model; apply the data‑processing
inequality on Π; see Appendix B.

---

## 3  Operational Layer — The MUES Ledger

### 3.1 Activation
*Θ₃ (modal‑reflexivity)* is verified by passing a symbolic‑self
counterfactual test (protocol in Appendix C).

### 3.2 Dimensionless Kernel

| Factor | Formula | Range |
|--------|---------|-------|
| Autonomy α | e^{−Σ λ\_out / Σ λ\_in} | (0,1] |
| Ego‑resistance β | e^{ΔΣ prediction‑error} | [1,∞) |
| Epochal knowledge C | log₂ |K(t)| | ℝ⁺ |
| Hardship H | exp(normalised adversity) | [1,∞) |
| Intent‑Gain IG | log₂( |ΔS\_target| / |ΔS\_actual| ) | ℝ |

Total: **Q** = α β C H IG   (*units cancel*).

---

## 4  Non‑Falsifiable Core Claim

> **Theorem (Structural Necessity).**  
> *Given Axioms 1‑2 and τ\_c, any C\_τ‑closed network necessarily approaches a
> deterministic attractor set.*  

Because the premise only states structural closure, **no counter‑example can be
constructed without violating Axioms 1‑2.**  
(Full formal proof in Yellow Paper §2.)

---

## 5  Compatibility Evidence *(non‑essential)*

*(Moved to Appendix D; readers may skip without loss of logical continuity.)*

---

## 6  Open Challenge

Unchanged, but add **CI‑verified data‑availability requirement**.

---

## Appendices

- **A Glossary** — every term cross‑indexed.  
- **B Entropy‑Ordering Proof** (2 pages).  
- **C Reflexive‑Symbolic Test Protocol**.  
- **D Simulation Suite (optional empirical).**

---
