def readable_dic(dictionary):
    max_key_length = max(len(str(key)) for key in dictionary.keys())

    for key, value in dictionary.items():
        padding = " " * (max_key_length - len(str(key)))
        print(f"{key}:{padding}{value}")
