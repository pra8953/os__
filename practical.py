# 4 wala

import os  # File and directory handling ke liye
import stat  # File permissions ke liye
import time  # Time conversion ke liye


def print_file_lekhka_jokha(file_name):
    # File ki details (like size, permissions, timestamps) lene ke liye
    file_details = os.stat(file_name)
    # File ke permissions ko human-readable format main convert karte hain
    file_permission = stat.filemode(file_details.st_mode)
    # File ka last access time human-readable banate hain
    file_acces_time = time.ctime(file_details.st_atime)

    # File ki sari details print karte hain
    print(file_details)
    print(file_permission)
    print(file_acces_time)


# Example call
print_file_lekhka_jokha("example.txt")


# 5 wala


import os  # File handling ke liye


def copy_file(source, destination):
    # Source file ko read mode main open karte hain
    with open(source, "rb") as src:
        # Destination file ko write mode main open karte hain
        with open(destination, "wb") as dest:
            while True:
                # Source file se chunk (1 KB) read karte hain
                chunk = os.read(src.fileno(), 1024)
                if not chunk:  # Agar data khatam ho gaya
                    break
                # Destination file main write karte hain
                os.write(dest.fileno(), chunk)


# Example call
copy_file("example.html", "destination.txt")


# 6 wala


def fcfs(processes, arrival, burst):
    n = len(processes)  # Number of processes
    completion = [0] * n  # Completion time list
    turnaround = [0] * n  # Turnaround time list
    waiting = [0] * n  # Waiting time list

    # Completion time calculate karte hain
    completion[0] = (
        arrival[0] + burst[0]
    )  # Pehla process complete hota hai arrival + burst time par
    for i in range(1, n):
        completion[i] = max(completion[i - 1], arrival[i]) + burst[i]

    # Turnaround aur Waiting time calculate karte hain
    for i in range(n):
        turnaround[i] = completion[i] - arrival[i]
        waiting[i] = turnaround[i] - burst[i]

    # Print karte hain process details
    print("P\tAT\tBT\tCT\tTAT\tWT")
    for i in range(n):
        print(
            f"{processes[i]}\t{arrival[i]}\t{burst[i]}\t{completion[i]}\t{turnaround[i]}\t{waiting[i]}"
        )


# Example call
fcfs(["P1", "P2", "P3"], [0, 2, 4], [5, 3, 2])


# 8 wala


def sjf(processes, arrival, burst):
    n = len(processes)  # Number of processes
    completed = [False] * n  # Kis process ka kaam ho chuka hai
    completion = [0] * n  # Completion time
    turnaround = [0] * n  # Turnaround time
    waiting = [0] * n  # Waiting time

    time = 0  # Current time
    done = 0  # Completed processes count

    while done < n:
        shortest = -1  # Sabse chhota job dhoondhne ke liye
        min_burst = float("inf")

        # Har process check karte hain
        for i in range(n):
            if arrival[i] <= time and not completed[i] and burst[i] < min_burst:
                min_burst = burst[i]
                shortest = i

        if shortest == -1:  # Agar koi process ready nahi hai
            time += 1
        else:  # Process execute karte hain
            time += burst[shortest]
            completion[shortest] = time
            turnaround[shortest] = completion[shortest] - arrival[shortest]
            waiting[shortest] = turnaround[shortest] - burst[shortest]
            completed[shortest] = True
            done += 1

    print("P\tAT\tBT\tCT\tTAT\tWT")
    for i in range(n):
        print(
            f"{processes[i]}\t{arrival[i]}\t{burst[i]}\t{completion[i]}\t{turnaround[i]}\t{waiting[i]}"
        )


# Example call
sjf(["P1", "P2", "P3"], [0, 1, 3], [7, 4, 1])


# 9 wala


def priority_scheduling(processes, arrival, burst, priority):
    n = len(processes)
    completed = [False] * n  # Kis process ka kaam ho chuka hai
    completion = [0] * n
    turnaround = [0] * n
    waiting = [0] * n

    time = 0
    done = 0

    while done < n:
        highest_priority = -1  # Sabse high priority job dhoondhne ke liye
        for i in range(n):
            if arrival[i] <= time and not completed[i]:
                if highest_priority == -1 or priority[i] < priority[highest_priority]:
                    highest_priority = i

        if highest_priority == -1:  # Agar koi process ready nahi hai
            time += 1
        else:
            time += burst[highest_priority]
            completion[highest_priority] = time
            turnaround[highest_priority] = (
                completion[highest_priority] - arrival[highest_priority]
            )
            waiting[highest_priority] = (
                turnaround[highest_priority] - burst[highest_priority]
            )
            completed[highest_priority] = True
            done += 1

    print("P\tAT\tBT\tPR\tCT\tTAT\tWT")
    for i in range(n):
        print(
            f"{processes[i]}\t{arrival[i]}\t{burst[i]}\t{priority[i]}\t{completion[i]}\t{turnaround[i]}\t{waiting[i]}"
        )


# Example call
priority_scheduling(["P1", "P2", "P3"], [0, 1, 2], [3, 4, 2], [1, 3, 2])


# 10 wala


def srjf(processes, arrival, burst):
    n = len(processes)
    remaining = burst[:]  # Remaining burst time track karte hain
    completion = [0] * n
    turnaround = [0] * n
    waiting = [0] * n

    time = 0  # Current time
    done = 0  # Completed processes count

    while done < n:
        shortest = -1  # Sabse chhota remaining job dhoondhne ke liye
        for i in range(n):
            if arrival[i] <= time and remaining[i] > 0:
                if shortest == -1 or remaining[i] < remaining[shortest]:
                    shortest = i

        if shortest == -1:  # Agar koi process ready nahi hai
            time += 1
        else:
            remaining[shortest] -= 1  # Ek unit execute karte hain
            time += 1
            if remaining[shortest] == 0:  # Agar process khatam ho gaya
                completion[shortest] = time
                turnaround[shortest] = completion[shortest] - arrival[shortest]
                waiting[shortest] = turnaround[shortest] - burst[shortest]
                done += 1

    print("P\tAT\tBT\tCT\tTAT\tWT")
    for i in range(n):
        print(
            f"{processes[i]}\t{arrival[i]}\t{burst[i]}\t{completion[i]}\t{turnaround[i]}\t{waiting[i]}"
        )


# Example call
srjf(["P1", "P2", "P3"], [0, 2, 4], [6, 8, 2])
