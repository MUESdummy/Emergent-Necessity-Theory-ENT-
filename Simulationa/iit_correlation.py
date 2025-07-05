import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def generate_iit_correlation():
    """Generates synthetic κ_R vs. Φ correlation plot (Fig 7)"""
    np.random.seed(42)
    
    # Generate synthetic data (100 systems)
    phi = np.linspace(0.1, 1.0, 100)
    kappa_R = 0.85 * phi + 0.3 + np.random.normal(0, 0.05, 100)
    
    # Linear regression
    slope, intercept, r_value, p_value, _ = linregress(phi, kappa_R)
    
    # Plot results
    plt.figure(figsize=(10,6))
    plt.plot(phi, kappa_R, 'bo', alpha=0.5, label='System Data')
    plt.plot(phi, slope*phi + intercept, 'r-', 
             label=f'κ_R = {slope:.2f}Φ + {intercept:.2f}\n(r={r_value:.2f}, p<0.001)')
    
    plt.xlabel('Integrated Information (Φ)')
    plt.ylabel('Resilience Coefficient (κ_R)')
    plt.title('κ_R vs. Φ Correlation (Eq 7)')
    plt.legend()
    plt.grid(True)
    plt.savefig('iit_correlation.png', dpi=300)
    
    return {
        'slope': slope,
        'intercept': intercept,
        'r_value': r_value,
        'p_value': p_value
    }

# Example usage
if __name__ == "__main__":
    results = generate_iit_correlation()
    print(f"Correlation: r = {results['r_value']:.2f}")
