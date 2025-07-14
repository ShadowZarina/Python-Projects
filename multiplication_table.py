# Multiplication Table Generator

rows = int(input("How many rows do you want to include? "))
columns = int(input("How many columns do you want to include? "))

def table_generator(rows, columns):
    
    x = 1
    y = 1
    
    while x <= rows:
        print(x)
        x += 1

    while y <= columns:
        print("")
        print(y,end='\t')
        z = 2
        while z <= columns:
            print(y*z,end='\t')
            z += 1
        y += 1
    print()

table_generator(rows, columns)
