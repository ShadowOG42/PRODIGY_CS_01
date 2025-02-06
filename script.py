def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - shift_base) % 26 + shift_base)
        else:
            result += char  # Non-alphabet characters remain unchanged
    return result

def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift - shift_base) % 26 + shift_base)
        else:
            result += char
    return result

def main():
    print("Caesar Cipher Encryption/Decryption")
    action = input("Choose action (encrypt/decrypt): ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (integer): "))
    
    if action == "encrypt":
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif action == "decrypt":
        decrypted_message = decrypt(message, shift)  # Make sure decrypt is defined above this
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid action! Please choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
