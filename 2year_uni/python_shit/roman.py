import os
from multiprocessing import Pool
import hashlib
from time import time

# print(os.cpu_count())
testpass = 'ACCCCC'
# hidden_hash = "abd90779cc179a42b911cae0d2d9bc52fe7130b9c928ecb1d4f4d7158cd4ec93"
hidden_hash = 'fd6e6f66c91b9324cbf4e61d1c6baf94e6e71d5585569229346450dd0b073a12'
pswd_len = 6

uppChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowChar = "abcdefghijklmnopqrstuvwxyz"
numChar = "0123456789"
spcChar = "!@#$%^&*_-"

pswd_pool = uppChar + numChar + spcChar

password = []

for i in range(pswd_len):
    password.append(0)

def generate_pswd():
    global password
    global pswd_len
    global pswd_pool
    temp = ""

    for i in range(pswd_len):
        temp += pswd_pool[password[i]]
        if i > 0 and password[i] >= len(pswd_pool) -1:
            password[i-1] += 1
            password[i] = 0
        elif i == pswd_len-1:
            password[i] +=1
    return temp


def check(temp):
    global hidden_hash
    test_hash_obj = hashlib.sha256(temp.encode('utf-8'))
    digest = test_hash_obj.hexdigest()
    if digest == hidden_hash:
        return True
    else:
        return False


if __name__ == '__main__':
    pool = Pool(processes=16)
    start = time()
    while True:
        pswd_line = []
        for i in range(4000): pswd_line.append(generate_pswd())
        # print(pswd_line)
        result = pool.map(check, pswd_line)
        # print(result)
        if True in result:
            print('password found')
            break
    finish = time()
    elapsed = finish - start
    print(f"Time elapsed: {elapsed:.4f} s")
    
    # test_hash_obj = hashlib.sha256(testpass.encode('utf-8'))
    # digest = test_hash_obj.hexdigest()
    # print(digest)