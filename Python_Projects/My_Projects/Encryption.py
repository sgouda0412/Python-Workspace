import onetimepad

input_msg = input("Please enter a message to be encrypted: ")
input_key = input("Please enter a key: ")
cipher = onetimepad.encrypt(input_msg, input_key)
print(f"Here is your Encrypted message: {cipher}")
decrypted_msg = onetimepad.decrypt(cipher, input_key)
print(f"Your Message is: {decrypted_msg}")
