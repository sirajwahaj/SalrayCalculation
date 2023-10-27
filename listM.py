from collections import Counter

groups = [[24, 3, 1], [23, 0, 5], [83, 2, 4]]


def first_elements_of_nasted_list():
    for elment in groups:
        print(elment[0])


def add_fourth_element(elment):
    for l in groups:
        l.append(elment)
    print(groups)


def sum_nasted_list():
    index = []
    for l in groups:
        index.append(sum(l))
    return index


def repeated_number(sequens):
    elments_repeated = {}
    for l in sequens:
        times = 0
        for n in sequens:
            if l == n:
                times += 1
        elments_repeated[l] = times

    orderd_dict = dict(
        sorted(elments_repeated.items(), key=lambda item: item[1]))
    return list(orderd_dict.items())[-1]
    # most_repeated = elments_repeated[]
    # for key, value in elments_repeated.items():


def repeated_number2(sequence):
    element_counts = Counter(sequence)  # Count occurrences of each element
    most_common_element, count = element_counts.most_common(
        1)[0]  # Get the most common element
    return most_common_element, count


def repeated_number3(sequence):
    elements_repeated = {}  # Dictionary to store element counts
    for element in sequence:
        elements_repeated[element] = elements_repeated.get(element, 0) + 1

    max_count_element = None
    max_count = 0
    for element, count in elements_repeated.items():
        if count > max_count:
            max_count = count
            max_count_element = element

    return max_count_element, max_count


def max_number(sequens):
    mx_number = float('-inf')
    for n in sequens:
        if mx_number < n:
            mx_number = n
    return mx_number


def compare_reverse_list(list1, list2):
    return list1 == list2[-1::-1]


def FizzBuzz(number1):
    for number in range(1, number1+1):
        output = ""
        if number % 3 == 0:
            output += "Fizz"
        if number % 5 == 0:
            output += "Buzz"
        print(output or number)


def string_to_litter(word):
    for i in word[::2]:
        print(i)


match int(input("Select the function you want to try: ")):
    case 1:
        first_elements_of_nasted_list()
    case 2:
        add_fourth_element(input("enter the elment you want to put: "))
    case 3:
        index = 0
        for l in sum_nasted_list():
            print(f"{index}:  {l}")
            index += 1

    case 4:
        # int(input("Enter a list of numbers press enter to end the list: "))
        print(repeated_number([12, 29, 12, 90, 23, 12]))
        print(repeated_number2([12, 29, 12, 90, 23, 12]))
        print(repeated_number3([12, 29, 12, 90, 23, 12]))
    case 5:
        print(max_number([2, 45, 1, 892, 23, 22, 222, 33, float('-inf')]))
    case 6:
        print(compare_reverse_list([2, 3, 4], [4, 3, 2]))
    case 7:
        FizzBuzz(int(input("Enter a number:  ")))
    case 8:
        string_to_litter(input("Enter a string:  "))
