class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f"We are {self.name} and eat {self.cuisine}")

    def open_restaurant(self):
        print(f"{self.name} opens at 8:00 am daily")

restaurant = Restaurant("May's food", "italian")
print(f"This is {restaurant.name}")
print(f"we eat {restaurant.cuisine}")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_1 = Restaurant("Kfc", "chicken")
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant("Dominos", "pizza")
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant("cold stone", "ice-cream")
restaurant_3.describe_restaurant()