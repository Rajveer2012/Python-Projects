while True:
    print('\n')
    print("✨ Welcome to the Password Combination Percentage Calculator! ✨")
    print("This program calculates the probability of your chosen password among all possible combinations for a given length.")
    print('\n')
    l = "Please enter the number of digits in your password (Choose between 4 and 8), or enter a word to use its length as the number of digits:\n (Note: Enter a 4 to 8 letter Word and It Should be a single word, no spaces, no punctuation, and no numbers👍👍): "
    digits_input = input(l).strip()
    if digits_input.isdigit():
        digits = int(digits_input)
    elif digits_input.isalpha():
        digits = len(digits_input)
        print(f"\n🔢 Using the length of the word '{digits_input} the number of digits is: {digits}\n")
    else:
        print("\n❌ Invalid input: Please enter either a single digit (4-8) or a word (length 4-8).\nRestarting the program. Please try again.")
        continue
    if not (4 <= digits <= 8):
        print("\n❌ Invalid input: Number of digits must be between 4 and 8.\nRestarting the program. Please try again.")
        continue
    n = "Now, enter your password (digits only): "
    password = input(n).strip()
    if not password.isdigit() or len(password) != digits:
        print("\n❌ Invalid input: Ensure your password contains only digits, has no spaces, and its length matches the number of digits entered (between 4 and 8). Example: 0505 is valid for 4 digits.\nRestarting the program. Please try again.")
        continue
    digits = int(digits)
    password_digits = [int(x) for x in password]
    if digits == 4:
        number = 0
        number2 = 0
        total = 11 ** 4
        for i in range(0, 11):
            for j in range(0, 11):
                for k in range(0, 11): 
                    for m in range(0, 11):
                        number += 1
                        # Only print at the end
                        if number == total:
                            print(f"\n🔢 Calculating... Total combinations checked for a {digits}-digit password: {number}")
                        if (i == password_digits[0] and j == password_digits[1] and k == password_digits[2] and m == password_digits[3]):    
                            number2 += 1
        print(f"\n🎯 The probability of your password among all possible {digits}-digit combinations is: {(number2 / (11 ** digits)) * 100:.8f}%\n")
        print("Thank you for using the Password Combination Percentage Calculator! Goodbye! 👋")
        break
    if digits == 5:
        number = 0
        number2 = 0
        total = 11 ** 5
        for i in range(0, 11):
            for j in range(0, 11):
                for k in range(0, 11): 
                    for m in range(0, 11):
                        for z in range(0, 11):
                            number += 1
                            if number == total:
                                print(f"\n🔢 Calculating... Total combinations checked for a {digits}-digit password: {number}")
                            if (i == password_digits[0] and j == password_digits[1] and k == password_digits[2] and m == password_digits[3] and z == password_digits[4]):    
                                number2 += 1
        print(f"\n🎯 The probability of your password among all possible {digits}-digit combinations is: {(number2 / (11 ** digits)) * 100:.8f}%\n")
        print("Thank you for using the Password Combination Percentage Calculator! Goodbye! 👋")
        break
    if digits == 6:
        number = 0
        number2 = 0
        total = 11 ** 6
        for i in range(0, 11):
            for j in range(0, 11):
                for k in range(0, 11): 
                    for m in range(0, 11):
                        for z in range(0, 11):
                            for y in range(0, 11):
                                number += 1
                                if number == total:
                                    print(f"\n🔢 Calculating... Total combinations checked for a {digits}-digit password: {number}")
                                if (i == password_digits[0] and j == password_digits[1] and k == password_digits[2] and m == password_digits[3] and z == password_digits[4] and y == password_digits[5]):    
                                    number2 += 1
        print(f"\n🎯 The probability of your password among all possible {digits}-digit combinations is: {(number2 / (11 ** digits)) * 100:.8f}%\n")
        print("Thank you for using the Password Combination Percentage Calculator! Goodbye! 👋")
        break
    if digits == 7:
        number = 0
        number2 = 0
        total = 11 ** 7
        for i in range(0, 11):
            for j in range(0, 11):
                for k in range(0, 11): 
                    for m in range(0, 11):
                        for z in range(0, 11):
                            for y in range(0, 11):
                                for b in range(0, 11):
                                    number += 1
                                    if number == total:
                                        print(f"\n🔢 Calculating... Total combinations checked for a {digits}-digit password: {number}")
                                    if (i == password_digits[0] and j == password_digits[1] and k == password_digits[2] and m == password_digits[3] and z == password_digits[4] and y == password_digits[5] and b == password_digits[6]):    
                                        number2 += 1
        print(f"\n🎯 The probability of your password among all possible {digits}-digit combinations is: {(number2 / (11 ** digits)) * 100:.8f}%\n")
        print("Thank you for using the Password Combination Percentage Calculator! Goodbye! 👋")
        break
    if digits == 8:
        number = 0
        number2 = 0
        total = 11 ** 8
        for i in range(0, 11):
            for j in range(0, 11):
                for k in range(0, 11): 
                    for m in range(0, 11):
                        for z in range(0, 11):
                            for y in range(0, 11):
                                for b in range(0, 11):
                                    for a in range(0, 11):
                                        number += 1
                                        if number == total:
                                            print(f"\n🔢 Calculating... Total combinations checked for a {digits}-digit password: {number}")
                                        if (i == password_digits[0] and j == password_digits[1] and k == password_digits[2] and m == password_digits[3] and z == password_digits[4] and y == password_digits[5] and b == password_digits[6] and a == password_digits[7]):    
                                            number2 += 1
        print(f"\n🎯 The probability of your password among all possible {digits}-digit combinations is: {(number2 / (11 ** digits)) * 100:.8f}%\n")
        print("Thank you for using the Password Combination Percentage Calculator! Goodbye! 👋")
        break























