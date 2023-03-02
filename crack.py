import argparse
import hashlib

parser = argparse.ArgumentParser(prog="Hash Cracker v1.0",description="Hack cracker written in Python")

parser.add_argument("--format", type=str, help="Hash format")
parser.add_argument("--wordlist", type=str, help="Word list")
parser.add_argument("--hash", type=str, help="Hash to crack")

allowed_hash_formats = ["md5", "sha1", "sha256", "sha512"]

arguments = parser.parse_args()

hash, hashformat, wordlist = arguments.hash, arguments.format, arguments.wordlist

def crack(hash, hashformat, wordlist):
    if hashformat not in allowed_hash_formats:
        print("[!] Hash format not allowed.")

    with open(wordlist, 'r') as dictfile:
        words = dictfile.readlines()

    if hashformat == "md5":
        for word in words:
            if hash == md5sum(word):
                print("[+] Hash has been cracked.")
                print(f"[HASH] {hashformat} --> {hash}:{word}")
                break
            else:
                pass
    ...

def md5sum(password: str):
    return hashlib.md5(bytes(password, "utf8")).hexdigest()

crack(hash, hashformat, wordlist)


# print(arguments._get_args())