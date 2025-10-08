import os
import hashlib
import multiprocessing
from multiprocessing import Pool
from time import time

# print(multiprocessing.cpu_count())
# print(os.cpu_count())

targetHash7 = '090ec244dc136b692f252ea2409b9c499794f2db7b37da089dcc9b8a' #sha224
# targetHash6 = '6f0874bd7ba418106ac15555ea927aef34bc05c8ba92cd2e4c3065e7751ccc125fd88f19eec18f007e9f033c8dd2749edf573ac8aeec47d073f5832553fcea9c' #blake2b
targetHash5 = '713417394e2b74aee7fa54d09375b0c78d288a90eba27a560cfc698c5b54886c' #blake2s
targetHash6 = 'ca451287a87b2163cf8bcd63a4a46bd3c9ff7638f0e3a1f81e4ef9ca9c0ed8fef7150ffa06c0436e89a6c668d2c5a7183015627601bb8baefd6a49ba05ab5daf' #blake2b accccc
uppChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowChar = "abcdefghijklmnopqrstuvwxyz"
numChar = "0123456789"
spcChar = "!@#$%^&*_-"
char = lowChar + uppChar
char6 = lowChar + numChar + spcChar
found = False
test_password = '*e5-qp'
test_password2 = 'accccc'

def worker_process(i_range):
    """Worker process that handles one range of the first character"""
    tries = 0
    start_i, end_i = i_range
    
    for i in range(start_i, end_i):
        for j in range(len(char6)):
            for k in range(len(char6)):
                for l in range(len(char6)):
                    for m in range(len(char6)):
                        for n in range(len(char6)):
                            temp_pass = char6[i] + char6[j] + char6[k] + char6[l] + char6[m] + char6[n]
                            temp_hash_obj = hashlib.blake2b(temp_pass.encode('utf-8'))
                            digest = temp_hash_obj.hexdigest() 
                            tries += 1
                            
                        
                            if tries % 1_000_000 == 0:
                                print(f"Process {start_i}-{end_i}: {tries} tries, current: {temp_pass}")
                            
                            if digest == targetHash6:
                                return temp_pass
        
    return None

def findPassSixthMultiprocess():
    start = time()
    
    num_processes = 4
    chars_per_process = len(char6) // num_processes
    
    
    ranges = []
    for p in range(num_processes):
        start_i = p * chars_per_process
        if p == num_processes - 1:
            end_i = len(char6)
        else:
            end_i = (p + 1) * chars_per_process
        ranges.append((start_i, end_i))
    
    print(f"Using {num_processes} processes")
    print(f"Character ranges: {ranges}")
    
    
    with Pool(processes=num_processes) as pool:
        results = pool.map(worker_process, ranges)
    
    
    found_password = None
    for result in results:
        if result is not None:
            found_password = result
            break
    
    finish = time()
    elapsed = finish - start
    
    if found_password:
        print(f"Password {found_password} found!")
    else:
        print("Password not found in search space")
    
    print(f"Time elapsed: {elapsed:.4f} s")
    return found_password


def findPassSeventh():
    found = False
    start = time()
    tries = 0
    for i in range(len(char)):
        for j in range(len(char)):
            for k in range(len(char)):
                for l in range(len(char)):
                    for m in range(len(char)):
                        temp_pass = char[i] + char[j] + char[k] + char[l] + char[m]
                        temp_hash_obj = hashlib.sha224(temp_pass.encode('utf-8'))
                        digest = temp_hash_obj.hexdigest()
                        # print(char[i] + char[j] + char[k])
                        tries += 1
                        if digest == targetHash7:
                            print(f"password {temp_pass} found in {tries} tries!")
                            found = True
                            break
                    if found == True:
                        break
                if found == True:
                    break
            if found == True:
                    break
        if found == True:
                    break
    finish = time()
    elapsed = finish - start
    print(f"Time elapsed: {elapsed:.4f} s")

def findPassSixth():
    found = False
    start = time()
    tries = 0
    for i in range(len(char6)):
        for j in range(len(char6)):
            for k in range(len(char6)):
                for l in range(len(char6)):
                    for m in range(len(char6)):
                        for n in range(len(char6)):
                            temp_pass = char6[i] + char6[j] + char6[k] + char6[l] + char6[m] + char6[n]
                            temp_hash_obj = hashlib.blake2b(temp_pass.encode('utf-8'))
                            digest = temp_hash_obj.hexdigest()
                            tries += 1

                            # Progress update every 1M tries
                            if tries % 1_000_000 == 0:
                                print(f"{tries:,} tries made, current attempt: {temp_pass}")

                            if digest == targetHash6:
                                print(f"Password {temp_pass} found in {tries:,} tries!")
                                found = True
                                break
                        if found: break
                    if found: break
                if found: break
            if found: break
        if found: break
    finish = time()
    elapsed = finish - start
    print(f"Time elapsed: {elapsed:.4f} s")

if __name__ == "__main__":
    # findPassSixth()
    findPassSixthMultiprocess()
    # test_hash_obj = hashlib.blake2b(test_password2.encode('utf-8'))
    # digest = test_hash_obj.hexdigest()
    # if digest == targetHash6:
    #      print(f"The password {test_password2} matches with its hash!")

    # print(digest)
