def main():
    while True:
        print("Enter your choice:")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher(message, shift)
            print("Encrypted message:", encrypted_message)
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher(message, -shift)
            print("Decrypted message:", decrypted_message)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1 for encryption, 2 for decryption, or 3 to exit.")

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted_char = shift_character(char, shift)
            result += shifted_char
        else:
            result += char
    return result

def shift_character(char, shift):
    if char.isupper():
        return chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
    elif char.islower():
        return chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
    else:
        return char

if __name__ == "__main__":
    main()
