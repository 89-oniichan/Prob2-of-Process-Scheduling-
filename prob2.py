# -*- coding: utf-8 -*-
"""prob2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oZs-yMqGoaPjnyohWdG3ucv_T0-Tlkjg
"""

import heapq
from collections import deque

# Patient data
patients = [
    {'name': 'A', 'arrival_time': 0, 'treatment_time': 30, 'urgency_level': 3},
    {'name': 'B', 'arrival_time': 10, 'treatment_time': 20, 'urgency_level': 5},
    {'name': 'C', 'arrival_time': 15, 'treatment_time': 40, 'urgency_level': 2},
    {'name': 'D', 'arrival_time': 20, 'treatment_time': 15, 'urgency_level': 4}
]

# First-Come-First-Served (FCFS) Scheduling
def fcfs_scheduling(patients):
    patients.sort(key=lambda x: x['arrival_time'])
    return patients

# Shortest Job First (SJF) Scheduling
def sjf_scheduling(patients):
    patients.sort(key=lambda x: (x['treatment_time'], x['arrival_time']))
    return patients

# Priority Scheduling (PS) - Lower priority number means higher urgency
def ps_scheduling(patients):
    patients.sort(key=lambda x: (x['urgency_level'], x['arrival_time']))
    return patients

# Round Robin (RR) Scheduling
def rr_scheduling(patients, quantum):
    patients.sort(key=lambda x: x['arrival_time'])
    patient_queue = deque(patients)
    result = []

    while patient_queue:
        patient = patient_queue.popleft()
        if patient['treatment_time'] <= quantum:
            result.append(patient['name'])
        else:
            result.append(patient['name'])
            patient['treatment_time'] -= quantum
            patient_queue.append(patient)

    return result

# Function to calculate average waiting time
def average_waiting_time(order):
    total_waiting_time = 0
    current_time = 0

    for patient in patients:
        waiting_time = max(current_time - patient['arrival_time'], 0)
        total_waiting_time += waiting_time
        current_time = max(current_time, patient['arrival_time']) + patient['treatment_time']

    return total_waiting_time / len(patients)

# Run and evaluate each scheduling algorithm
fcfs_order = fcfs_scheduling(patients.copy())
sjf_order = sjf_scheduling(patients.copy())
ps_order = ps_scheduling(patients.copy())
rr_order = rr_scheduling(patients.copy(), quantum=10)

print("FCFS Schedule:", [p['name'] for p in fcfs_order])
print("SJF Schedule:", [p['name'] for p in sjf_order])
print("Priority Schedule:", [p['name'] for p in ps_order])
print("RR Schedule:", rr_order)