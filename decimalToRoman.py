# Array with roman number
arrRomans = ["M", "CM", "D", "CD", "C", "L", "XL", "X", "IX", "V", "IV", "I"]

# Array with roman number values in decimal
arrDecimals = [1000, 900, 500, 400, 100, 50, 40, 10, 9, 5, 4, 1]

def decimalToRomans(number):
    result = ""
    i = 0
    
    while number > 0:
        for r in arrRomans:
            if arrDecimals[i] <= number:
                number -= arrDecimals[i]
                result += arrRomans[i]
        i += 1
    
    return result

if __name__ == "__main__":
    validado = False
    
    while validado != True:
        try:
            # User input
            userNumber = int(input("Insert a whole number in decimal format: "))
            
            if 0 < userNumber and userNumber < 4000:
                validado = True
                print(decimalToRomans(userNumber))
            else:
                print("Insert a whole number between 1 and 3999 inclusive. Try Again\n")
        except:
            print("The given number is invalid. Try again.\n")