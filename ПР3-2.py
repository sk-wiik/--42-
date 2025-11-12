f = float(input("f: "))
k = float(input("k: "))
if k == 2:
    R = 1
elif k < 2:
    R = k**2
elif f < 5 and k > 2:
    R = f + k - 1
else:
    R = "не определено"
print(f"R = {R}")