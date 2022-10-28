class EmailValidator:
    def __init__(self, min_length:int, mails: list, domains: list):
        min_length = min_length
        mails = mails
        domains = domains

    def __is_name_valid(self, name):
        if len(name) < min_length:
            return False
        else:
            return True

    def __is_mail_valid(self, mail):
        if mail in mails:
            return True
        else:
            return False

    def __is_domain_valid(self, domain):
        if domain in domains:
            return True
        else:
            return False

    def validate(self, email):
        x = email.split("@")
        username = x[0]
        mail, domain = x[1].split(".")
        if __is_name_valid(username) and __is_mail_valid(mail) and __is_domain_valid(domain):
            return True
        else:
            return False



mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
