A = int(input("A: "))
B = int(input("B: "))
if A < B:
    i = A
    while i <= B:
        print(i)
        i += 1
else:
    i = A
    while i >= B:
        print(i)
        i -= 1