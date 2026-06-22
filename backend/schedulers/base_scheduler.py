"""
Base abstract scheduler defining metrics and task records.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any

class Process:
    def __init__(self, pid: int, arrival_time: float, burst_time: float, priority: int = 1):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.start_time = None
        self.completion_time = None
        self.waiting_time = 0.0
        self.turnaround_time = 0.0

class BaseScheduler(ABC):
    def __init__(self, name: str):
        self.name = name
        
    @abstractmethod
    def schedule(self, processes: List[Process]) -> Dict[str, Any]:
        pass
