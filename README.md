# Prob2-of-Process-Scheduling- 

Imagine a busy hospital emergency room where patients arrive at different times and have different levels of urgency. Given the data below, use the FCFS, SJF, PS, and RR scheduling algorithms to determine the order in which patients should be attended to. After applying each algorithm, discuss which one provides the most efficient and fair scheduling.

| Patient | Arrival Time | Estimated Treatment Time | Urgency Level (1-5, 5 being most urgent) |
|---------|--------------|--------------------------|----------------------------------------|
|   A     |     00:00    |           30 mins        |                 3                      |
|   B     |     00:10    |           20 mins        |                 5                      |
|   C     |     00:15    |           40 mins        |                 2                      |
|   D     |     00:20    |           15 mins        |                 4                      |


## Scheduling Algorithms


### FCFS (First-Come, First-Served)

In FCFS, patients are attended to in the order they arrive.

Order of Patients (FCFS):
1. A
2. B
3. C
4. D

### SJF (Shortest Job First)

In SJF, patients with the shortest estimated treatment time are prioritized.

Order of Patients (SJF):
1. D
2. B
3. A
4. C

### PS (Priority Scheduling)

In PS, patients with higher urgency levels are attended to first.

Order of Patients (PS):
1. B (Urgency Level: 5)
2. D (Urgency Level: 4)
3. A (Urgency Level: 3)
4. C (Urgency Level: 2)

### RR (Round Robin) with Time Quantum (TQ) of 10 mins

In RR, patients are attended to in a round-robin manner with a specified time quantum.

Order of Patients (RR with TQ = 10 mins):
1. A (Remaining Time: 20 mins)
2. B (Remaining Time: 10 mins)
3. C (Remaining Time: 30 mins)
4. D (Remaining Time: 5 mins)
5. A (Remaining Time: 10 mins)
6. B (Remaining Time: 0 mins)
7. C (Remaining Time: 20 mins)
8. D (Remaining Time: 0 mins)
9. A (Remaining Time: 0 mins)

## Discussion

The choice of the most suitable algorithm depends on the hospital's priorities. If urgency levels are a crucial factor, Priority Scheduling (PS) would be the best choice. However, if a balance between efficiency and fairness is desired, Round Robin (RR) with an appropriate time quantum can be a reasonable compromise. Ultimately, the choice should align with the hospital's policies and patient needs.

