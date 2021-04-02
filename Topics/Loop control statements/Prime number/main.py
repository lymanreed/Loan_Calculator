n = int(input())
prime = True
if n == 1:
    prime = False
else:
    for x in range(2, n):
        if not n % x:
            prime = False
            break
print("This number is", end=" ")
print("prime" if prime else "not prime")
