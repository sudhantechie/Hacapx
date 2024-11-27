import wmi

def get_graphics_info():
    # Initialize WMI interface for Windows
    wmi_interface = wmi.WMI()
    
    try:
        # Query for graphics information
        graphics_info = []
        for video_controller in wmi_interface.Win32_VideoController():
            graphics_info.append({
                'Name': video_controller.Name,
                'AdapterRAM': video_controller.AdapterRAM / (1024 * 1024),  # Convert bytes to MB
                'DriverVersion': video_controller.DriverVersion,
                'VideoModeDescription': video_controller.VideoModeDescription,
                'DeviceID': video_controller.DeviceID,
                'PNPDeviceID': video_controller.PNPDeviceID,
                'Status': video_controller.Status,
                'Caption': video_controller.Caption,
                'CurrentHorizontalResolution': video_controller.CurrentHorizontalResolution,
                'CurrentVerticalResolution': video_controller.CurrentVerticalResolution,
                'VideoProcessor': video_controller.VideoProcessor
            })
        
        return graphics_info
    except Exception as e:
        print(f"Error accessing graphics information: {e}")
        return []

if __name__ == "__main__":
    graphics_info = get_graphics_info()
    if graphics_info:
        print("\033[1;31m--- Graphics Information ---\033[0;35m\n")
        for info in graphics_info:
            print(f"\033[0;32mName:\033[0m {info['Name']}")
            print(f"\033[0;32mAdapter RAM:\033[0m {info['AdapterRAM']:.2f} MB")
            print(f"\033[0;32mDriver Version:\033[0m {info['DriverVersion']}")
            print(f"\033[0;32mVideo Mode Description:\033[0m {info['VideoModeDescription']}")
            print(f"\033[0;32mDevice ID:\033[0m {info['DeviceID']}")
            print(f"\033[0;32mPNP Device ID:\033[0m {info['PNPDeviceID']}")
            print(f"\033[0;32mStatus:\033[0m {info['Status']}")
            print(f"\033[0;32mCaption:\033[0m {info['Caption']}")
            print(f"\033[0;32mCurrent Horizontal Resolution:\033[0m {info['CurrentHorizontalResolution']}")
            print(f"\033[0;32mCurrent Vertical Resolution:\033[0m {info['CurrentVerticalResolution']}")
            print(f"\033[0;32mVideo Processor:\033[0m {info['VideoProcessor']}")
            print("\033[0;35m-\033[0m" * 40)
    else:
        print("No graphics information found.")
