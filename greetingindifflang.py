
class English:

    def greeting(self):
        print('Hello')


class French:

    def greeting(self):
        print('Bonjour')


def greet(language):
    language.greeting()

print('Greeting in english then french:-')
e = English()
greet(e)
f= French()
greet(f)
