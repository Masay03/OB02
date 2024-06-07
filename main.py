class User():
    def __init__(self, user_id, name ):
        self._user_id = user_id
        self._name = name
        self._level = "user"

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def set_name(self, name):
        self._name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._level = "admin"

    def add_user(self, user_list, user):
        user_list.append(user)
        print(f"Пользователь успешно добавлен в список: {user}.")

    def remove_user(self, user_list, user):
        user_list.remove(user)
        print(f"Пользователь успешно удален из списка: {user}.")

users = []
admin = Admin(1, "admin")
admin.add_user(users, User(2, "user1"))
admin.add_user(users, User(3, "user2"))
admin.remove_user(users, User(3, "user2"))