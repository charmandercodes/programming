import threading
import time

# Daemon threads run in the background and will automatically stop when the main program exits.
# This example uses a daemon thread to continuously read from a file every 3 seconds.

path = "daemon.txt"
text = ""

def read_file():
    global path, text
    while True:
        try:
            with open(path, "r") as file:
                text = file.read()
        except IOError as e:
            print(f"Error reading file: {e}")
        time.sleep(3)

def print_text():
    for _ in range(30):
        print(text)
        time.sleep(1)

# Create a daemon thread for reading the file
file_thread = threading.Thread(target=read_file, daemon=True)
print_thread = threading.Thread(target=print_text)

file_thread.start()
print_thread.start()

print_thread.join()  # Optionally wait for the non-daemon thread to finish
