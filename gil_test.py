import os
import sys
import threading
import time


# 1. CPU-bound task
def heavy_computation(n):
    while n > 0:
        n -= 1


def run_benchmark():
    # Number of threads to simulate
    THREAD_COUNT = os.cpu_count()

    # Total work per thread (Adjust based on CPU speed)
    WORK_PER_THREAD = 50_000_000

    print(f"--- Python Version: {sys.version.split()[0]} ---")

    # Check GIL status
    try:
        gil_status = (
            "Active (Standard)" if sys._is_gil_enabled() else "Disabled (Free-Threaded)"
        )
    except AttributeError:
        gil_status = "Active (Standard)"
    print(f"--- GIL Status: {gil_status} ---")
    print("\n")
    print(f"--- CPU Cores Available: {os.cpu_count()} ---")
    print(f"--- Simulating {THREAD_COUNT} Threads ---\n")

    # ---------------------------------------------------------
    # TEST 1: Sequential (Single Thread Logic)
    # We run the task 4 times, one after another.
    # ---------------------------------------------------------
    print("Running Sequential Test...", end="", flush=True)
    start_time = time.perf_counter()

    for _ in range(THREAD_COUNT):
        heavy_computation(WORK_PER_THREAD)

    end_time = time.perf_counter()
    seq_duration = end_time - start_time
    print(f" Done! ({seq_duration:.4f}s)")

    # ---------------------------------------------------------
    # TEST 2: Multi-Threaded (Parallel Logic)
    # We run 4 threads at the exact same time.
    # ---------------------------------------------------------
    print("Running Threaded Test...  ", end="", flush=True)
    threads = []
    for _ in range(THREAD_COUNT):
        t = threading.Thread(target=heavy_computation, args=(WORK_PER_THREAD,))
        threads.append(t)

    start_time = time.perf_counter()

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end_time = time.perf_counter()
    threaded_duration = end_time - start_time
    print(f" Done! ({threaded_duration:.4f}s)")

    # ---------------------------------------------------------
    # ANALYSIS
    # ---------------------------------------------------------
    print("\n" + "=" * 40)

    # Calculate Speedup: How many times faster was threading?
    # Perfect scaling would be roughly equal to THREAD_COUNT (4x).
    speedup = seq_duration / threaded_duration

    print(f"Speedup Factor: {speedup:.2f}x")

    if speedup > 1.5:
        print("RESULT: SUCCESS. Effective Parallelism.")
        print(f"Your code ran {speedup:.2f} times faster using threads.")
    else:
        print("RESULT: FAIL. No significant speedup.")
        print("The GIL prevented threads from running in parallel.")
    print("=" * 40)


if __name__ == "__main__":
    run_benchmark()
