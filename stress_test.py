import time
import threading
import psutil
import random
import os

# Function to stress test CPU
def stress_cpu(duration):
    print("\033[0;32mStarting CPU stress test...\033[0m")
    start_time = time.time()
    initial_cpu_usage = psutil.cpu_percent(interval=1)
    while time.time() - start_time < duration:
        # Use multiple threads to increase CPU load
        threads = []
        for _ in range(psutil.cpu_count()):
            thread = threading.Thread(target=lambda: [x**2 for x in range(10000000)])
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
    final_cpu_usage = psutil.cpu_percent(interval=1)
    print("\033[0;32mCPU stress test completed.\033[0m")
    print(f"\033[0;32mInitial CPU Usage:\033[0m {initial_cpu_usage}%")
    print(f"\033[0;32mFinal CPU Usage:\033[0m {final_cpu_usage}%")

# Function to stress test memory
def stress_memory(duration):
    print("\033[0;32mStarting Memory stress test...\033[0m")
    start_time = time.time()
    initial_memory_info = psutil.virtual_memory()
    memory_list = []
    while time.time() - start_time < duration:
        memory_list.append([random.random() for _ in range(10**7)])
    final_memory_info = psutil.virtual_memory()
    print("\033[0;32mMemory stress test completed.\033[0m")
    print(f"\033[0;32mInitial Memory Usage:\033[0m {initial_memory_info.percent}%")
    print(f"\033[0;32mFinal Memory Usage:\033[0m {final_memory_info.percent}%")

# Function to stress test disk
def stress_disk(duration):
    print("\033[0;32mStarting Disk stress test...\033[0m")
    start_time = time.time()
    temp_file = 'temp_stress_test_file.dat'
    bytes_written = 0
    with open(temp_file, 'wb') as f:
        while time.time() - start_time < duration:
            data = random.randbytes(10**6)
            f.write(data)
            bytes_written += len(data)
    print("\033[0;32mDisk stress test completed.\033[0m")
    os.remove(temp_file)  
    print(f"\033[0;32mTotal Bytes Written:\033[0m {bytes_written / (1024 * 1024):.2f} MB")

# Run all stress tests
def run_stress_tests(duration):
    print("\033[0;32mRunning stress tests...\033[0m")
    stress_threads = []
    stress_threads.append(threading.Thread(target=stress_cpu, args=(duration,)))
    stress_threads.append(threading.Thread(target=stress_memory, args=(duration,)))
    stress_threads.append(threading.Thread(target=stress_disk, args=(duration,)))
    
    for thread in stress_threads:
        thread.start()
    for thread in stress_threads:
        thread.join()
    print("\033[0;32mAll stress tests completed.\033[0m")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Run stress tests for CPU, memory, and disk.')
    parser.add_argument('--s-duration', type=int, required=True, help='Duration of the stress tests in seconds.')
    args = parser.parse_args()
    
    run_stress_tests(args.s_duration)
