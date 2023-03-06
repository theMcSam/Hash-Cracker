## Simple implementation of a hash cracking tool written in Python
---
### Installation
1. Clone the repository. <br>
Command: `git clone https://github.com/theMcSam/hash_cracker.git`
2. Change your working directory to the hash_cracker directory.<br>
Command: `cd hash_cracker`

### Usage
Cracking hashes.<br>
Command: `python crack.py --format <hashfomat> --hash <hash> --wordlist <wordlist>`

Example: `python crack.py --format md5 --hash 0716a5cea0577995508b18acd9a590bd`

Hashing types or formats currently supported:
1. md5 
2. sha1
3. sha256
