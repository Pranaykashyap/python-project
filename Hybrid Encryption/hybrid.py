import hybrid_encrypt
import hybrid_decrypt
import time

plaintext = "Wireshark is the world's foremost and widely-used network protocol analyzer. It lets you see what's happening on your network at a microscopic level and is the de facto standard across many commercial and non-profit enterprises, government agencies, and educational institutions.".encode('utf-8')
start_time = time.time()
ciphertext = hybrid_encrypt.encrypt(plaintext)
print("\n ============================================= *** Ciphertext ***=============================================\n")
print(ciphertext)

decryptedtext = hybrid_decrypt.decrypt()
print("\n\n ============================================= *** Plaintext ***=============================================\n")
print(decryptedtext)

end_time = time.time()

print(end_time - start_time)

