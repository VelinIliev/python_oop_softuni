from project.user import User
from project.library import Library


class Registration:
    def __init__(self):
        pass

    def add_user(self, user: User, library: Library):
        users = [x.user_id for x in library.user_records]
        if user.user_id not in users:
            library.user_records.append(user)
        else:
            return f'User with id = {user.user_id} already registered in the library!'

    def remove_user(self, user: User, library: Library):
        for i, x in enumerate(library.user_records):
            if user.user_id == x.user_id:
                library.user_records.pop(i)
        else:
            return f'We could not find such user to remove!'

    def change_username(self, user_id: int, new_username: str, library: Library):
        for x in library.user_records:
            if x.user_id == user_id:
                if x.username == new_username:
                    return f'Please check again the provided username - it should be different than the username used so far!'
                else:
                    x.username = new_username
                    return f'Username successfully changed to: {new_username} for user id: {user_id}'
        else:
            return f'There is no user with id = {user_id}!'