def segreagrateMarks(lst):
    a = []
    b = []
    c = []
    for val in lst:
        if val >= 80:
            a.append(val)
        elif val < 80 and val > 50:
            b.append(val)
        else:
            c.append(val)   
    return a, b, c

def calculateBill(units):
    if units > 200:
        return 100+(100*2)+(units-200)*3
    elif units <= 200 and units > 100:
        return  (units-100)*2 + 100
    else:
        return units * 1
    
def cumulativeAddition(lst):
    out = []
    addition = 0
    for val in lst:
        addition += val
        out.append(addition)
    
    return out

def main():
    numbers = [3, 5, 2, 4, 1]
    result = cumulativeAddition(numbers)
    print(result)

if __name__ == "__main__":
    main()


input = [2, 5, 4, 2, 8, 9, 5, 3, 6, 2, 4]
output = [2, 5, 4, 8, 9, 3, 6]

for val in input:
    if val not in output:
        output.append(val)