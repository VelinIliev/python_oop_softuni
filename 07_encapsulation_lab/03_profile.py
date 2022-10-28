class Profile:
    def __init__(self, username: str, password: str):
        if len(username) < 5 or len(username) > 15:
            raise ValueError(f'The username must be between 5 and 15 characters.')
        count_upper_case = 0
        count_digits = 0
        for char in password:
            if char.isupper():
                count_upper_case += 1
            elif char.isdigit():
                count_digits += 1
        if len(password) < 8 or count_upper_case < 1 or count_digits < 1:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        __username = username
        __password = password

    def __str__(self):
        return f'You have a profile with username: "{__username}" and password: {"*" * len(__password)}'


# profile_with_invalid_password = Profile('My_username', 'My-password')
# #
# profile_with_invalid_username = Profile('Too_long_username', 'Any')

correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
