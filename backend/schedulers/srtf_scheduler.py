"""
Preemptive Shortest Remaining Time First (SRTF) scheduler.
"""

from typing import List, Dict, Any
from backend.schedulers.base_scheduler import BaseScheduler, Process

class SRTFScheduler(BaseScheduler):
    def __init__(self, context_switch_cost: float = 0.1):
        super().__init__("SRTF")
        self.context_switch_cost = context_switch_cost

    def schedule(self, processes: List[Process]) -> Dict[str, Any]:
        """Execute SRTF simulation tracking context switches."""
        time = 0.0
        completed = []
        ready_queue = []
        context_switches = 0
        current_proc = None
        
        # Sort by arrival
        remaining = sorted(processes, key=lambda p: p.arrival_time)
        
        while len(completed) < len(processes):
            # Enqueue newly arrived
            while remaining and remaining[0].arrival_time <= time:
                ready_queue.append(remaining.pop(0))
                
            if not ready_queue:
                if remaining:
                    time = remaining[0].arrival_time
                continue
                
            # Pick shortest remaining
            ready_queue.sort(key=lambda p: p.remaining_time)
            chosen = ready_queue.pop(0)
            
            if current_proc != chosen:
                context_switches += 1
                time += self.context_switch_cost
                current_proc = chosen
                
            # Run for 1.0 unit or until completion / arrival
            run_step = min(chosen.remaining_time, 1.0)
            chosen.remaining_time -= run_step
            time += run_step
            
            if chosen.remaining_time <= 0.0:
                chosen.completion_time = time
                chosen.turnaround_time = chosen.completion_time - chosen.arrival_time
                chosen.waiting_time = chosen.turnaround_time - chosen.burst_time
                completed.append(chosen)
                current_proc = None
            else:
                ready_queue.append(chosen)
                
        avg_wait = sum(p.waiting_time for p in completed) / len(completed)
        avg_tat = sum(p.turnaround_time for p in completed) / len(completed)
        
        return {
            "algorithm": "SRTF",
            "avg_waiting_time": round(avg_wait, 2),
            "avg_turnaround_time": round(avg_tat, 2),
            "total_context_switches": context_switches
        }
