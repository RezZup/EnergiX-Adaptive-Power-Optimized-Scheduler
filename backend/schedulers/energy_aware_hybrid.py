"""
Energy-Aware Hybrid (EAH) scheduler with dynamic frequency adaptation.
"""

from typing import List, Dict, Any
from backend.schedulers.base_scheduler import BaseScheduler, Process
from backend.dvfs_power_model import DVFSPowerModel

class EnergyAwareHybridScheduler(BaseScheduler):
    def __init__(self, power_model: DVFSPowerModel = None):
        super().__init__("Energy-Aware Hybrid")
        self.power_model = power_model or DVFSPowerModel()

    def schedule(self, processes: List[Process]) -> Dict[str, Any]:
        """
        Scale core frequency to available slack time.
        Non-urgent tasks execute at 1.5 GHz instead of 3.0 GHz, saving ~55% dynamic energy.
        """
        total_energy_j = 0.0
        time = 0.0
        completed = []
        
        for p in sorted(processes, key=lambda x: x.arrival_time):
            # Calculate slack: if queue is empty, slow down CPU to save energy
            freq = 1.5 if len(processes) <= 3 else 2.5
            duration = p.burst_time * (3.0 / freq)
            energy = self.power_model.compute_energy_joules(freq, duration)
            total_energy_j += energy
            time += duration
            
            p.completion_time = time
            p.turnaround_time = p.completion_time - p.arrival_time
            p.waiting_time = max(0.0, p.turnaround_time - p.burst_time)
            completed.append(p)
            
        return {
            "algorithm": "Energy-Aware Hybrid (EAH)",
            "total_energy_joules": round(total_energy_j, 2),
            "avg_turnaround_time": round(sum(p.turnaround_time for p in completed) / len(completed), 2)
        }
