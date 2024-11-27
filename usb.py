import wmi

# Initialize WMI 
wmi_interface = wmi.WMI()

# Function to get USB devices information
def get_usb_devices():
    try:
        usb_devices = []
        for usb in wmi_interface.Win32_PnPEntity():
            if 'USB' in usb.DeviceID:
                device_info = {
                    'DeviceID': usb.DeviceID,
                    'PNPDeviceID': usb.PNPDeviceID,
                    'Description': usb.Description,
                    'Manufacturer': usb.Manufacturer if usb.Manufacturer else 'Unknown'
                }
                usb_devices.append(device_info)
        return usb_devices
    except Exception as e:
        print(f"\033[0;36mError accessing USB devices:\033[0m {e}")
        return []
