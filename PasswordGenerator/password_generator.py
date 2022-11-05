import random
import string

alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters+string.digits+"!@#$%^&*()")


def random_password_generator(pass_len=8, alp_count=4, digits_count=2, special_char_count=2):
    password = []
    ch_count = alp_count+digits_count+special_char_count
    for _ in range(alp_count):
        password.append(random.choice(alphabets))

    for _ in range(digits_count):
        password.append(random.choice(digits))

    for _ in range(special_char_count):
        password.append(random.choice(special_characters))

    if ch_count < pass_len:
        random.shuffle(characters)
        for _ in range(pass_len-ch_count):
            password.append(random.choice(characters))

    random.shuffle(password)

    return "".join(password)

