x = int(input("Select an integer and press enter"))
rev = int(str(abs(x))[::-1])
if rev > 2**31 or rev < -2**31:
    print("0")
elif x < 0:
    print(-1*rev)
else:
    print(rev)