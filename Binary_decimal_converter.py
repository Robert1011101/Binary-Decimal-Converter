convert_to = None

def user_input():
    global convert_to
    convert_to = int(input("Input 1, to convert decimal to binary, or 2 to convert binary to decimal"))

def decimal_binary():
    i = int(input("Input a number in decimal   : "))
    b = 0
    while 2**b <= i:
        b = b + 1
    b = b - 1
    while i != 0:
        i = i - 2**b
        if i < 0:
            i = i + 2**b
            b = b - 1
            print (0)
        else:
            b = b - 1
            print (1)
    while b != -1:
        b = b - 1
        print (0)
        
def binary_decimal():
    i = int(input("Input a number in binary   : "))
    count = 0
    d = 0
    while i != 0:
        if i % 2 == 1:
            d = d + (2**count)
            i = i/10 - 0.1
            count = count + 1
        elif i % 2 == 0:
            count = count + 1
            i = i/10
        else:
            print ("This is not a binary number")
            break
    print (d)

def run():
    user_input()
    if convert_to == 1:
        decimal_binary()

    elif convert_to == 2:
            binary_decimal()
    else:
        print ("Enter either 1 or 2")

while True:
    run()
