import argparse
import subprocess

def print_logo_and_author():
    logo = """
\033[1;31m
    ██╗  ██╗ █████╗  ██████╗ █████╗ ██████╗ ██╗  ██╗
    ██║  ██║██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗██╔╝
    ███████║███████║██║     ███████║██████╔╝ ╚███╔╝ 
    ██╔══██║██╔══██║██║     ██╔══██║██╔═══╝  ██╔██╗ 
    ██║  ██║██║  ██║╚██████╗██║  ██║██║     ██╔╝ ██╗
    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝
\033[0m
    """
    project_info = """
\033[1;34m
\033[0;36mProject:\033[0m \033[1;31mHacapx\033[0m
\033[0;36mAuthor:\033[0m \033[1;32mSudhan\033[0m
\033[0;36mDescription:\033[0m \033[1;35mSystem Performance Monitoring and Analysis Tool
\033[0m
    """
    print(logo)
    print(project_info)

# Print logo and author information
print_logo_and_author()

# Command-line argument parsing
parser = argparse.ArgumentParser(description='\033[1;32mSystem Performance Monitor\033[0m \033[1;31m')
parser.add_argument('--graph', action='store_true', help='Show performance graph')
parser.add_argument('--sys-per', action='store_true', help='Show system performance metrics')
parser.add_argument('--usb', action='store_true', help='Show USB devices')
parser.add_argument('--s-duration', type=int, help='Duration of the stress tests in seconds.')
parser.add_argument('--port', type=int, default=6009, help='Port number for the Dash app')
parser.add_argument('--interval', type=int, default=1, help='Graph update interval in seconds')
parser.add_argument('--sys-update', action='store_true', help='Show system updates and hotfixes')
parser.add_argument('--graphics', action='store_true', help='Show graphics information')
parser.add_argument('--bios', action='store_true', help='Show BIOS information\033[0m')

args = parser.parse_args()
if args.graph:
    from dsh import create_dash_app
    app = create_dash_app(port=args.port, interval=args.interval)
    app.run_server(port=args.port)

elif args.sys_per:
    from performance import print_system_performance
    print_system_performance()

elif args.usb:
    from performance import print_usb_devices
    print_usb_devices()

elif args.s_duration is not None:
    # Run stress test for specified duration
    subprocess.run(['python', 'stress_test.py', '--s-duration', str(args.s_duration)])

elif args.sys_update:
    # Run system updates and hotfixes information retrieval
    subprocess.run(['python', 'update_info.py'])

elif args.graphics:
    # Run graphics information retrieval
    subprocess.run(['python', 'grap_info.py'])

elif args.bios:
     # Run BIOS information retrieval
    from performance import print_bios_info
    print_bios_info()

else:
    print("No valid arguments provided. Use --help for options.")
