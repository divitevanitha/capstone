try:
    a=int(input())
    b=int(input())
    div=a/b
    print(div)
except ZeroDivisionError:
        print("deneminator is zero")
except ValueError:
        print("value should be a number")


