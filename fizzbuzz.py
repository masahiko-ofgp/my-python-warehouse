def fizzbuzz(n):
    if (n % 15) == 0:
        print("Fizzbuzz")
    elif (n % 5) == 0:
        print("Buzz")
    elif (n % 3) == 0:
        print("Fizz")
    else:
        print(n)

def fizzbuzz2(n):
    fizzp, buzzp = ((n % 3 == 0), (n % 5 == 0))
    if fizzp & buzzp:
        print("Fizzbuzz")
    elif (not fizzp) & buzzp:
        print("Buzz")
    elif fizzp & (not buzzp):
        print("Fizz")
    else:
        print(n)
    

if __name__ == '__main__':
    for i in range(0, 31):
        fizzbuzz2(i)
