import hashlib
import sys

def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

sha_signature = encrypt_string(sys.argv[1])
print(sha_signature)
