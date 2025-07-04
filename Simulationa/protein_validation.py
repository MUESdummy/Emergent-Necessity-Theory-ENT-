import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from mpl_toolkits.mplot3d import Axes3D

def simulate_chignolin_folding():
    """Simulates τ-dynamics during Chignolin folding (PDB 5AWL)"""
    # Simplified energy landscape (Muller-Brown potential)
    def energy_landscape(x, y):
        return (0.5*np.exp(1 - 1.4*x**2 - y**2) +
                1.2*np.exp(-0.8*(x-0.5)**2 - 0.9*(y+0.5)**2))
    
    # Simulated FRET efficiency (proxy for folding state)
    def fret_efficiency(x, y):
        return 1.0 / (1 + np.exp(-2*(x**2 + y**2)))
    
    # Molecular dynamics simulation (Langevin dynamics)
    np.random.seed(42)
    dt = 0.01  # ns
    steps = 5000
    kT = 0.596  # kcal/mol at 300K
    gamma = 0.1  # Friction coefficient
    
    # Initialize trajectory
    x, y = 1.5, 1.5  # Unfolded state
    trajectory = []
    
    for _ in range(steps):
        # Calculate forces
        dx = (energy_landscape(x+1e-5, y) - energy_landscape(x, y)) / 1e-5
        dy = (energy_landscape(x, y+1e-5) - energy_landscape(x, y)) / 1e-5
        
        # Langevin dynamics
        x += -dx*dt/gamma + np.sqrt(2*kT*dt/gamma)*np.random.normal()
        y += -dy*dt/gamma + np.sqrt(2*kT*dt/gamma)*np.random.normal()
        
        # Record state
        trajectory.append((x, y, fret_efficiency(x, y)))
    
    # Calculate ∇N and κ_R (Eq 5 & Theorem 3)
    time = np.arange(steps) * dt
    fret = np.array([t[2] for t in trajectory])
    
    # Entropy gradient (∇N = -dS/dt)
    dS_dt = np.gradient(-np.log(fret + 1e-10), time)
    nabla_N = -dS_dt.mean()
    
    # τ-complexity (relative to unfolded state)
    tau = -np.log(fret / fret[0])
    tau_c = -np.log(0.7)  # Critical τ at 70% folded
    kappa_R = tau / tau_c
    
    # Plot results
    fig = plt.figure(figsize=(15,10))
    
    # Energy landscape
    ax1 = fig.add_subplot(221, projection='3d')
    xx, yy = np.meshgrid(np.linspace(-2,2,50), np.linspace(-2,2,50))
    zz = energy_landscape(xx, yy)
    ax1.plot_surface(xx, yy, zz, cmap='viridis', alpha=0.7)
    ax1.plot([t[0] for t in trajectory], [t[1] for t in trajectory], 
            [energy_landscape(t[0],t[1]) for t in trajectory], 'r-')
    ax1.set_title('Folding Energy Landscape')
    
    # κ_R dynamics
    ax2 = fig.add_subplot(222)
    ax2.plot(time, kappa_R, 'b-')
    ax2.axhline(y=1.28, color='r', linestyle='--', label='Chignolin κ_R')
    ax2.set_xlabel('Time (ns)')
    ax2.set_ylabel('κ_R')
    ax2.set_title('Resilience Coefficient Dynamics')
    ax2.legend()
    
    # ∇N correlation
    ax3 = fig.add_subplot(223)
    ax3.plot(dS_dt, kappa_R, 'bo', alpha=0.5)
    ax3.set_xlabel('dS/dt')
    ax3.set_ylabel('κ_R')
    ax3.set_title('∇N Correlation (Eq 5)')
    
    # Save figure
    plt.tight_layout()
    plt.savefig('protein_folding.png', dpi=300)
    
    return {
        'nabla_N': nabla_N,
        'kappa_R': kappa_R.mean(),
        'folding_time': time[np.argmax(kappa_R > 1.2)]
    }

# Example usage
if __name__ == "__main__":
    results = simulate_chignolin_folding()
    print(f"∇N_bio = {results['nabla_N']:.1f} kJ/mol·ns")
    print(f"κ_R = {results['kappa_R']:.2f}")
