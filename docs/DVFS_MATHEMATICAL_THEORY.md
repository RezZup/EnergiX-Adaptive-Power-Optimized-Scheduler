# Dynamic Voltage and Frequency Scaling (DVFS) Mathematical Theory

EnergiX implements energy-aware scheduling based on CMOS dynamic and static power dissipation physics.

## 1. Physical Power Equations

The total power consumption $P_{total}$ of a CMOS processor core consists of dynamic switching power and static leakage power:

$$P_{total} = P_{dynamic} + P_{static}$$

Where:
$$P_{dynamic} = \alpha \cdot C_{eff} \cdot V_{dd}^2 \cdot f$$
$$P_{static} = V_{dd} \cdot I_{leakage}$$

- $\alpha$: Activity factor (fraction of gates switching per clock cycle)
- $C_{eff}$: Effective load capacitance
- $V_{dd}$: Operating supply voltage
- $f$: Clock operating frequency

Because voltage scales approximately linearly with frequency in the stable operating region ($V_{dd} \propto f$), dynamic power scales cubically:

$$P_{dynamic} \propto f^3$$

## 2. Energy Minimization Principle

The total energy consumed to execute a workload with clock cycles $N_{cycles}$ at frequency $f$ during execution time $T = \frac{N_{cycles}}{f}$ is:

$$E = P_{dynamic} \cdot T = (C_{eff} \cdot V_{dd}^2 \cdot f) \cdot \left(\frac{N_{cycles}}{f}\right) = C_{eff} \cdot V_{dd}^2 \cdot N_{cycles}$$

By reducing operating frequency and supply voltage during task slack periods, quadratic energy savings are achieved while meeting deadline constraints.
