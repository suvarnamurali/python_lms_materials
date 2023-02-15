class Product:
    count = 0
    def __init__(self,name,category,price):
        self.name = name
        self.category = category
        self.__price = price 
        Product.count =+ 1
    def display_product(self):
        print("name:",self.name)
        print("category:",self.category)
        # print("price:",self.__price)
    def product_count(self):
        print("total number of products : %d" %Product.count)

    def calculate_price(self):
        price = self.__price * (100/50)
        
        return price

    def set_price(self,price):
        self.__price = price
        
    def get_price(self):
        return self.__price

prod1 =Product('pen','stationary',30)
# print(prod1.__price)

# name mangling 

# print(prod1._Product__price)

# creating another variable and storing value 
# prod1.__price = 40

# print(prod1.__price)
# print(prod1._Product__price)

# getters and setters 

        
prod1.set_price(60)
print(prod1.get_price())
print(prod1._Product__price)

# price updated using set price and get it 