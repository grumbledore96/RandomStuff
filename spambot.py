import pyautogui, time, keyboard
time.sleep(5)
#x= "https://youtu.be/dQw4w9WgXcQ" #rick roll
#x= "haachamachama~"#"はあちゃまちゃま"
#x = "https://youtu.be/wXMD6wmcwvE" # better jungler wins
x = "https://www.youtube.com/watch?v=935OINm1ssk&list=PLZtz1DzziwHKByddau4O4xPo8HUED-bYH"
print("Time to go")
#x = "https://cdn.discordapp.com/attachments/346016213110882306/675439318873014292/unknown.png\n https://cdn.discordapp.com/attachments/346016213110882306/675439329513832450/unknown.png\n https://cdn.discordapp.com/attachments/346016213110882306/675439347885015050/unknown.png"
while True:
    pyautogui.typewrite(x)
    pyautogui.press("enter")
    #pyautogui.press("enter")
    if keyboard.is_pressed('q'):
        break
    time.sleep(0.4)
