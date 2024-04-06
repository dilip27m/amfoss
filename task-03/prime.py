n = int(input("Enter  the number : "))
print("The Prime numbers up to", n, ":")
for i in range(2, n + 1):
    #a whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1 
    count = 0
    '''here we are using count variable to show that how many times it is exactly divided 
    if the count is 2 them is only divided by 1 and itself 
      then we can it is a prime number  '''
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i)
print("These are the prime numbers upto ",n,)        