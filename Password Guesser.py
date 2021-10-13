import random
import pyautogui


chars = "1234567890"
chars_list = list(chars)

password = pyautogui.password("Enter a pin code: ")

guess_password = ""

number = 0


while(guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))

    number +=1
    print("<========================" + str(guess_password) + "========================>")

    if(guess_password == list(password)):
        print("Your pin code is: " + "".join(guess_password))
        
        break

print(f"The number of tries is {number}")
