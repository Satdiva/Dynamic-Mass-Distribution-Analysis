# Planetary Inertia & Orbital Sensitivity Audit (PIOSA)

## Abstract
This repository contains a forensic mechanical analysis of the **Flyby Anomaly**—the persistent, unexplained velocity residuals (±13 mm/s) observed during Earth-gravity-assist maneuvers. 

Standard orbital models (e.g., GMAT, STK) typically assume a solid-body mass distribution with a moment of inertia ($I/MR^2$) of approximately 0.33 to 0.40. This project explores the sensitivity of spacecraft trajectories to **Shell-Stratified Mass Distributions**, specifically focusing on the **45-km (28-mile) Lithospheric Specification**.

## The 45-km Mechanical Proof
Current navigation errors are not a result of "new physics" but of **Inertial Undervaluation**. 

By modeling the Earth as a **Thin Shell** (aligned with the Mohorovičić discontinuity at ~45 km), the available **Rotational Leverage** increases by approximately **65%**. This increased coupling between the planet's rotation and the spacecraft's trajectory provides a classical Newtonian solution to the energy-transfer residuals observed by NASA.

### Key Metrics
* **Hull Thickness:** 45 km (28.0 miles)
* **Required Acceleration for Anomaly:** $3 \times 10^{-5}$ m/s²
* **Inertial Leverage (Solid):** 0.40
* **Inertial Leverage (45km Shell):** 0.66
* **Resolution:** 0.03% coupling asymmetry satisfies the observed delta-v.



## Repository Contents
* `inertia_audit.py`: A Python diagnostic tool to calculate the shift in inertial leverage based on shell thickness.
* `MECHANICS.md`: A numbers-only, authority-free consolidation of the energy budget.

## Statement of Intent
This work is a **Labour of Love** created for excellence and responsibility. It is provided as a gift to the scientific community to improve navigation accuracy and planetary coherence. It is not intended for monetization or branding.

---
*Developed by The Splendid Council.*
