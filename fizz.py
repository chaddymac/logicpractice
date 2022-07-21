x = range(1,101)

for n in x:
    if n % 3 == 0 and n % 5 == 0:
        print("Fizzbuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)



