"""
Challenge: Set a Countdown Timer

Create a Python script that allows the user to set a timer in seconds. The script should:

1. Ask the user for the number of seconds to set the timer.
2. Show a live countdown in the terminal.
3. Notify the user when the timer ends with a final message and sound (if possible).

Bonus:
- Format the remaining time as MM:SS
- Use a beep sound (`\a`) at the end if the terminal supports it
- Prevent negative or non-integer inputs
"""

import time

while True:
    try: 
        seconds = int(input("enter the secionds for timer : "))
        if seconds <1:
            print("positive second de bhia 1 se bda atlest ")
            continue
        break
    except ValueError:
        print("invaliod input pleas enter an good second number")
    
print("\n Timer Started ..........")

for remaining in range(seconds , 0 , -1):
   mins, sec =  divmod(remaining , 60)
   time_format = f"{mins :02} :  {sec : 02}"
   
   print(f"Time left : {time_format} " , end = '\r')
   time.sleep(1)
   
   
print("\n Timnes up next kaam klro")   
print("\a") ## makes an beep sounds