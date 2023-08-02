class User:
    def __init__(self, userid, username):
        #intialize
        self.id = userid
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Hardik")
user_2 = User("002","Happy")
# user_1.id = "001"
# user_1.USERNAME = "Hardik"
#
# print(user_1.id)
# print(user_1.USERNAME)
# print(user_1.followers)
# user_1.follow(user_2)
# print(user_1.following)
# print(user_2.followers)
# print(user_1.followers)
# print(user_2.following)


