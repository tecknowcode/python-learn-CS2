from week_4.function import return_char

def main():
    numbers = [72,69,76,76,79]

    result = map(return_char,numbers)
    print(list(result))
    
if __name__ == "__main__":
    main()