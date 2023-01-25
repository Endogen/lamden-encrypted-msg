from nacl.public import SealedBox, PublicKey

receiver_address = input('Recipient address ')
receiver_address = PublicKey(bytes.fromhex(receiver_address))

plaintext_msg = input('Cleartext msg     ')
plaintext_msg = plaintext_msg.encode('utf-8')

sealed_box = SealedBox(receiver_address)
encrypted = sealed_box.encrypt(plaintext_msg)
print('Encrypted msg    ', encrypted.hex())
