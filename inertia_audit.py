import numpy as np

def corrected_inertia_analysis():
    """
    Corrected analysis of inertial coupling for flyby anomalies.
    """
    # Constants
    R = 6371.0  # Earth radius in km
    omega = 7.2921159e-5  # rad/s
    R_m = R * 1000  # meters
    
    # 1. Required acceleration
    delta_v = 0.013  # m/s (13 mm/s)
    tau = 1000  # seconds
    a_req = delta_v / tau
    
    # 2. Centrifugal reference
    a_c = omega**2 * R_m
    
    # 3. Coupling ratio
    coupling_ratio = a_req / a_c
    
    print("=== CORRECTED FLYBY ANOMALY ANALYSIS ===")
    print(f"Required acceleration: {a_req:.2e} m/s²")
    print(f"Centrifugal acceleration: {a_c:.2e} m/s²")
    print(f"Required coupling: {coupling_ratio*100:.4f}%")
    print()
    
    # 4. Shell thickness calculation
    def I_over_MR2(thickness_km):
        """Calculate I/MR² for given shell thickness in km"""
        t = thickness_km
        R_inner = R - t
        numerator = R**5 - R_inner**5
        denominator = R**3 - R_inner**3
        I_over_M = (2/5) * numerator / denominator
        return I_over_M / (R**2)
    
    # Measured Earth value
    I_earth = 0.3307
    
    # Required increase
    required_I = I_earth * (1 + coupling_ratio)
    
    print(f"Earth measured I/MR²: {I_earth:.4f}")
    print(f"Required I/MR²: {required_I:.6f}")
    print(f"Required increase: {(required_I - I_earth):.6f}")
    print()
    
    # Find thickness that gives required I
    # Binary search
    low, high = 0, R
    target = required_I
    
    for _ in range(50):
        mid = (low + high) / 2
        I_mid = I_over_MR2(mid)
        if I_mid > target:
            high = mid
        else:
            low = mid
    
    required_thickness = (low + high) / 2
    
    print(f"Required shell thickness: {required_thickness:.3f} km")
    print(f"                      = {required_thickness*1000:.0f} meters")
    print()
    
    # 5. Comparison with claimed 45km
    I_45km = I_over_MR2(45)
    print(f"I/MR² for 45km shell: {I_45km:.4f}")
    print(f"Increase vs Earth: {((I_45km/I_earth)-1)*100:.1f}%")
    print(f"Overestimate factor: {45/required_thickness:.0f}x")
    
    return required_thickness

if __name__ == "__main__":
    corrected_inertia_analysis()
