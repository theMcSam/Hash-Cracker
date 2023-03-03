import argparse
import hashlib
import multiprocessing
import sys

def get_args():
    parser = argparse.ArgumentParser(prog="Hash Cracker v1.0",description="Hack cracker written in Python")

    parser.add_argument("--format", type=str, help="Hash format")
    parser.add_argument("--wordlist", type=str, help="Word list")
    parser.add_argument("--hash", type=str, help="Hash to crack")

    return parser.parse_args()
   

def crack_word_chunks(chunk: list, hash: str, hashformat: str, result_queue):
    for word in chunk:
        if len(word.strip()) <= 30: 
            print(f"\r[+] Trying --> {word.strip()}"+" "*(80-len(word)), end="")

        if hash == hashsum(hashformat, word):
            return result_queue.put((True, word))

        result_queue.put((False, None))
    

def crack(hash: str, hashformat: str, wordlist: str):
    
    try:
        result_queue = multiprocessing.Queue()

        with open(wordlist, 'r', encoding="ISO-8859-1") as dictfile:
            words = dictfile.readlines()

        num_of_cores = multiprocessing.cpu_count()

        chunk_size = len(words) // num_of_cores

        chunks = [words[i:i+chunk_size] for i in range(0, len(words), chunk_size)]

        processes = []

        for chunk in chunks:
            process = multiprocessing.Process(target=crack_word_chunks, \
                                            args=(chunk, hash, hashformat, result_queue))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        while not result_queue.empty():
            result = result_queue.get()
            if result[0]:
                print("\n[+] Hash has been cracked.")
                print(f"[HASH] {hashformat} --> {hash} --> {result[1]}", end="")
                break
            
    except KeyboardInterrupt:
        print("[-] CTRL-C detected, exiting...")
        sys.exit()
        

def hashsum(hashformat:str, password: str):

    hashfunctions = {
        'md5' : hashlib.md5,
        'sha1' : hashlib.sha1,
        'sha256' : hashlib.sha256
    }

    if  hashformat in hashfunctions:
        return hashfunctions[hashformat](password.encode("utf8")).hexdigest()
    
    print("[+] Hash not supported")

if __name__ == "__main__":
    arguments = get_args()
    hash, hashformat, wordlist = arguments.hash, arguments.format, arguments.wordlist
    try:
        crack(hash, hashformat, wordlist)
    except KeyboardInterrupt:
        sys.exit("[-] CTRL-C detected, exiting...")

