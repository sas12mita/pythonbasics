with open("Sample.txt", "r") as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())

try:
    with open("sample.doc","r") as file:
        for var in file:
            var=var.strip()
            print(var)
except FileNotFoundError:
    print("File doesnot exist")
    