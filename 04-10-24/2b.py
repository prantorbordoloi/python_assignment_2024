list = ["hello" , "i" , "am" , "Prantor"]
new_list=[]
def add_excitement(list,new_list):
    for i in range(len(list)):
        new_list.append(list[i]+"!")
    
    print("the new list is : ")
    for i in new_list:
        print(i)

add_excitement(list,new_list)