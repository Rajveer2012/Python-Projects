while True:
    print('\n')
    print("✨ Welcome to the Password Combination Percentage Calculator! ✨")
    print("This program calculates the probability of your chosen password among all possible combinations for a given length.")
    print('\n')
    l = "Please enter the number of digits in your password (Choose between 4 and 8): "
    digits = str(input(l))
    n = "Now, enter your password (digits only): "
    password = str(input(n))
    if not digits.isdigit() or not password.isdigit() or len(password) != int(digits) or int(digits) > 8 or int(digits) < 4:
        print("❌ Invalid input: Ensure your password length matches the number of digits entered, and is between 4 and 8.")
        print("Exiting the program. Please try again.")
        exit()
    digits = int(digits)
    password_digits = [int(x) for x in password]
    if digits == 4:
        number = 0
        number2 = 0
        for i in range(0, 11):
            for j in range(0, 11):
                for k in range(0, 11): 
                    for m in range(0, 11):
                        number += 1
                        if number % 1000000 == 0:
                            print(f"🔢 Calculating... Total combinations checked for a {digits}-digit password: {number}")              
                        if (i == password_digits[0] and j == password_digits[1] and k == password_digits[2] and m == password_digits[3]):    
                            number2 += 1
        print(f"🎯 The probability of your password among all possible {digits}-digit combinations is: {(number2 / (11 ** digits)) * 100:.2f}%")
        break
    if digits == 5:
        number = 0
        number2 = 0
        for i in range(0, 11):
            for j in range(0, 11):
                for k in range(0, 11): 
                    for m in range(0, 11):
                        for z in range(0, 11):
                            number += 1
                            if number % 1000000 == 0:
                                print(f"🔢 Calculating... Total combinations checked for a {digits}-digit password: {number}")              
                            if (i == password_digits[0] and j == password_digits[1] and k == password_digits[2] and m == password_digits[3] and z == password_digits[4]):    
                                number2 += 1
        print(f"🎯 The probability of your password among all possible {digits}-digit combinations is: {(number2 / (11 ** digits)) * 100:.2f}%")
        break
    if digits == 6:
        number = 0
        number2 = 0
        for i in range(0, 11):
            for j in range(0, 11):
                for k in range(0, 11): 
                    for m in range(0, 11):
                        for z in range(0, 11):
                            for y in range(0, 11):
                                number += 1
                                if number % 1000000 == 0:
                                    print(f"🔢 Calculating... Total combinations checked for a {digits}-digit password: {number}")              
                                if (i == password_digits[0] and j == password_digits[1] and k == password_digits[2] and m == password_digits[3] and z == password_digits[4] and y == password_digits[5]):    
                                    number2 += 1
        print(f"🎯 The probability of your password among all possible {digits}-digit combinations is: {(number2 / (11 ** digits)) * 100:.2f}%")
        break
    if digits == 7:
        number = 0
        number2 = 0
        for i in range(0, 11):
            for j in range(0, 11):
                for k in range(0, 11): 
                    for m in range(0, 11):
                        for z in range(0, 11):
                            for y in range(0, 11):
                                for b in range(0, 11):
                                    number += 1
                                    if number % 1000000 == 0:
                                        print(f"🔢 Calculating... Total combinations checked for a {digits}-digit password: {number}")              
                                    if (i == password_digits[0] and j == password_digits[1] and k == password_digits[2] and m == password_digits[3] and z == password_digits[4] and y == password_digits[5] and b == password_digits[6]):    
                                        number2 += 1
        print(f"🎯 The probability of your password among all possible {digits}-digit combinations is: {(number2 / (11 ** digits)) * 100:.2f}%")
        break
    if digits == 8:
        number = 0
        number2 = 0
        for i in range(0, 11):
            for j in range(0, 11):
                for k in range(0, 11): 
                    for m in range(0, 11):
                        for z in range(0, 11):
                            for y in range(0, 11):
                                for b in range(0, 11):
                                    for a in range(0, 11):
                                        number += 1
                                        if number % 1000000 == 0:
                                            print(f"🔢 Calculating... Total combinations checked for a {digits}-digit password: {number}")              
                                        if (i == password_digits[0] and j == password_digits[1] and k == password_digits[2] and m == password_digits[3] and z == password_digits[4] and y == password_digits[5] and b == password_digits[6] and a == password_digits[7]):    
                                            number2 += 1
        print(f"🎯 The probability of your password among all possible {digits}-digit combinations is: {(number2 / (11 ** digits)) * 100:.2f}%")
        break





