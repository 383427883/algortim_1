#1-task
list1 = []

def lst1():
    n = int(input("1-son: "))
    y = int(input("2-son: "))
    z = int(input("3-son: "))
    list1.append(n)
    list1.append(y)
    list1.append(z)
    print(list1)
    return f"{list1[0]}\n"

print(lst1())

#2-task
def lst2():
    list1 = [1,2,3]
    list2 = [4,5,6,7]
    print(f"{list1},{list2}")
    list1.extend(list2)
    return f"{list1}\n"

print(lst2())


#3-task
def lst3():
    lists = [1,2,3,4,5,6,7]
    print(lists)
    return f"{lists[-1]}\n"

print(lst3())

#4-task
list3 = []

def lst4():
    num1 = int(input("num: "))
    num2 = int(input("num: "))
    print(f"{num1},{num2}")
    list3.append(num1)
    list3.append(num2)
    return list3

print(lst4())