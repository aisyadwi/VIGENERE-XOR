
def encrypt(plaintext, key):
    ciphertext = ""
    key_stream = generate_key_stream(plaintext, key)
    
    for i in range(len(plaintext)):
        plaintext_char = plaintext[i]
        key_char = key_stream[i]
        cipher_char = str(ord(plaintext_char) ^ ord(key_char))
        ciphertext += cipher_char + " "
    
    return ciphertext.strip()

def decrypt(ciphertext, key):
    decrypted_text = ""
    key_stream = generate_key_stream(ciphertext, key)
    
    cipher_chars = ciphertext.split()
    
    for i in range(len(cipher_chars)):
        cipher_char = int(cipher_chars[i])
        key_char = ord(key_stream[i])
        decrypted_char = chr(cipher_char ^ key_char)
        decrypted_text += decrypted_char
    
    return decrypted_text

def generate_key_stream(text, key):
    key_stream = ""
    key_length = len(key)
    text_length = len(text)
    
    for i in range(text_length):
        key_stream += key[i % key_length]
    
    return key_stream

while True:
    print("\nMenu:")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Exit")
    
    choice = input("Pilih opsi (1/2/3): ")
    
    if choice == "1":
        plaintext = input("Masukkan plaintext: ")
        key = input("Masukkan kunci: ")
        encrypted_text = encrypt(plaintext, key)
        print("Teks Terenkripsi:", encrypted_text)
    elif choice == "2":
        ciphertext = input("Masukkan ciphertext: ")
        key = input("Masukkan kunci: ")
        decrypted_text = decrypt(ciphertext, key)
        print("Teks Terdekripsi:", decrypted_text)
    elif choice == "3":
        print("Program keluar. Terima kasih!")
        break
    else:
        print("Opsi tidak valid. Silakan masukkan angka 1, 2, atau 3.")
