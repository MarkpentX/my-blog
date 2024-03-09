# users = {
#    "user": {
#        "id": 1,
#        "name": "John",
#        "age": 22,
#    },
#    "user2": {
#        "id": 2,
#        "name": "Jack",
#        "age": 19,
#    },
#    "user3": {
#        "id": 3,
#        "name": "Eva",
#        "age": 17
#    },
# }
#
# for item in users:
#     print(users[item]["id"])
#     print(users[item]["age"])
#     print(users[item]["name"])
#     print("------------------")


class User:
    def __init__(self, id: int, name:str, age:int):
        self.id = id
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello from {self.name}")


user1 = User(1, "John", 19)
user1.say_hello()

user2 = User(2, "Jack", 16)
user2.say_hello()

user3 = User(3, "Eva", 15)
user3.say_hello()
# users = [user1, user2, user3]
#
# for item in users:
#     print(item.id)
#     print(item.name)
#     print(item.age)
#     print("***********")

