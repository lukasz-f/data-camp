import random
import string

print(''.join(random.choices(string.ascii_letters + string.digits + '!@_$%^&', k=10)))
