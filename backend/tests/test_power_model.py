"""Tests for DVFS power model."""
from backend.dvfs_power_model import DVFSPowerModel

def test_power_scales_with_frequency():
    model = DVFSPowerModel()
    p_low = model.compute_power_watts(freq_ghz=1.0)
    p_high = model.compute_power_watts(freq_ghz=3.0)
    # Higher frequency with higher voltage must yield significantly higher power
    assert p_high > (p_low * 3.5)

def test_energy_zero_duration():
    model = DVFSPowerModel()
    assert model.compute_energy_joules(2.0, duration_seconds=0.0) == 0.0
