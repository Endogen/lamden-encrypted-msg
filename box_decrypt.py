from nacl.public import Box, PrivateKey, PublicKey


own_privkey = input('Own private key ')
own_privkey = PrivateKey(bytes.fromhex(own_privkey))

sender_address = input('Sender address  ')
sender_address = PublicKey(bytes.fromhex(sender_address))

encrypted_msg = input('Encrypted msg   ')

secret_box = Box(own_privkey, sender_address)
decrypted = secret_box.decrypt(bytes.fromhex(encrypted_msg))
print('Decrypted msg  ', decrypted.decode('utf-8'))
