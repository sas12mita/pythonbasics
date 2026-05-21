with open("sample.txt", "r") as file:
    data = file.read((10))
    print(data)
    print(file.read(5))
    print(file.red(5))
    #position if curson
    print(file.tell())
    #seek() chnage 
    