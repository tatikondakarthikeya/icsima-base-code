import psutil

TARGET = "AcquireData.py"
found = False

for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
    try:
        # Check if the target script name appears in the command line
        if proc.info['cmdline'] and any(TARGET in part for part in proc.info['cmdline']):
            print(f"{TARGET} is running with PID {proc.info['pid']}")
            found = True
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

if not found:
    print(f"{TARGET} is NOT running")
