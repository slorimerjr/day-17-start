class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Sam")
user_2 = User("002", "Jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# class Car:
#     def __init__(self, seats):
#         self.seats = seats
#     def enter_race_mode(self):
#         self.seats = 2
#
# car_1 = Car(5)
# print(car_1.seats)
# car_1.enter_race_mode()
# print(car_1.seats)