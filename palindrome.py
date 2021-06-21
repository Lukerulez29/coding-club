a = int(input())

def Palindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0): 
                print("False")

    z = 0
    while (x > z):
        z = z * 10 + x % 10
        print("z:" + str(z))
        x = x // 10
        print("x:" + str(x))
    if x == z:
        print("True")
    elif x == z//10:
        print("True")
    else:
        print("False")

Palindrome(a)
            