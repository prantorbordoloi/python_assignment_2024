list = ["hello" , "i" , "am" , "Prantor"]
def add_excitement(list):
    for i in range(len(list)):
        list[i] += "!"
    
    print("the list is : ")
    for i in list:
        print(i)

add_excitement(list)