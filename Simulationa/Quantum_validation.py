import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import QiskitRuntimeService

def simulate_qubit_decoherence(qubit_index: int, shots: int = 1024):
    """Simulates τ-dynamics during qubit decoherence on IBM-Q Lima"""
    # Connect to IBM Quantum (replace with your API token)
    service = QiskitRuntimeService(channel="ibm_quantum", token="YOUR_API_TOKEN")
    backend = service.backend("ibmq_lima")
    
    # Configure T1/T2 times from device calibration
    t1 = backend.properties().t1(qubit_index) * 1e9  # Convert to ns
    t2 = backend.properties().t2(qubit_index) * 1e9
    
    # Create time evolution points
    time_points = np.linspace(0, 3*t2, 50)
    kappa_R_values = []
    
    for t in time_points:
        # Build decoherence circuit
        qc = QuantumCircuit(1, 1)
        qc.x(0)  # Initialize to |1>
        qc.delay(t, 0, unit='ns')  # Decoherence time
        qc.measure(0, 0)
        
        # Simulate with noise model
        simulator = AerSimulator.from_backend(backend)
        tqc = transpile(qc, simulator)
        result = simulator.run(tqc, shots=shots).result()
        
        # Calculate |1> probability
        p1 = result.get_counts().get('1', 0) / shots
        
        # Compute τ and κ_R (Eq 1 & Theorem 3)
        tau = -np.log(p1) if p1 > 0 else 0
        tau_c = -np.log(0.5)  # Critical τ at P(|1>) = 0.5
        kappa_R = tau / tau_c if tau_c > 0 else 0
        
        kappa_R_values.append(kappa_R)
    
    # Plot results
    plt.figure(figsize=(10,6))
    plt.plot(time_points, kappa_R_values, 'b-', label='κ_R')
    plt.axhline(y=1.15, color='r', linestyle='--', label='Awareness Threshold')
    plt.axvline(x=t2, color='g', linestyle=':', label='T2 Time')
    plt.xlabel('Time (ns)')
    plt.ylabel('Resilience Coefficient (κ_R)')
    plt.title(f'Qubit {qubit_index} Decoherence τ-Dynamics\nIBM-Q Lima')
    plt.legend()
    plt.grid(True)
    plt.savefig('quantum_kappaR.png', dpi=300)
    
    return {
        't1': t1,
        't2': t2,
        'critical_time': time_points[np.argmax(np.array(kappa_R_values) > 1.15],
        'nabla_N': np.gradient(kappa_R_values, time_points).mean()
    }

# Example usage
if __name__ == "__main__":
    results = simulate_qubit_decoherence(qubit_index=0)
    print(f"∇N = {results['nabla_N']:.5f} ns⁻¹")
    print(f"Awareness threshold crossed at t = {results['critical_time'][0]:.1f} ns")
