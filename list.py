import random as rd


def favorit_frukter(element, action):
    list = []
    frukter = ["Apple", "pinapple", "watermellon", "greps", "climenten",
               "potatos", "greps", "watermellon", "watermellon", "watermellon"]
    if (action == "add"):
        frukter.append(element)
        print(frukter)
    elif (action == "edit"):
        frukter.insert(3, element)
        print(frukter)
    elif (action == "remove"):
        frukter.pop(int(len(frukter)/2-1))
        frukter.remove(element)
        print(frukter)
    elif (action == "print"):
        for frukt in frukter:
            print(frukt)
        print(frukter.count("watermellon"))
        print(frukter.copy())
    elif (action == "slic"):
        print(frukter[2:5])
    elif (action == "stepslic"):
        print(frukter[1:5:2])

    elif (action == "omvand"):
        omfrukter = frukter[-1::-1]
        print(omfrukter)
        frukter.reverse()
        print(frukter)

    return frukter


def ran():
    list = []
    for _ in range(10):
        list.append(rd.randrange(4, 93))
    print(list)
    print(f"inbyggada Max function: {max(list)}")
    print(f"inbyggada Max function: {min(list)}")
    list.sort()
    print(f"inbyggada Max function: {list}")
    print(f"inbyggada Max function: {sum(list)}")

    max1 = list[0]
    for a in list:
        if max1 < a:
            max1 = a
    print(max1)
    return list


def jamnaTal(arr):
    num = 0
    for v in arr:
        if v % 2 != 0:
            num += 1
    print(f"this is the sum function: {sum(arr)}")
    return num


def suma(listA, listB):
    listAlistB = []
    for i in range(len(listA)):
        listAlistB.append(listA[i]+listB[i])
    return listAlistB


def persionDict():
    person = {
        "name": "Sirajulhaq",
        "lastn": "Wahaj",
        "email": "this@gmail.com",

    }
    person["tele"] = "89282"
    person.update({"age": 93})
    person["age"] += 1
    for key, value in person.items():
        print(key, " -----", value)

    if "mellannamn" not in person:
        person["mellannamn"] = "Khan"

    return person


def dynamicDict():
    my_dict = dict()
    for i in range(15):
        my_dict[i] = i**2

    for key, value in my_dict.items():
        print(f" {key } ----> {value}")

    sum1 = 0
    for value in my_dict.values():
        sum1 += value
    return sum1


match int(input(f"Choose 1. for ran and 2. for favorit_rukter:"
                "3. kombinera listor"
                "4. hitta jämmna tal   ")):

    case 1:
        ran()
    case 2:
        favorit_frukter(input("\nEnter the element:   "),
                        input("\nEnter the action:   "))
    case 3:
        print(ran() + favorit_frukter("this", "omvand"))
    case 4:
        tal = []
        while True:
            userinput = input("Enter the numbers: ")
            if (int(userinput) in tal):
                break
            tal.append(int(userinput))
            print(tal)
        print(jamnaTal(tal))
    case 5:
        listx1, listx2 = [3, 5, 7, 9], [3, 2, 90, 1]
        print(suma(listx1, listx2))
    case 6:
        print(persionDict())
    case 7:
        print(dynamicDict())
