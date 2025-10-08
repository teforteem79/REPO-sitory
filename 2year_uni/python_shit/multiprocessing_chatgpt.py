import os
import hashlib
import multiprocessing as mp
from multiprocessing import Pool, Manager, Value
from time import time
import itertools
import sys

# Target hashes
targetHash6 = '6f0874bd7ba418106ac15555ea927aef34bc05c8ba92cd2e4c3065e7751ccc125fd88f19eec18f007e9f033c8dd2749edf573ac8aeec47d073f5832553fcea9c'  # blake2b

# Character sets
uppChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowChar = "abcdefghijklmnopqrstuvwxyz"
numChar = "0123456789"
spcChar = "!@#$%^&*_-"
char6 = lowChar + numChar + spcChar

def worker_process(args):
    """
    Worker function that processes a chunk of password combinations.
    Returns (found, password, tries) tuple.
    """
    start_idx, end_idx, charset, password_length, target_hash, hash_algorithm = args
    
    base = len(charset)
    tries = 0
    
    for i in range(start_idx, end_idx):
        # Convert index to password combination
        password_chars = []
        temp = i
        for _ in range(password_length):
            password_chars.append(charset[temp % base])
            temp //= base
        
        password = ''.join(reversed(password_chars))
        
        # Hash the password
        if hash_algorithm == 'blake2b':
            hash_obj = hashlib.blake2b(password.encode('utf-8'))
        elif hash_algorithm == 'sha224':
            hash_obj = hashlib.sha224(password.encode('utf-8'))
        else:
            raise ValueError(f"Unsupported hash algorithm: {hash_algorithm}")
        
        digest = hash_obj.hexdigest()
        tries += 1
        
        if digest == target_hash:
            return (True, password, tries)
    
    return (False, None, tries)

def create_chunks(total_combinations, num_processes, chunk_size=None):
    """
    Create work chunks for multiprocessing.
    """
    if chunk_size is None:
        chunk_size = max(total_combinations // (num_processes * 4), 10000)
    
    chunks = []
    for start in range(0, total_combinations, chunk_size):
        end = min(start + chunk_size, total_combinations)
        chunks.append((start, end))
    
    return chunks

def multiprocess_crack(charset, password_length, target_hash, hash_algorithm, num_processes=8):
    """
    Multiprocessing password cracker.
    """
    if num_processes is None:
        num_processes = mp.cpu_count()
    
    total_combinations = len(charset) ** password_length
    
    print(f"Multiprocessing Hash Cracker")
    print(f"=" * 50)
    print(f"Character set: {charset}")
    print(f"Password length: {password_length}")
    print(f"Total combinations: {total_combinations:,}")
    print(f"Hash algorithm: {hash_algorithm}")
    print(f"Using {num_processes} processes")
    print(f"Target hash: {target_hash}")
    print("=" * 50)
    
    # Create work chunks
    chunks = create_chunks(total_combinations, num_processes)
    print(f"Created {len(chunks)} work chunks")
    
    # Prepare arguments for worker processes
    worker_args = [
        (start, end, charset, password_length, target_hash, hash_algorithm)
        for start, end in chunks
    ]
    
    start_time = time()
    total_tries = 0
    found = False
    found_password = None
    
    try:
        with Pool(processes=num_processes) as pool:
            print("Starting parallel processing...")
            
            # Process chunks and check results
            for i, result in enumerate(pool.imap(worker_process, worker_args)):
                found_flag, password, tries = result
                total_tries += tries
                
                # Progress update
                if i % max(1, len(chunks) // 20) == 0:
                    progress = (i + 1) / len(chunks) * 100
                    elapsed = time() - start_time
                    rate = total_tries / elapsed if elapsed > 0 else 0
                    print(f"Progress: {progress:.1f}% - {total_tries:,} tries - {rate:,.0f} tries/sec")
                
                if found_flag:
                    found = True
                    found_password = password
                    print(f"\n🎉 PASSWORD FOUND: {password}")
                    print(f"Found in {total_tries:,} tries!")
                    break
    
    except KeyboardInterrupt:
        print("\n⚠️  Process interrupted by user")
        pool.terminate()
        pool.join()
        return None
    
    end_time = time()
    elapsed = end_time - start_time
    
    print(f"\n" + "=" * 50)
    if found:
        print(f"✅ SUCCESS!")
        print(f"Password: {found_password}")
        print(f"Total tries: {total_tries:,}")
    else:
        print(f"❌ Password not found in search space")
        print(f"Total tries: {total_tries:,}")
    
    print(f"Time elapsed: {elapsed:.4f} seconds")
    if elapsed > 0:
        print(f"Average rate: {total_tries / elapsed:,.0f} tries/second")
    
    return found_password if found else None

def single_threaded_crack(charset, password_length, target_hash, hash_algorithm):
    """
    Original single-threaded approach for comparison.
    """
    print(f"Single-threaded Hash Cracker")
    print(f"=" * 50)
    
    start_time = time()
    tries = 0
    found = False
    
    # Generate all combinations
    for combination in itertools.product(charset, repeat=password_length):
        password = ''.join(combination)
        
        # Hash the password
        if hash_algorithm == 'blake2b':
            hash_obj = hashlib.blake2b(password.encode('utf-8'))
        elif hash_algorithm == 'sha224':
            hash_obj = hashlib.sha224(password.encode('utf-8'))
        
        digest = hash_obj.hexdigest()
        tries += 1
        
        # Progress update
        if tries % 1_000_000 == 0:
            elapsed = time() - start_time
            rate = tries / elapsed if elapsed > 0 else 0
            print(f"{tries:,} tries made, rate: {rate:,.0f}/sec, current: {password}")
        
        if digest == target_hash:
            print(f"Password {password} found in {tries:,} tries!")
            found = True
            break
    
    end_time = time()
    elapsed = end_time - start_time
    print(f"Time elapsed: {elapsed:.4f} seconds")
    
    return password if found else None

def benchmark_comparison(charset, password_length, target_hash, hash_algorithm, sample_size=1000000):
    """
    Compare single-threaded vs multiprocessing performance on a sample.
    """
    print(f"Performance Benchmark ({sample_size:,} combinations)")
    print(f"=" * 50)
    
    # Single-threaded benchmark
    print("Single-threaded performance:")
    start_time = time()
    tries = 0
    
    for combination in itertools.product(charset, repeat=password_length):
        password = ''.join(combination)
        if hash_algorithm == 'blake2b':
            hash_obj = hashlib.blake2b(password.encode('utf-8'))
        elif hash_algorithm == 'sha224':
            hash_obj = hashlib.sha224(password.encode('utf-8'))
        digest = hash_obj.hexdigest()
        tries += 1
        if tries >= sample_size:
            break
    
    single_time = time() - start_time
    single_rate = tries / single_time
    print(f"Rate: {single_rate:,.0f} hashes/second")
    
    # Multiprocessing benchmark
    print("Multiprocessing performance:")
    chunks = create_chunks(sample_size, mp.cpu_count())
    worker_args = [
        (start, min(end, sample_size), charset, password_length, "dummy_hash", hash_algorithm)
        for start, end in chunks[:mp.cpu_count()]  # Limit for benchmark
    ]
    
    start_time = time()
    with Pool() as pool:
        results = pool.map(worker_process, worker_args)
    
    multi_time = time() - start_time
    multi_tries = sum(result[2] for result in results)
    multi_rate = multi_tries / multi_time if multi_time > 0 else 0
    
    print(f"Rate: {multi_rate:,.0f} hashes/second")
    
    if single_time > 0 and multi_time > 0:
        speedup = multi_rate / single_rate
        print(f"Speedup: {speedup:.2f}x")

if __name__ == "__main__":
    print("Hash Cracking with Multiprocessing")
    print("=" * 50)
    
    # Example usage for 6-character passwords
    print("Example: Cracking 6-character password (blake2b)")
    
    # First, run a performance benchmark
    benchmark_comparison(char6, 6, targetHash6, 'blake2b', sample_size=100000)
    
    print(f"\nReady to crack? Total search space: {len(char6)**6:,} combinations")
    print("This could take a while even with multiprocessing!")
    
    # Uncomment to run the actual crack
    result = multiprocess_crack(char6, 6, targetHash6, 'blake2b')
    # result = single_threaded_crack(char6, 6, targetHash6, 'blake2b')
    # For testing with smaller search space (4 characters):
    print(f"\nFor testing - 4 character search space: {len(char6)**4:,} combinations")
    # result = multiprocess_crack(char6, 4, "test_hash_here", 'blake2b')
    
    print(f"\nSystem info:")
    print(f"CPU cores: {mp.cpu_count()}")
    print(f"Estimated speedup: {mp.cpu_count()}x (theoretical maximum)")