# All readers,writers, and speakers are users
class User():
    def sign_in(self):
        print('logged_in')
# creating attributes and functions for Reader


class Reader(User):
    def __init__(self, name, bookName):
        self.name = name
        self.bookName = bookName

    def read(self):
        print(f'Recently, i have been focusing on reading {self.bookName} ')
# Creating attributes and functions for writer


class Writer(User):
    def __init__(self, name, bookName):
        self.name = name
        self.bookName = bookName

    def write(self):
        print(f'Recently, i have been focusing on writing {self.bookName}')
# Creating attributes and functions for speaker


class Speaker(User):
    def __init__(self, name, presentation):
        self.name = name
        self.presentation = presentation

    def speak(self):
        print(f'Today, i will be presenting {self.presentation} ')


Speaker1 = Speaker("Coolio", "How to sleep good")

print(isinstance(Speaker1, object))
