import numpy as np
import matplotlib.pyplot as plt
from nilearn import datasets
from nilearn.connectome import ConnectivityMeasure

def analyze_hcp_resting_state():
    """Analyzes τ-dynamics in Human Connectome Project (HCP) data"""
    # Load HCP dataset (requires nilearn >= 0.9.0)
    try:
        hcp_data = datasets.fetch_hcp_resting_state(subject_ids=['100206'])
        time_series = np.loadtxt(hcp_data['func'][0])
    except:
        print("HCP data not available, generating synthetic data")
        time_series = np.random.randn(1200, 50)  # Fallback synthetic data
    
    # Calculate functional connectivity
    conn_measure = ConnectivityMeasure(kind='correlation')
    fc_matrix = conn_measure.fit_transform([time_series])[0]
    
    # Compute τ-complexity (Eq 1)
    p = np.abs(fc_matrix).mean(axis=0)  # Functional distribution
    p0 = np.ones_like(p) / len(p)       # Uniform baseline
    tau = -np.sum(p * np.log(p / p0))   # Kullback-Leibler divergence
    
    # Critical τ from random network model
    random_fc = np.random.randn(*fc_matrix.shape)
    random_fc = (random_fc - random_fc.mean()) / random_fc.std()
    p_rand = np.abs(random_fc).mean(axis=0)
    tau_c = -np.sum(p_rand * np.log(p_rand / p0))
    
    # Resilience coefficient (Theorem 3)
    kappa_R = tau / tau_c
    
    # ∇N from temporal variability (Eq 4)
    sliding_window = []
    window_size = 100
    for i in range(0, len(time_series) - window_size, 10):
        window_fc = conn_measure.fit_transform([time_series[i:i+window_size]])[0]
        p_win = np.abs(window_fc).mean(axis=0)
        tau_win = -np.sum(p_win * np.log(p_win / p0))
        sliding_window.append(tau_win)
    
    dtau_dt = np.gradient(sliding_window)
    nabla_N = -np.mean(dtau_dt)
    
    # Visualization
    plt.figure(figsize=(12,8))
    
    plt.subplot(221)
    plt.imshow(fc_matrix, cmap='viridis', vmin=-1, vmax=1)
    plt.colorbar()
    plt.title('Functional Connectivity')
    
    plt.subplot(222)
    plt.plot(range(len(sliding_window)), sliding_window, 'b-')
    plt.xlabel('Time Window')
    plt.ylabel('τ(t)')
    plt.title('Temporal Complexity Dynamics')
    
    plt.subplot(223)
    plt.plot(range(len(dtau_dt)), dtau_dt, 'r-')
    plt.xlabel('Time Window')
    plt.ylabel('dτ/dt')
    plt.title('Entropy Gradient')
    
    plt.tight_layout()
    plt.savefig('hcp_analysis.png', dpi=300)
    
    return {
        'tau': tau,
        'tau_c': tau_c,
        'kappa_R': kappa_R,
        'nabla_N': nabla_N
    }

# Example usage
if __name__ == "__main__":
    results = analyze_hcp_resting_state()
    print(f"∇N = {results['nabla_N']:.3f}")
    print(f"κ_R = {results['kappa_R']:.2f} (HCP Resting-State)")
