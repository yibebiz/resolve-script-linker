
import os
import sys
import subprocess
import platform
from pathlib import Path

# To create symbolic link to the default davinci resolve composition script folder from the directory of this script, 
# you can just run this python code as Administrator. IT IS IMPORTANT YOU RUN THIS CODE AS ADMINISTRATOR. 

 # Detect platform
system = platform.system()
user_home = Path.home()

#Windows
if system == "Windows":
    #resolve_script_dir = r"C:\Users\username\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Comp"
    resolve_script_dir = user_home / "AppData" / "Roaming" / "Blackmagic Design" / "DaVinci Resolve" / "Support" / "Fusion" / "Scripts" / "Comp"
#Linux
elif system in ["Linux"]:
    #resolve_script_dir = "/home/yourname/.local/share/DaVinciResolve/Fusion/Scripts/Comp"
    fusion_scripts_path = user_home / ".local" / "share" / "DaVinciResolve" / "Fusion" / "Scripts" / "Comp"

#macOS
elif system in ["Darwin"]:
    #resolve_script_dir = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Comp"
    resolve_script_dir = user_home / "Library" / "Application Support" / "Blackmagic Design" / "DaVinci Resolve" / "Fusion" / "Scripts" / "Comp"

else:
    raise RuntimeError(f"Unsupported platform: {system}")

if not os.path.exists(resolve_script_dir):
    print(f"\nThe follwoing is not valid path: \n\t{resolve_script_dir}\nPerhaps try creating symbolic link manually.\n")
    exit(1)


script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
linked_dir = os.path.join(resolve_script_dir, os.path.basename(script_dir))

if os.path.exists(linked_dir):
    print(f"\nSymbolic link between '{script_dir}' and '{linked_dir}' already created. No change was made\n")
    exit(1)


command = f'mklink /D "{linked_dir}" "{script_dir}"'

# Run as shell command (must be run as administrator)
result = subprocess.run(command, shell=True)

if  result.returncode == 0:
    print(f"\n✅ Symbolic link completed successfully!\n")
else: 
    print(f"\n❌Something went wrong. Make sure you run the script with Administrator privilege.")
    