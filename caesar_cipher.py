def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Program ===")
    
    choice = input("Do you want to Encrypt or Decrypt? (E/D): ").strip().upper()
    
    if choice not in ['E', 'D']:
        print("Invalid choice. Please enter E or D.")
        return

    message = input("Enter your message: ")

    try:
        shift = int(input("Enter shift value (e.g., 3): "))
    except ValueError:
        print("Invalid shift value. Please enter a number.")
        return

    if choice == 'E':
        result = encrypt(message, shift)
        print("Encrypted message:", result)
    else:
        result = decrypt(message, shift)
        print("Decrypted message:", result)

if __name__ == "__main__":
    main()