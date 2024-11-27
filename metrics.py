import time
import psutil
import random
import wmi

# Initialize WMI interface for Windows
wmi_interface = wmi.WMI()

# Function to get system metrics
def get_system_metrics():
    try:
        # Real data with some random fluctuation added for testing
        cache_hits = psutil.disk_io_counters().read_count + random.randint(-5, 5)
        cache_misses = psutil.disk_io_counters().write_count + random.randint(-5, 5)

        cpu_usage = psutil.cpu_percent(interval=None) + random.uniform(-1, 1)
        memory_info = psutil.virtual_memory().percent + random.uniform(-1, 1)
        disk_usage = psutil.disk_usage('/').percent + random.uniform(-1, 1)

        net_io = psutil.net_io_counters()
        network_sent = net_io.bytes_sent + random.randint(-1000, 1000)
        network_recv = net_io.bytes_recv + random.randint(-1000, 1000)

        # Disk I/O statistics
        disk_read_speed = psutil.disk_io_counters().read_bytes / (1024 * 1024)  # MB/s
        disk_write_speed = psutil.disk_io_counters().write_bytes / (1024 * 1024)  # MB/s

        # System uptime
        system_uptime = time.time() - psutil.boot_time()

        # Top processes by CPU usage (top 6)
        top_processes = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']),
                                key=lambda p: p.info['cpu_percent'], reverse=True)[:6]

        # Battery status 
        battery_status = psutil.sensors_battery()
        battery_info = f"\033[0;32mBattery Percentage:\033[0m {battery_status.percent}%, \033[0;32mPlugged In:\033[0m {battery_status.power_plugged}" if battery_status else "N/A"

        # Get the bus speed using WMI
        def get_bus_speed():
            try:
                query = "SELECT Speed FROM Win32_PhysicalMemory"
                results = wmi_interface.query(query)
                
                if results:
                    return f"{results[0].Speed} MHz"
                else:
                    return "Unknown"
            except Exception as e:
                print(f"\033[1;36mError getting bus speed:\033[0m {e}")
                return "Unknown"

        bus_speed = get_bus_speed()

        # Additional metrics
        disk_health = get_disk_health()
        network_bandwidth = get_network_bandwidth()
        load_average = get_load_average()

        return (cache_hits, cache_misses, cpu_usage, memory_info, disk_usage, network_sent, network_recv,
                disk_read_speed, disk_write_speed, system_uptime, top_processes, battery_info, bus_speed,
                disk_health, network_bandwidth, load_average)
    except Exception as e:
        print(f"\033[1;36mError accessing system metrics:\033[0m {e}")
        return (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], "N/A", "Unknown", {}, {}, {}, (0, 0, 0))  # Return zeros if there is an error

# Function to get disk health (example, may need adjustment based on system)
def get_disk_health():
    try:
        disk_health = {}
        for disk in psutil.disk_partitions():
            usage = psutil.disk_usage(disk.mountpoint)
            disk_health[disk.device] = {
                'total': usage.total,
                'used': usage.used,
                'free': usage.free
            }
        return disk_health
    except Exception as e:
        print(f"\033[1;36mError accessing disk health:\033[0m {e}")
        return {}

# Function to get network bandwidth usage
def get_network_bandwidth():
    try:
        net_io = psutil.net_io_counters()
        return {
            "bytes_sent": net_io.bytes_sent,
            "bytes_recv": net_io.bytes_recv
        }
    except Exception as e:
        print(f"\033[1;36mError accessing network bandwidth:\033[0m {e}")
        return {"bytes_sent": 0, "bytes_recv": 0}

# Function to get system load average
def get_load_average():
    try:
        load = psutil.getloadavg()
        return load
    except Exception as e:
        print(f"\033[1;36mError accessing load average:\033[0m {e}")
        return (0, 0, 0)

# Function to get BIOS information 
def get_bios_info():
    try:
        wmi_interface = wmi.WMI()
        bios_info = wmi_interface.Win32_BIOS()[0]
        
        bios_details = {
            '\033[0;32mManufacturer\033[0m': bios_info.Manufacturer,
            '\033[0;32mVersion\033[0m': bios_info.Version,
            '\033[0;32mReleaseDate\033[0m': bios_info.ReleaseDate,
            '\033[0;32mSMBIOSVersion\033[0m': bios_info.SMBIOSBIOSVersion
        }
        
        return bios_details
    except Exception as e:
        print(f"\033[1;36mError accessing BIOS information:\033[0m {e}")
        return {}
