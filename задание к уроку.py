# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.
# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа
# ('user' для обычных сотрудников).
# 2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа,
# специфичный для администраторов ('admin'). Класс должен также содержать методы add_user и remove_user,
# которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    # Getters
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_access_level(self, access_level):
        if access_level in ['user', 'admin']:
            self.__access_level = access_level
        else:
            raise ValueError("Уровень доступа должен быть либо 'user', либо 'admin'")

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')
        self.__admin_access_level = 'admin'

    def add_user(self, user_list, user):
        if isinstance(user, User):
            user_list.append(user)
        else:
            raise TypeError("Можно добавлять только экземпляры пользователя")

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                return
        raise ValueError(f"Пользователь с идентификатором {user_id} не найден")

# Пример использования
if __name__ == "__main__":
    # Создаем список для хранения пользователей
    user_list = []

    # Создаем администратора
    admin = Admin(user_id=1, name="Admin")

    # Создаем обычного пользователя
    user1 = User(user_id=2, name="User1")

    # Администратор добавляет пользователя в список
    admin.add_user(user_list, user1)

    # Проверяем, что пользователь добавлен
    for user in user_list:
        print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")

    # Администратор удаляет пользователя из списка
    admin.remove_user(user_list, user_id=2)

    # Проверяем, что пользователь удален
    if not user_list:
        print("Список пользователей пуст")