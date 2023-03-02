import argparse

parser = argparse.ArgumentParser("Hash Cracker v1.0",description="Hack cracker written in Python")

parser.add_argument("--format", type=str, help="Hash format")
parser.add_argument("--wordlist", type=str, help="Word list")
parser.add_argument("--file", type=str, help="File containing hashes")

arguments = parser.parse_args()

print(arguments)