import itertools
import string
import multiprocessing
from time import time
# Character set: lowercase + uppercase letters
characters = string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
password_length = 3
target_password = "AAA"

def search(target_password, password_length):
    for i in range(1):
        attempt_count = 0
        for attempt in itertools.product(characters, repeat=password_length):
            attempt_count += 1
            attempt_password = ''.join(attempt)
            if attempt_password == target_password:
                # print(f"Password found after {attempt_count} attempts: {attempt_password}")
                break

start = time()
search(target_password, password_length)
finish = time()
elapsed = finish - start
print(f"Time elapsed: {elapsed:.4f} s")
