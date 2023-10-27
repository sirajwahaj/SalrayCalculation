import readable_dict as readable_dic


def rovarsprok(word):
    consonat = "bcdfghjklmnpqrstvwxyz"
    rovsentence = ""

    for letter in word:
        if letter.lower() in consonat:
            rovsentence += f"{letter}o{letter}"
        else:
            rovsentence += letter
    print(rovsentence)


def count_letters(sentence):
    letter_dict = {}
    for letter in sentence.lower():
        letter_dict[letter] = letter_dict.get(letter, 0) + 1
    readable_dic(letter_dict)


def count_word(text):
    text = text.lower()
    words = text.split(" ")
    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1
    readable_dic(word_dict)


def exchange_key_value(dictionary):
    reversed_dict = {}
    for key, value in dictionary.items():
        if value in reversed_dict:
            if isinstance(reversed_dict[value], list):
                reversed_dict[value].append(key)
            else:
                reversed_dict[value] = [reversed_dict[value], key]
        else:
            reversed_dict[value] = key
    readable_dic(reversed_dict)


person_data = {
    "person1": {"name": "Alice", "age": 28, "city": "New York"},
    "person2": {"name": "Bob", "age": 35, "city": "Chicago"},
    "person3": {"name": "Charlie", "age": 22, "city": "Los Angeles"},
    "person4": {"name": "David", "age": 31, "city": "San Francisco"},
    "person5": {"name": "Eva", "age": 29, "city": "Miami"},
    "person6": {"name": "Frank", "age": 40, "city": "Seattle"},
    "person7": {"name": "Grace", "age": 26, "city": "Boston"},
    "person8": {"name": "Helen", "age": 33, "city": "Austin"},
    "person9": {"name": "Irene", "age": 27, "city": "Denver"},
    "person10": {"name": "Jack", "age": 38, "city": "Portland"}
}

person_data2 = {
    "Alice": "28",
    "Bob": "35",
    "Charlie": "22",
    "David": "29",
    "Eva": "29",
    "Frank": "40",
    "Grace": "22",
    "Helen": "35",
    "Irene": "22",
    "Jack": "35"
}
match int(input("Choose the function you want to call:  ")):
    case 1:
        rovarsprok(input("Enter a sentence or a word: "))
    case 2:
        count_letters(input("Enter a sentence: "))
    case 3:
        count_word(input("Enter a sentence: "))
    case 4:
        exchange_key_value(person_data2)
