import secrets

from nacl.public import Box, PrivateKey


# BOB's SEED
seed_bob = secrets.token_bytes(32)
# BOB's PRIVATE KEY
privkey_bob = PrivateKey(seed_bob)
print('Privkey Bob  ', privkey_bob.encode().hex())
# BOB's PUBLIC KEY
address_bob = privkey_bob.public_key
print('Address Bob  ', address_bob.encode().hex())

# ALICE's SEED
seed_alice = secrets.token_bytes(32)
# ALICE's PRIVATE KEY
privkey_alice = PrivateKey(seed_alice)
print('Privkey Alice', privkey_alice.encode().hex())
# ALICE's PUBLIC KEY
address_alice = privkey_alice.public_key
print('Address Alice', address_alice.encode().hex())

message = input('Cleartext msg ').encode()

# ENCRYPT
bob_box = Box(privkey_bob, address_alice)
encrypted = bob_box.encrypt(message)
encrypted_result = encrypted.hex()
print('Encrypted msg', encrypted_result)

# DECRYPT
alice_box = Box(privkey_alice, address_bob)
decrypted = alice_box.decrypt(bytes.fromhex(encrypted_result))
print('Decrypted msg', decrypted.decode('utf-8'))
