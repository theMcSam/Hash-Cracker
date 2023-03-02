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
   

def crack(hash, hashformat, wordlist):
    
    with open(wordlist, 'r', encoding="iso-8859-1") as dictfile:
        words = dictfile.readlines()

    
    for word in words:
        print(f"\rTrying --> {word.strip()}" + " "*(100-len(word)), end="")
        sys.stdout.flush()

        if hash != hashsum(hashformat,word):
            continue
        
        print("\n[+] Hash has been cracked.")
        print(f"[HASH] {hashformat} --> {hash} --> {word}", end="")
        break


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
    crack(hash, hashformat, wordlist)

