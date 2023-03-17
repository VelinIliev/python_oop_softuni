from abc import ABC, abstractmethod


class IContent(ABC):
    def __init__(self, content):
        self.content = content

    @abstractmethod
    def __str__(self):
        ...


class MyContent(IContent):
    def __str__(self):
        return f'<MyML>{self.content}</MyML>'


class HTTPContent(IContent):
    def __str__(self):
        return f'<HTTP>{self.content}</HTTP>'


class DIVContent(IContent):
    def __str__(self):
        return f'<DIV>{self.content}</DIV>'


protocols = {"IM": "I'm"}


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def get_protocol(self):
        return protocols[self.protocol] if self.protocol in protocols else self.protocol

    def set_sender(self, sender):
        self.__sender = f'{self.get_protocol()} {sender}'

    def set_receiver(self, receiver):
        self.__receiver = f'{self.get_protocol()} {receiver}'

    def set_content(self, content):
        self.__content = content

    def __repr__(self):
        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"


# email = Email('IM', 'MyML')
# email.set_sender('qmal')
# email.set_receiver('james')
# email.set_content('Hello, there!')
# print(email)

email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = MyContent('Hello, there!')
email.set_content(content)
print(email)
