import os
import sys
import platform
import subprocess

def install_deps():
    print("[*] Installing dependency: rich...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rich"])

def setup_windows(script_path):
    # Creates shapeshift.bat in the User Profile folder
    batch_path = os.path.join(os.environ['USERPROFILE'], 'shapeshift.bat')
    with open(batch_path, 'w') as f:
        f.write(f'@echo off\npython "{script_path}" %*')
    
    print(f"\n[+] Windows shortcut created: {batch_path}")
    print("[!] Ensure your User folder is in the system PATH.")

def setup_linux(script_path):
    # Creates a symbolic link in /usr/local/bin
    target = "/usr/local/bin/shapeshift"
    try:
        with open(target, 'w') as f:
            f.write(f'#!/bin/bash\npython3 "{script_path}" "$@"')
        os.chmod(target, 0o755)
        print(f"\n[+] Linux binary created: {target}")
    except PermissionError:
        print("[!] Error: Run with sudo (sudo python3 install.py)")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    main_file = os.path.join(current_dir, "Shapeshift.py")
    
    install_deps()
    
    if platform.system() == "Windows":
        setup_windows(main_file)
    else:
        setup_linux(main_file)
    
    print("\n[✔] Installation complete! Try running 'shapeshift' in a new terminal.")