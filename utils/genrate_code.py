import random

def genrate_code(legnth=8):
    numbers='0123456789'
    code=''.join(random.choice(numbers) for x in range(legnth))
    return code