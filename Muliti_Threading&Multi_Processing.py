import threading
import time

# Function to be executed by each thread
def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)

# Creating two threads that will run the print_numbers function
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

# Starting both threads
thread1.start()
thread2.start()

# Joining the threads (waits for them to finish before continuing)
thread1.join()
thread2.join()

print("Both threads have finished execution.")