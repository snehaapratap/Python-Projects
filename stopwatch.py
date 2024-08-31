import os
import time
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
 
clear_screen()
print("\n\n\n\n")
print("╔═════════════════════╗")
print("║      Stopwatch      ║")
print("╠═════════════════════╣")
print("║      00:00:00       ║")
print("╚═════════════════════╝")

start_time = time.time()
try:
    while True:
        elapsed_time = time.time() - start_time
        hours, rem = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(rem, 60)
        clear_screen()
        print("\n\n\n\n")
        print("╔════════════════════════════════════════╗")
        print("║      Stopwatch      ║     {:02.0f}:{:02.0f}:{:02.0f}     ║".format(hours, minutes, seconds))
        print("╚════════════════════════════════════════╝")
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
    clear_screen()
    print("\n\n\n\n")
    print("╔════════════════════════════════════════════╗")
    print("║      Stopwatch      ║       Stopped        ║")
    print("╚════════════════════════════════════════════╝")
