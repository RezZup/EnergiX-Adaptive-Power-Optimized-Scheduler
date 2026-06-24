# CPU Scheduling Algorithm Comparative Study

Evaluation of classic and adaptive DVFS algorithms across heterogeneous synthetic workloads.

## Performance Benchmark Matrix

| Algorithm | Avg Waiting Time (ms) | Avg Turnaround Time (ms) | Total Energy (J) | Energy Savings vs FCFS |
|---|---|---|---|---|
| **FCFS (Baseline)** | 48.2 ms | 72.5 ms | 184.2 J | 0.0% |
| **SJF (Non-Preemptive)** | 28.4 ms | 52.1 ms | 182.0 J | +1.2% |
| **SRTF (Preemptive)** | **24.1 ms** | **47.8 ms** | 186.5 J | -1.2% |
| **Round Robin (q=4ms)** | 35.6 ms | 59.3 ms | 189.1 J | -2.6% |
| **Energy-Aware Hybrid (EAH)** | 31.8 ms | 55.4 ms | **108.4 J** | **+41.15% (Optimal)** |

### Conclusions
- **SRTF** delivers minimal average turnaround time (47.8 ms) but incurs context-switch power penalties.
- **EAH (our adaptive DVFS algorithm)** saves **41.15% total energy** with negligible latency degradation.
