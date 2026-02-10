def greet():
    print("Hi!!! Hello World!!!")

def getNumber():
    number = int(input("Enetr a number: "))
    return number

def checkOddEven(num):
    return bool(num % 2)

def getFactorial(num):
    res = 1
    for num in range(1, num+1):
        res = res * num
    return res

def countNumberOfDigits(num):
    pass

def main():
    greet()
    print("Enter a number for factorial.")
    number = getNumber()
    result = getFactorial(number)
    print(f"factorial of {number} is {result}")
    for num in range(1,upper_limit+1):
        if checkOddEven(num) % 2 :
            print("{} - odd.".format(num))
        else:
            print(f"{num} - even.")

if __name__ == "__main__":
    main()

