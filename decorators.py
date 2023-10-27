from readable_dict import readable_dic


def total(*args, **kwargs):
    positional = ""
    for value in args:
        positional += str(value) + ", "
    print("Positional arguments: ")
    print(f"{positional} = {sum(args)}")

    print("Key word arguments: ")
    print(type(kwargs))
    readable_dic(kwargs)


total(12, 3, 9, 3, 11, 23,  Alice="28",
      Bob="35",
      Charlie="22",
      David="29",)
