originalMoney = 107.80
birthdayMoney = 390.00
userInput = " "
while (userInput) != "stop":
    userInput = input("o for original, b for birthday")
    while userInput == "o":
        userInput = input("How much to take away from original money")
        originalMoney-=float(userInput)
    while userInput =="b":
        userInput = input("How much to take away from birthday money")
        birthdayMoney-=(userInput)
        print(birthdayMoney)
