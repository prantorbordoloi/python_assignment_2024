inventory={}

def add_inv(inv,name,price,qtn):
    inv[name] = ("₹" + str(price),qtn)

def update_inv(inv,name,sold_qtn):
    if name not in inv:
        print(f"{name} does not exist in the inventory...")
        return
    price,avl_qtn = inv[name]
    if sold_qtn>avl_qtn:
        print(f"not enough {name} in the inventory to sell ... aavailable quantity is {avl_qtn}")
        return
    new_qtn = avl_qtn-sold_qtn
    inv[name] = (price,new_qtn)
    print(f"name:{name}, sold quantity : {sold_qtn}, remaining quantity : {new_qtn}" )

def display(inv):
    print("\n inventory items are : ")

    for name,(price,qtn) in inv.items():
        print(f"{name} : price ${price} , quantity ${qtn}")

add_inv(inventory,"apple",20,100)
update_inv(inventory,"apple",20)
display(inventory)
    