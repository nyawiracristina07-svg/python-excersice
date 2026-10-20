# user_one_name = "john"
# user_one_last_name = "doe"
# user_one_age = 30
# user_one_admin = False
# user_one_score = 85.5

# user_two_name = "jane"
# user_two_last_name = "miriam"
# user_two_age = 25
# user_two_admin = True
# user_two_score = 92.0

user_one = {
    "name": "john",
    "last_name": "doe",
    "age": 30,
    "admin": False,
    "score": 85.5
}
user_two = {
    "name": "jane",
    "last_name": "miriam",
    "age": 25,
    "admin": True,
    "score": 92.0
}

def show_user_data(some_data):
    print(some_data,type(some_data))

show_user_data(user_one["age"])

user_two["score"] += 3
show_user_data(user_two["score"])
