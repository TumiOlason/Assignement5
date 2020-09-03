n = int(input("Enter the length of the sequence: ")) # Do not change this line
n0 = 1
n1 = 2
n2 = 3
if n == 1:
    print(n0)
elif n == 2:
    print(n1)
elif n == 3:
    print(n2)
else:
    print(n0)
    print(n1)
    print(n2)
    for i in range(4, n+1):
        n3 = n0 + n1 + n2
        n0 = n1
        n1 = n2
        n2 = n3
        print(n3)