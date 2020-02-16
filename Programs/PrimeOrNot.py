x = int(input("Enter any positive integer"))

if x < 2:
    print("Given number is not prime number")

elif x == 2:
    print("Given number is prime number")

elif x >= 3:
    for i in range(3, x):
        if x % i == 0:
            print("not prime number")
            break
    else:
        print("prime")
