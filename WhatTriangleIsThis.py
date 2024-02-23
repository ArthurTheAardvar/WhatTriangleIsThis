
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

    if better_round(a + b > c):
        if better_round(a == b != c or a == c != b or b == c != a):
            print("Isosceles")
        

        elif better_round(a == b and a == c and b == c):
            print("Equilateral")
        if better_round(a + b > c):
            if better_round(a != b and a != c and b != c):
                print("Scalene")

    if better_round(a + b < c):
        print("Not a Triangle")
