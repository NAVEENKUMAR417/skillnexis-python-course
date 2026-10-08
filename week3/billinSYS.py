class product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_price(self):
        return self.price * self.quantity

class bill:
    def __init__(self):
        self.products = []
    def add_product(self,product):
        self.products.append(product)
    def calculate_total_price(self):
        total_price = 0
        for product in self.products:
            total_price += product.total_price()

        return total_price

    def display(self):
        print("\n========== BILL ==========")
        print("Product\t\tPrice\tQuantity\tTotal")

        for product in self.products:
            total_price = product.total_price()
            print(
                product.name,
                "\t\t",
                product.price,
                "\t",
                product.quantity,
                "\t\t",
                total_price
            )

        subtotal=self.calculate_total_price()
        tax=subtotal*0.18
        final_price=subtotal+tax


        print("\nSubtotal:",subtotal)
        print("Tax:",tax)
        print("Final price:",final_price)
#this is a section which user gives to the system
bill=bill()
product1=product("laptop",50000,10)
product2=product("bag",500,100)
product3=product("stand",500,20)

bill.add_product(product1)
bill.add_product(product2)
bill.add_product(product3)

bill.display()
