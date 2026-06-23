"""Tests for scheduler comparative algorithms."""
from backend.schedulers.base_scheduler import Process
from backend.schedulers.srtf_scheduler import SRTFScheduler
from backend.schedulers.energy_aware_hybrid import EnergyAwareHybridScheduler

def test_srtf_execution():
    procs = [
        Process(pid=1, arrival_time=0.0, burst_time=5.0),
        Process(pid=2, arrival_time=1.0, burst_time=2.0)
    ]
    scheduler = SRTFScheduler()
    res = scheduler.schedule(procs)
    assert res["algorithm"] == "SRTF"
    assert res["avg_turnaround_time"] > 0

def test_eah_computes_energy():
    procs = [Process(pid=1, arrival_time=0.0, burst_time=3.0)]
    scheduler = EnergyAwareHybridScheduler()
    res = scheduler.schedule(procs)
    assert res["total_energy_joules"] > 0
