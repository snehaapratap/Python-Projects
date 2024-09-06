import os
import time
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
sin = int(input("Enter the countdown time in seconds: "))
while sin >= 0:
    clear_screen()
    minutes, secs = divmod(sin, 60)
    print("\n\n\n\n")
    print("╔═════════════════════╗")
    print("║      Countdown      ║")
    print("╠═════════════════════╣")
    print("║        {:02d}:{:02d}        ║".format(minutes, secs))
    print("╚═════════════════════╝")

    time.sleep(1)
    sin -= 1

clear_screen()
print("\n\n\n\n")
print("╔═════════════════════╗")
print("║      Countdown      ║")
print("╠═════════════════════╣")
print("║      Time's Up!     ║")
print("╚═════════════════════╝")


