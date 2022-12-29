#print addition of multiple numbers
print(2+3+4+5)
#print length of string
a="welcometohcl"
print(len(a))
#print "python is amazing",use tab space and new line character
print("python\tis\t\namazing")
#int
#float
#complex
#set
#boolen
#tuple
#dictionary
#list
list_a=[1,2,3,5]
list_b=list_a
print(list_b)


print(id(list_a))
print(id(list_b))

list_b[3]=4

print(list_a)
print(list-b)
list_a=[1,2]
list_b=list_a
list_a=list_a+[6,7]
print(list_a)

list_a=[1,2,3,4,5]
list_b=list_a[0:4]
print(list_b)

list_a=[1,2,3,4,5]
print(list_a[4])
print(list_a[-1])

list_a=[5,6,7,8,9]

list_b=list_a[:4]
print(list_b)

list_a=[5,4,3,2,1]
list_b=list_a[4:0:-1]
print(list_b)

list_a[2]="name"
print(list_a)

list_a.remove("string" "dhana")

print(list_a)

string_1="program"
string_2=string_1[6:0:-2]
print(string_2)

id("hello")
id(object)
print(id("10"))

list_a=["1,2,3,4,5"]
print(list_a)

list_a=[1,2,3,4]
list_b=list_a
print(id(list_a))
print(id(list_b))

list_b[0]=5
print(list_a)
print(list_b)

list_a=[1,2]
list_b=list_a
list_a=list_a+[6,7]
print((list_a))
print((list_b))
a="1 2 3 6     5"
list_a=a.split()
print(list_a)

list_a="appleballcatdogegg"
list_b=list_a.split('a')
print(list_b)

list_a=[1,2,3,4,5]
print(list_a[4])
print(list_a[-1])

list_a=[1,2,3,4,5]
list_b=list_a[-5:-1]
print(list_b)

n=int(input())
m=str(input())

#string concepts

a="waterfall"
part=a[0:7:2]
print(part)

is_digit="4748".isdigit()
print(is_digit)

mobile="    9392 48 8105   "
mobile=mobile.strip()
print(mobile)

name=".ravi/"
name=name.strip("/")
print(name)

name=",,..vanitha...xx,,,"
name=name.strip(",,..")
print(name)

sentence="teh cat and teh dog"
sentence=sentence.replace("teh","the")
print(sentence)

url="https://onthegomodel.com"
is_secure_url=url.startswith("https://")
print(is_secure_url)

gmail_id="rahul123@gmail.com"
is_gmail=gmail_id.endswith("@gmail.com")
print(is_gmail)

name="vanitha"
print(name.upper())

Name="VANITHA"
print(Name.lower())

Date="dd/mm/yy"
#print(Date.replace("/","-"))
Date=Date.upper()
print(Date.replace("/","-"))


Name="Mercy@123"
cap_char=0
small_char=0
spec_char=0
num_char=0
for ele in range(len(input())):
    if(cap_char==0 and small_char==0 and spec_char==0 and num_char==0):
        print(==+1)
    else:
        print(==0)
        print("strong password")
        print("not a strong password")
