for i in range(1,100):
    if i%15 == 0:
        i = "FizzBuzz"
    elif i % 5 == 0 :
        i = "Buzz"
    elif i % 3 == 0:
        i = "Fizz"
    print(i)    