import string
import random


def id_generator(size=10, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# print "moad_" + id_generator()
# print id_generator(3, "6793YUIO")


