
cases = int(input()) 

for i in range(cases): #go through the other lines
    line = input().rstrip()
    
    line = line.split(", ") #split up the line by spaces
     
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])

    if a + b > c:
        if a == b != c or a == c != b or b == c != a:
            print("Isosceles")
        

        elif a == b and a == c and b == c:
            print("Equilateral")
        if a + b > c:
            if a != b and a != c and b != c:
                print("Scalene")

    if a + b < c:
        print("Not a Triangle")
