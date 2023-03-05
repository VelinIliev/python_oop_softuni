class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError(f'The username must be between 5 and 15 characters.')
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        count_upper_case = 0
        count_digits = 0
        for char in value:
            if char.isupper():
                count_upper_case += 1
            elif char.isdigit():
                count_digits += 1

        if len(value) < 8 or count_upper_case < 1 or count_digits < 1:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

#
# profile_with_invalid_password = Profile('My_username', 'My-password')
# print(profile_with_invalid_password)
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
# print(profile_with_invalid_username)
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)


