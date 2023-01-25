from nacl.public import SealedBox, PrivateKey

own_privkey = input('Own private key ')
own_privkey = PrivateKey(bytes.fromhex(own_privkey))

encrypted = input('Encrypted msg   ')

sealed_box = SealedBox(own_privkey)
plaintext = sealed_box.decrypt(bytes.fromhex(encrypted))
print('Decrypted msg  ', plaintext.decode('utf-8'))
