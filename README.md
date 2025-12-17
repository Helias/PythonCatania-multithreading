# PythonCatania-multithreading

Demo project showcasing Python's multithreading, multiprocessing, and the experimental GIL-free Python 3.14t build.

📍 [Event](https://www.meetup.com/python-catania/events/312066711/)  
📄 [Slides](https://slides.com/stefanoborzi/code-e7d3ed/fullscreen#/1), [download](https://github.com/Helias/PythonCatania-multithreading/blob/main/multithreading.pdf)

## Overview

This repository contains practical examples demonstrating:

- **GIL (Global Interpreter Lock) behavior**: Understanding the limitations of Python's threading model
- **Free-threaded Python 3.14t**: Testing the experimental nogil build for true parallelism
- **Multiprocessing with Pathos**: Achieving parallel execution with multiple processes
- **Progress tracking with tqdm**: Monitoring long-running tasks

## Install requirements

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.14t python3.14-nogil python3.14-venv
python3.14t -m venv venv
source ./venv/bin/activate
pip install pathos tqdm
```

## Examples

### 1. `tqdm.py` - Basic Progress Bar

A simple demonstration of `tqdm` for tracking progress in sequential loops.

```bash
python tqdm.py
```

**What it does**: Iterates through 100 items with a 1-second sleep, displaying a progress bar.

### 2. `pathos.py` - Parallel Processing with Progress Bar

Combines `pathos` multiprocessing with `tqdm` for parallel execution with visual feedback.

```bash
python pathos.py
```

**What it does**:

- Uses `pathos.multiprocessing.ProcessingPool` to distribute work across CPU cores
- Processes 100 items in parallel (1-second sleep each)
- Shows real-time progress with `tqdm`
- **Expected speedup**: ~N×, where N is the number of CPU cores

### 3. `gil_test.py` - GIL Benchmark

A comprehensive benchmark comparing sequential vs. threaded execution to demonstrate the impact of the GIL.

```bash
python gil_test.py
```

**What it does**:

- Detects Python version and GIL status (standard vs. free-threaded)
- Runs CPU-bound computations (50M iterations per thread)
- Compares sequential execution vs. 22 threads
- Calculates speedup factor

**Expected results**:

- **Standard Python**: ~1x speedup (threads compete for GIL)
- **Python 3.14t (nogil)**: Significant speedup (true parallel execution)

## Understanding the GIL

The Global Interpreter Lock (GIL) is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecode simultaneously. This means:

- ✅ **Threading works well for**: I/O-bound tasks (network requests, file operations)
- ❌ **Threading is limited for**: CPU-bound tasks (computation-heavy operations)

Python 3.14t introduces an experimental **free-threaded** build that removes the GIL, enabling true parallel execution of Python threads.

## Key Differences

| Approach                  | Use Case        | Overhead                  | GIL Impact                     |
| ------------------------- | --------------- | ------------------------- | ------------------------------ |
| **Threading**             | I/O-bound tasks | Low                       | Limited by GIL                 |
| **Multiprocessing**       | CPU-bound tasks | Higher (process creation) | No GIL (separate interpreters) |
| **Free-threaded (3.14t)** | CPU-bound tasks | Low                       | No GIL                         |
