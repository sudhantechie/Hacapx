import wmi

def get_hotfixes_info():
    # Initialize WMI interface
    wmi_interface = wmi.WMI()
    
    try:
        # Query for installed hotfixes
        hotfixes_info = []
        for hotfix in wmi_interface.Win32_QuickFixEngineering():
            hotfixes_info.append({
                'HotFixID': hotfix.HotFixID,
                'Description': hotfix.Description,
                'InstalledOn': hotfix.InstalledOn,
                'Status': hotfix.Status
            })
        
        return hotfixes_info
    except Exception as e:
        print(f"\033[1;36mError accessing hotfix information:\033[0m {e}")
        return []

def get_windows_updates_info():
    wmi_interface = wmi.WMI()
    
    try:
        # Query for installed Windows updates
        updates_info = []
        for update in wmi_interface.Win32_QuickFixEngineering():
            updates_info.append({
                'UpdateID': update.HotFixID,
                'Description': update.Description,
                'InstalledOn': update.InstalledOn
            })
        
        return updates_info
    except Exception as e:
        print(f"\033[1;36mError accessing update information:\033[0m {e}")
        return []

if __name__ == "__main__":
    print("\033[1;31m--- Hotfixes Information ---\033[0m\n")
    hotfixes_info = get_hotfixes_info()
    if hotfixes_info:
        for info in hotfixes_info:
            print(f"\033[0;32mHotFix ID:\033[0m {info['HotFixID']}")
            print(f"\033[0;32mDescription:\033[0m {info['Description']}")
            print(f"\033[0;32mInstalled On:\033[0m {info['InstalledOn']}")
            print(f"\033[0;32mStatus:\033[0m {info['Status']}")
            print("\033[0;35m-\033[0m" * 40,"\n")
    else:
        print("No hotfix information found.")

    print("\033[0;31m--- Windows Updates Information ---\033[0m\n")
    updates_info = get_windows_updates_info()
    if updates_info:
        for info in updates_info:
            print(f"\033[0;32mUpdate ID:\033[0m {info['UpdateID']}")
            print(f"\033[0;32mDescription:\033[0m {info['Description']}")
            print(f"\033[0;32mInstalled On:\033[0m {info['InstalledOn']}")
            print("\033[0;35m-\033[0m" * 40)
    else:
        print("No update information found.")
