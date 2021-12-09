import hashlib
from binascii import unhexlify, hexlify

# Values are in Little Endian format
VERSION = "01000000"
PREV_HASH = "81cd02ab7e569e8bcd9317e2fe99f2de44d49ab2b8851ba4a308000000000000"
MERKLE_ROOT = "e320b6c2fffc8d750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122b"
TIMESTAMP = "c7f5d74d"
BITS = "f2b9441a"
NONCE = "42a14695"

header_hex = (
    VERSION +
    PREV_HASH +
    MERKLE_ROOT + 
    TIMESTAMP +
    BITS + 
    NONCE
 )

header_bin = unhexlify(header_hex)
hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
print(hexlify(hash).decode("utf-8"))
print(hexlify(hash[::-1]).decode("utf-8"))
