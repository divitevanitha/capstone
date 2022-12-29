list_a =[1,2,3,4,2,3,6]
set_a =set(list_a)
print(set_a)
list_b =list(set_a)
print(list_b)

set_a={1,2,3,4}
set_b={11,9,5,6,7}
set_c=set_a|set_b
print(set_c)


set_a={1,2,3,4,5,6,8}
to_delete = 1,2,3,4
set_a.difference_update(to_delete)
print(set_a)


set_a={1,2,3,4,5,6,7}
set_b={1,2,3,4,5,6,}
is_subset=set_b.issubset(set_a)
print(is_subset)

is_superset=set_a.issuperset(set_b)
print(is_superset)

set_a={1,2,3}
set_b={4,5,6}
is_disjoint=set_b.isdisjoint(set_a)
print(is_disjoint)

set_a={1,2,3,4,5}
set_b={4,5,6,7,8}
set_c={7,8,9,4,1}
intersection=set_a &set_b & set_c
print(intersection)

list_a=[5,"six",[8,6],8.2]
print(list_a[2])
print(list_a[2][0])

dict_a={
    'name':'vanitha'
    'age': 21
}
del dict_a['age']
print(dict_a)


dict_a={ }
m=int(input())
n=int(input())
for i in range(m,n):
    dict_a[i]=i**2
    print(dict_a)

rows=int(input("enter the rows:"))
columns=int(input("enter the columns:"))
matrix=[]
for i in range(rows):
    row=input().split()
    for j in rows:
        matrix.append(a)

        print(matrix)
print( )










