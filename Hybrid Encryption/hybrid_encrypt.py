import secrets
from Crypto.Cipher import DES3, AES
from Crypto import Random

output_file = 'encrypted.bin'


def encrypt(plaintext):
	try:
		key = secrets.token_bytes(16)
		iv = Random.new().read(DES3.block_size)
		cipher_encrypt = DES3.new(key, DES3.MODE_CFB, iv)
		encrypted_text = cipher_encrypt.encrypt(plaintext)
		cipher = AES.new(key, AES.MODE_EAX)
		nonce = cipher.nonce
		ciphertext, tag = cipher.encrypt_and_digest(encrypted_text)
		file_in = open(output_file, "wb")
		file_in.write(key)    #  16(fixed)
		file_in.write(iv)     #  8(fixed)
		file_in.write(nonce)  #  16(fixed)
		file_in.write(tag)    #  16(fixed)
		file_in.write(ciphertext)	
		file_in.close()

	except Exception as e:
		print(e)
	
	return ciphertext