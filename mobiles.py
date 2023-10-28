class Mobile:
    def __init__(self, brand, price, ram, camera):
        self.brand = brand
        self.price = price
        self.ram = ram 
        self.camera = camera

    def display(self):
        print("Brand: ", self.brand)
        print("Price: ", self.price)
        print("Ram: ", self.ram)
        print("Camera: ", self.camera)
        print("--------------------------------------")

iphone = Mobile("Apple", 100000, '8Gb', '48mp')
iphone.display()
redmi = Mobile('Xiaomi', 20000, '8Gb', '108mp')
redmi.display()

        