from nacl.public import Box, PrivateKey, PublicKey


own_privkey = input('Own private key   ')
own_privkey = PrivateKey(bytes.fromhex(own_privkey))

receiver_address = input('Recipient address ')
receiver_address = PublicKey(bytes.fromhex(receiver_address))

plaintext_msg = input('Cleartext msg     ')
plaintext_msg = plaintext_msg.encode('utf-8')

secret_box = Box(own_privkey, receiver_address)
encrypted = secret_box.encrypt(plaintext_msg)
print('Encrypted msg    ', encrypted.hex())
