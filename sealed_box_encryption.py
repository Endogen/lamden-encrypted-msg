from lamden.crypto import wallet
from nacl.public import SealedBox

# SENDER
walletReceiver = wallet.Wallet()
walletSender = wallet.Wallet()

# RECEIVER
receiverPrivateKey = walletReceiver.sk.to_curve25519_private_key()
receiverPublicKey = receiverPrivateKey.public_key

message = input('Cleartext msg ').encode()

# ENCRYPT
sealed_box = SealedBox(receiverPublicKey)
encrypted = sealed_box.encrypt(message)

# DECRYPT
unseal_box = SealedBox(receiverPrivateKey)
plaintext = unseal_box.decrypt(encrypted)
print('Decoded msg', plaintext.decode('utf-8'))
