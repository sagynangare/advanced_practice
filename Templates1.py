from string import Template
class MyTemplate(Template):
    delimiter = "#"
def main():
    cart = []
    cart.append(dict(item = "Parle-G", price=10,qty=3))
    cart.append(dict(item = "Monaco", price=18,qty=5))
    cart.append(dict(item = "BurBone", price=30,qty=2))

    t= MyTemplate("#qty * #item= #price")

    total = 0
    print("Cart: ")
    for data in cart:
        print (t.substitute(data))
        total +=data["price"]
    print("Total is:"+str(total))

if __name__=='__main__':
    main()
