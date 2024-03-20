from main.models import Passwords
def run():
    password = Passwords.objects.get(id = 1)
    print(password)

