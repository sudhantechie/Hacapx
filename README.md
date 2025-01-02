# System Performance Monitoring and Analysis Tool

## Requirements

The following Python libraries are required to run the tool:

- `time`
- `dash`
- `plotly.graph_objs`
- `wmi`
- `argparse`
- `subprocess`
- `random`
- `psutil`
- `threading`
- `os`

---


Download/Installation
---------------------

* git clone https://github.com/sudhantechie/Hacapx.git
* cd hacapx
* pip install -r requirements.txt


Usage
-----

```


    ██╗  ██╗ █████╗  ██████╗ █████╗ ██████╗ ██╗  ██╗
    ██║  ██║██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗██╔╝
    ███████║███████║██║     ███████║██████╔╝ ╚███╔╝
    ██╔══██║██╔══██║██║     ██╔══██║██╔═══╝  ██╔██╗
    ██║  ██║██║  ██║╚██████╗██║  ██║██║     ██╔╝ ██╗
    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝




Project: Hacapx
Author: Sudhan
Description: System Performance Monitoring and Analysis Tool


usage: hacapx.py [-h] [--graph] [--sys-per] [--usb] [--s-duration S_DURATION] [--port PORT] [--interval INTERVAL]
                 [--sys-update] [--graphics] [--bios]

System Performance Monitor

options:
  -h, --help            show this help message and exit
  --graph               Show performance graph
  --sys-per             Show system performance metrics
  --usb                 Show USB devices
  --s-duration S_DURATION
                        Duration of the stress tests in seconds.
  --port PORT           Port number for the Dash app
  --interval INTERVAL   Graph update interval in seconds
  --sys-update          Show system updates and hotfixes
  --graphics            Show graphics information
  --bios                Show BIOS information

  ```

  Examples
  --------

  1. **Stress Testing:**
   ```
    python hacapx.py --s-duration 10
   ```
  Output:
    
    Running stress tests...
    Starting CPU stress test...
    Starting Memory stress test...
    Starting Disk stress test...
    Disk stress test completed.
    Total Bytes Written: 58.17 MB
    CPU stress test completed.
    Initial CPU Usage: 17.6%
    Final CPU Usage: 40.9%
    Memory stress test completed.
    Initial Memory Usage: 75.2%
    Final Memory Usage: 80.1%
    All stress tests completed.
    

   2. **Get Update and Hotfixes Info:**

     python hacapx.py --sys-update
     
   3. **Get Real-time metrics:**
      
     python hacapx.py --graph --interval 1 --port 80 

   5. **Displaying Help Message:**

   To see all available options and usage instructions, use the help flag:

     python hacapx.py --help

