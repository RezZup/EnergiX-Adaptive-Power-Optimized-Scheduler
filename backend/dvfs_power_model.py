"""
DVFS dynamic and static power dissipation modeling engine.
"""

from typing import Dict, Any

class DVFSPowerModel:
    """
    Calculates CPU power consumption based on CMOS physical parameters.
    """
    def __init__(
        self,
        base_capacitance: float = 1.0,
        leakage_current: float = 0.05,
        voltage_frequency_table: Dict[float, float] = None
    ):
        self.c_eff = base_capacitance
        self.i_leak = leakage_current
        # Default mapping of frequency (GHz) to required core voltage (V)
        self.vf_table = voltage_frequency_table or {
            1.0: 0.85,
            1.5: 0.95,
            2.0: 1.05,
            2.5: 1.18,
            3.0: 1.30,
        }

    def compute_power_watts(self, freq_ghz: float, alpha: float = 0.8) -> float:
        """Compute total core power in Watts at given frequency."""
        voltage = self.vf_table.get(freq_ghz, 1.2)
        p_dyn = alpha * self.c_eff * (voltage ** 2) * freq_ghz
        p_stat = voltage * self.i_leak
        return p_dyn + p_stat

    def compute_energy_joules(self, freq_ghz: float, duration_seconds: float, alpha: float = 0.8) -> float:
        """Compute energy consumption (Joules) for a task burst."""
        power_w = self.compute_power_watts(freq_ghz, alpha)
        return power_w * duration_seconds
