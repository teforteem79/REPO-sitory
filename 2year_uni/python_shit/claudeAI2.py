import os
import hashlib
import multiprocessing
from multiprocessing import Pool, Manager
from time import time
# targetHash6 = 'ca451287a87b2163cf8bcd63a4a46bd3c9ff7638f0e3a1f81e4ef9ca9c0ed8fef7150ffa06c0436e89a6c668d2c5a7183015627601bb8baefd6a49ba05ab5daf' #blake2b accccc
# targetHash6 = '6f0874bd7ba418106ac15555ea927aef34bc05c8ba92cd2e4c3065e7751ccc125fd88f19eec18f007e9f033c8dd2749edf573ac8aeec47d073f5832553fcea9c' #blake2b
targetHash6 = '1cb355866d2b0fb1b9474b745c7879e67ebe1df742639d3a229c9a1bc9c316d0014ca785474bef5d4c1bd7048a41edc69b8b29232edf64cb2144c3de3cf3e43b' # 000010
targetHash7 = 'your_sha224_hash_here'  # Add your target here
uppChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowChar = "abcdefghijklmnopqrstuvwxyz"
numChar = "0123456789"
spcChar = "!@#$%^&*_-"
# char6 = lowChar + numChar + spcChar
char6 = numChar + lowChar
test_password2 = '900000' 
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
                            
                            # Progress update every 1M tries per process
                            if tries % 1_000_000 == 0:
                                print(f"Process {start_i}-{end_i}: {tries} tries, current: {temp_pass}")
                            
                            if digest == targetHash6:
                                return temp_pass  # Found the password!
        
    return None  # Not found in this range

def findPassSixthMultiprocess():
    start = time()
    
    # Split the work by dividing the first character range among processes
    num_processes = 8
    chars_per_process = len(char6) // num_processes
    
    # Create ranges for each process
    ranges = []
    for p in range(num_processes):
        start_i = p * chars_per_process
        if p == num_processes - 1:  # Last process gets any remaining chars
            end_i = len(char6)
        else:
            end_i = (p + 1) * chars_per_process
        ranges.append((start_i, end_i))
    
    print(f"Using {num_processes} processes")
    print(f"Character ranges: {ranges}")
    
    # Start the multiprocessing
    with Pool(processes=num_processes) as pool:
        results = pool.map(worker_process, ranges)
    
    # Check results
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


# Your original functions (unchanged)
def findPassSeventh():
    found = False
    start = time()
    tries = 0
    for i in range(len(char6)):
        for j in range(len(char6)):
            for k in range(len(char6)):
                for l in range(len(char6)):
                    for m in range(len(char6)):
                        temp_pass = char6[i] + char6[j] + char6[k] + char6[l] + char6[m]
                        temp_hash_obj = hashlib.sha224(temp_pass.encode('utf-8'))
                        digest = temp_hash_obj.hexdigest()
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
    print(f"CPU cores available: {multiprocessing.cpu_count()}")
    
    test_hash_obj = hashlib.blake2b(test_password2.encode('utf-8'))
    digest = test_hash_obj.hexdigest()
    if digest == targetHash6:
        print(f"The password {test_password2} matches with its hash!")

    print(digest)

    # Test with multiprocessing
    print("Running with multiprocessing:")
    findPassSixthMultiprocess()
    
    # Uncomment to compare with single-threaded
    # print("\nRunning single-threaded:")
    # findPassSixth()