# All readers,writers, and speakers are users
class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged_in')
# creating attributes and functions for Reader


class Reader(User):
    def __init__(self, name, bookName,email):
        super().__init__(email)
        self.name = name
        self.bookName = bookName

    def read(self):
        print(f'Recently, i have been focusing on reading {self.bookName} ')
# Creating attributes and functions for writer


class Writer(User):
    def __init__(self, name, bookName,email):
        super().__init__(email)
        self.name = name
        self.bookName = bookName

    def write(self):
        print(f'Recently, i have been focusing on writing {self.bookName}')
# Creating attributes and functions for speaker

    def project(self):
        print(f'{self.name}')


class Speaker(User):
    def __init__(self, name, presentation, email):
        super().__init__(email)
        self.name = name
        self.presentation = presentation

    def speak(self):
        print(f'Today, i will be presenting {self.presentation} ')

    def project(self):
        print(f'{self.name}')


def student_project(char):
    char.project()


# Speaker1 = Speaker("Coolio", "How to sleep good")
# Writer1 = Writer("Julio", "How to sleep good")
# student_project(Speaker1)
# for char in [Speaker1, Writer1]:
#     student_project(char)
# print(isinstance(Speaker1, object))
Writer1 = Writer("John", "How to Win in Monopoly","John.Smith@gmail.com")
Speaker1 = Speaker('George', "How to Speak in Public", 'george@gmail.com')
print(Speaker1.email)
