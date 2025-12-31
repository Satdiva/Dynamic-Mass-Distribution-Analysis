import numpy as np

def calculate_inertial_leverage(thickness_km=45):
    """
    Compares the Inertial Leverage of a Solid Sphere (Mainstream) 
    vs. a Thin Shell (Splendid Maintenance Model).
    """
    R_earth = 6371.0  # Mean radius in km
    
    # 1. Mainstream: Solid Uniform Sphere
    I_solid = 0.40
    
    # 2. Splendid: Thin Shell Model
    # Moment of Inertia for a thick spherical shell: 
    # I = (2/5) * (R_outer^5 - R_inner^5) / (R_outer^3 - R_inner^3)
    r_outer = R_earth
    r_inner = R_earth - thickness_km
    
    I_shell_ratio = (2/5) * (r_outer**5 - r_inner**5) / (r_outer**3 - r_inner**3)
    normalized_I_shell = I_shell_ratio / (R_earth**2)

    leverage_increase = (normalized_I_shell - I_solid) / I_solid * 100

    print(f"--- Planetary Maintenance Audit: Inertial Leverage ---")
    print(f"Hull Thickness: {thickness_km} km")
    print(f"Solid Model Ratio (I/MR^2): {I_solid:.4f}")
    print(f"Shell Model Ratio (I/MR^2): {normalized_I_shell:.4f}")
    print(f"Inertial Leverage Gain: {leverage_increase:.2f}%")
    print(f"------------------------------------------------------")
    print("Conclusion: The Shell model provides significantly higher")
    print("rotational coupling for spacecraft flyby interaction.")

if __name__ == "__main__":
    calculate_inertial_leverage(45)
  
