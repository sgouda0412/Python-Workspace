import random
import string
from collections import (
    Counter,
    OrderedDict,
    defaultdict,
    UserDict,
    UserList,
    UserString,
    deque,
    namedtuple,
)


def password_gen(length=12):
    character = string.ascii_letters + string.punctuation + string.digits

    return "".join(random.choice(character) for i in range(length))


if __name__ == "__main__":
    print(password_gen())
