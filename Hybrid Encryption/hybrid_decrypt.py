from Crypto.Cipher import DES3, AES

input_file = 'encrypted.bin'

file_in = open(input_file, 'rb')
key = file_in.read(16)
iv = file_in.read(8)
nonce = file_in.read(16)
tag = file_in.read(16)
ciphered_data = file_in.read()
file_in.close()


def decrypt():
	cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
	des_plaintext = cipher.decrypt(ciphered_data)
	try:
		cipher.verify(tag)
		cipher_decrypt = DES3.new(key, DES3.MODE_CFB, iv)
		plaintext = cipher_decrypt.decrypt(des_plaintext)

		return plaintext
  
	except ValueError:
		print("Key incorrect or message corrupted")