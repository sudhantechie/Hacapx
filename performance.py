import time
from metrics import get_system_metrics
from usb import get_usb_devices
from metrics import get_bios_info

# Print system performance 
def print_system_performance():
    metrics = get_system_metrics()
    cache_hits, cache_misses, cpu_usage, memory, disk, net_sent, net_recv, \
    disk_read_speed, disk_write_speed, system_uptime, top_processes, battery_info, bus_speed, \
    disk_health, network_bandwidth, load_average = metrics

    print("\n\033[1;31m--- System Performance ---\033[0m\n")
    print(f"\033[0;32mCache Hits:\033[0m {cache_hits}")
    print(f"\033[0;32mCache Misses:\033[0m {cache_misses}")
    print(f"\033[0;32mCPU Usage:\033[0m {cpu_usage:.2f}%")
    print(f"\033[0;32mMemory Usage:\033[0m {memory:.2f}%")
    print(f"\033[0;32mDisk Usage:\033[0m {disk:.2f}%")
    print(f"\033[0;32mDisk Read Speed:\033[0m {disk_read_speed:.2f} MB/s")
    print(f"\033[0;32mDisk Write Speed:\033[0m {disk_write_speed:.2f} MB/s")
    print(f"\033[0;32mSystem Uptime:\033[0m {time.strftime('%H:%M:%S', time.gmtime(system_uptime))}")
    print(f"\033[0;32mNetwork Sent:\033[0m {net_sent} Bytes")
    print(f"\033[0;32mNetwork Received:\033[0m {net_recv} Bytes")
    print(f"\033[0;32mBattery Status:\033[0m {battery_info}")
    print(f"\033[0;32mBus Speed:\033[0m {bus_speed}")

    # Print disk health info
    print("\n\033[0;41mDisk Health:\033[0m")
    for disk, health in disk_health.items():
        print(f"\033[1;35mDisk:\033[0m {disk}")
        print(f"\033[0;32mTotal:\033[0m {health['total'] / (1024 * 1024):.2f} MB")
        print(f"\033[0;32mUsed:\033[0m {health['used'] / (1024 * 1024):.2f} MB")
        print(f"\033[0;32mFree:\033[0m {health['free'] / (1024 * 1024):.2f} MB")

    # Print network bandwidth usage
    print("\n\033[0;41mNetwork Bandwidth Usage:\033[0m\n")
    print(f"\033[0;32mBytes Sent:\033[0m {network_bandwidth['bytes_sent']}")
    print(f"\033[0;32mBytes Received:\033[0m {network_bandwidth['bytes_recv']}")

    # Print top processes
    print("\n\033[0;41mTop 6 Processes:\033[0m\n")
    for process in top_processes:
        print(f"\033[0;32mPID:\033[0m {process.info['pid']}, \033[0;32mName:\033[0m {process.info['name']}, \033[0;32mCPU Usage:\033[0m {process.info['cpu_percent']}%, \033[0;32mMemory Usage:\033[0m {process.info['memory_info'].rss / (1024 * 1024):.2f} MB")

def print_usb_devices():
    usb_devices = get_usb_devices()
    if usb_devices:
        print("\n\033[1;31m--- USB Devices ---\033[0m\n")
        for device in usb_devices:
            print(f"\033[0;32mDeviceID:\033[0m {device['DeviceID']}")
            print(f"\033[0;32mPNPDeviceID:\033[0m {device['PNPDeviceID']}")
            print(f"\033[0;32mDescription:\033[0m {device['Description']}")
            print(f"\033[0;32mManufacturer:\033[0m {device['Manufacturer']}")
            print("\033[0;35m-\033[0m" * 40)  
        print("\033[0;35m------------------\033[0m\n")
    else:
        print("\n\033[1;36m--- No USB Devices Found ---\033[0m\n")


# Print BIOS information
def print_bios_info():
    bios_info = get_bios_info()
    if bios_info:
        print("\n\033[1;31m--- BIOS Information ---\033[0m\n")
        for key, value in bios_info.items():
            print(f"{key}: {value}")
    else:
        print("\n\033[1;36m--- BIOS Information Not Available ---\033[0m\n")

