def read_file():
    with open("C:\pythonCode\data.csv") as data:
        contants = data.read()
        print(contants)


def read_lines():
    with open("C:\pythonCode\data.csv") as data:
        contants = None
        line_number = 1
        for line in data.readlines():
            yield f"{line_number}-  " + line.strip()
            line_number += 1
            # contants = data.readline()
            # print(contants)


def write_to_file(text):

    writeTofile = open("file.txt", 'w+')
    writeTofile.write(text)
    writeTofile.close()

    with open("file2..txt", "a") as f:
        f.write(text)
    print(type(f))


def create_file(name="filename"):
    createfile = open(f"{name}.txt", "x")
    createfile.close()
    return createfile.name


def copy_file(source_file, destination_file):
    with open(source_file, "r") as source:
        data = ""
        for line in source.readlines():
            if "Wednesday" in line:
                data += line
        with open(destination_file, "a") as destination:
            destination.write(data)


match int(input("Enter 1 to creat a file 2 to write to a file:  ")):

    case 1:
        print(create_file(input("Enter the name of the file: ")))

    case 2:
        write_to_file(input("Your text: "))

    case 3:
        read_file()

    case 4:
        for line in read_lines():
            print(line)
    case 5:
        copy_file("data.csv", create_file("copy_data"))
