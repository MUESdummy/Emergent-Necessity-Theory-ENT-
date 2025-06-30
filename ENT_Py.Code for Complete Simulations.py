import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from qiskit import Aer
from qiskit.algorithms import QAOA
from qiskit.algorithms.optimizers import COBYLA
from qiskit.opflow import Z, I
from qiskit.circuit.library import TwoLocal
from qiskit.quantum_info import Statevector

# ========================
# SIMULATION 1: STRING VACUA SELECTION
# ========================
np.random.seed(42)
traces = np.abs(np.random.normal(1.0, 0.3, 10000))
dets = np.abs(np.random.normal(0.5, 0.2, 10000))
τ_vacua = traces / np.sqrt(dets)
τ_c_vac = 1.8
stable_mask = τ_vacua >= τ_c_vac
stable_fraction = np.mean(stable_mask) * 100
m_susy = np.exp(τ_c_vac - np.median(τ_vacua[~stable_mask]))

# Plot
plt.figure(figsize=(10,6))
plt.hist(τ_vacua, bins=50, alpha=0.7, color='skyblue', label='All Vacua')
plt.hist(τ_vacua[stable_mask], bins=50, alpha=0.7, color='orange', label=f'Stable Vacua ($\\tau \\geq {τ_c_vac}$)')
plt.axvline(τ_c_vac, color='r', linestyle='--', lw=2, label='$\\tau_c$')
plt.title('ENT Vacuum Selection: $\\tau \\geq \\tau_c$')
plt.xlabel('Coherence $\\tau$')
plt.ylabel('Count')
plt.legend()
plt.annotate(f'Stable Fraction: {stable_fraction:.1f}%\nSUSY Scale: {m_susy:.2f} TeV', 
             xy=(0.65, 0.85), xycoords='axes fraction', fontsize=12,
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))
plt.grid(alpha=0.2)
plt.savefig('vacua_selection.png', dpi=300, bbox_inches='tight')

# ========================
# SIMULATION 2: GRAVITATIONAL SIGNATURES
# ========================
x = np.linspace(0, 10, 1000)
dx = x[1] - x[0]
τ = 2.0 * np.exp(-0.5 * ((x-5)/1.5)**2)
d2τ_dx2 = np.gradient(np.gradient(τ, dx), dx)

χ = 1.0
ΔG = -χ * d2τ_dx2
ΔG_max = np.max(np.abs(ΔG))
ligo_bound = 1e-19
χ_max = ligo_bound / ΔG_max

plt.figure(figsize=(12,8))
plt.subplot(211)
plt.plot(x, τ, 'b-', lw=2.5)
plt.title('Cosmic Coherence Field $\\tau(x)$')
plt.ylabel('$\\tau$')
plt.grid(alpha=0.2)

plt.subplot(212)
plt.plot(x, ΔG, 'r-', lw=2)
plt.fill_between(x, ΔG, 0, where=ΔG>0, color='red', alpha=0.15)
plt.fill_between(x, ΔG, 0, where=ΔG<0, color='blue', alpha=0.15)
plt.title('ENT Gravitational Signature $\\Delta G_{\\mu\\nu} = -\\chi \\nabla_\\mu \\nabla_\\nu \\tau$')
plt.xlabel('Cosmic Scale (Mpc)')
plt.ylabel('$\\Delta G$')
plt.axhline(0, color='k', ls='--', alpha=0.5)
plt.annotate(f'LIGO constraint: $\\chi < {χ_max:.2e} \\, \\mathrm{{m}}^2$', 
             xy=(0.4, 0.9), xycoords='axes fraction', fontsize=10,
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray"))
plt.grid(alpha=0.2)
plt.tight_layout()
plt.savefig('grav_signature.png', dpi=300, bbox_inches='tight')

# ========================
# SIMULATION 3: QUANTUM τ-MAXIMIZATION (QAOA)
# ========================
# ENT Hamiltonian: Maximize ∑<Z_i Z_j>
graph = [(0,1), (1,2)]
H_τ = - (Z^Z^I) - (I^Z^Z)

# QAOA setup
optimizer = COBYLA(maxiter=100)
qaoa = QAOA(optimizer=optimizer, reps=2, quantum_instance=Aer.get_backend('statevector_simulator'))
result = qaoa.compute_minimum_eigenvalue(H_τ)
optimal_params = result.optimal_parameters
τ_value = -result.eigenvalue.real
τ_c_quant = 1.5

# Get statevector
qc_opt = qaoa.construct_circuit(optimal_params, H_τ)[0]
statevector = Aer.get_backend('statevector_simulator').run(qc_opt).result().get_statevector()
probs = Statevector(statevector).probabilities()

print("\n=== FINAL RESULTS ===")
print(f"Stable vacua fraction: {stable_fraction:.1f}% (τ_c = {τ_c_vac})")
print(f"SUSY scale prediction: {m_susy:.2f} TeV")
print(f"LIGO χ constraint: < {χ_max:.2e} m²")
print(f"QAOA τ: {τ_value:.4f} (τ_c = {τ_c_quant})")