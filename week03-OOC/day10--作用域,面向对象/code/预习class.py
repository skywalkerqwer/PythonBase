class Restaurant():
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print('restaurant name is:'+self.name.title())
        print('cuisine type is:'+self.type.title())

    def open_restaurant(self):
        print("Is open now!")

restaurant = Restaurant('KFC','Fast food')
restaurant.describe_restaurant()
restaurant.open_restaurant()

