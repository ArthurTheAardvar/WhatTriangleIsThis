
cases = int(input()) 


def better_round(val:float, n_digits:int = 0):
    val *= 10**n_digits
    result = int(val + (0.50002 if val >= 0 else -0.50002))
    return result / 10**n_digits

for i in range(cases): #go through the other lines
    line = input().rstrip()
    
    line = line.split(", ") #split up the line by spaces
     
    a = float(line[0])
    b = float(line[1])
    c = float(line[2])


    if a + b <= c or b + c <= a or c + a <= b:
        print("Not a Triangle")
        
    else:
        if a == b and a != c or b == c and b != a or c == a and c != b:
            print("Isosceles")
        

        elif a == b and a == c and b == c:
            print("Equilateral")

        if a + b > c:
            if a != b and a != c and b != c:
                print("Scalene")

    
