def greetings():
    print("hello")
greetings()

def greetings(hcl):
    name="welcome"+hcl
    print(name)
    name="hcl"
greetings(name)

def square( ):
    string_1 = str(input())
    b=string_1.split( )
    a=list(b)
    print(a)
list=[ ]
    for i in range(a):
        i=i**2
        print(i)
square()

number=int(input( ))
def division(number):
    if number%7==0:num=int(input( ))
        print("true")
    else:
        print("false")
division(number)

num=(input())
def division(num):
    if num%3==0 and num%5!=0:
        print("marco")
    elif num%5==0 and num%3!=0:
        print("polo")
    elif num%3==0 and num%5==0:
        print("macropolo")
    else:
        print("no")
division(num)






side=int(input())
area=side*side
perimeter=4*side
print(area)
print(perimeter)







