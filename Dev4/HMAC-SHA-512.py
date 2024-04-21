import hashlib
import hmac

def hmac_sha512(key, message):
    block_size = 128
    opad = bytes([0x5c] * block_size)
    ipad = bytes([0x36] * block_size)

    if len(key) > block_size:
        key = hashlib.sha512(key).digest()
    if len(key) < block_size:
        key += bytes(block_size - len(key))

    o_key_pad = bytes([x ^ y for x, y in zip(key, opad)])
    i_key_pad = bytes([x ^ y for x, y in zip(key, ipad)])

    inner_hash = hashlib.sha512(i_key_pad + message).digest()
    outer_hash = hashlib.sha512(o_key_pad + inner_hash).hexdigest()

    return outer_hash

# Example usage
message = b"This input string is being used to test my own implementation of HMAC-SHA-512."

key = b'Hello, world!'
result = hmac_sha512(key, message)
print("My implementation results: " +result)

#use hmac and hashlib to verify
h = hmac.new(key, message, hashlib.sha512)
print("Library results: "+ h.hexdigest())
if h.hexdigest() == result:
    print("Results match!")



