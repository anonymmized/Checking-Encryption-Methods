import re
from collections import Counter
import base64
import codecs

def check_caesar_cipher(text):
    if not text.isascii():
        return False
    
    freq = Counter(text.lower())
    common_letters = 'etaoinshrdlu'  
    text_common = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    

    if len(text_common) < 3:
        return False
    
    return True

def check_base64(text):

    base64_pattern = '^[A-Za-z0-9+/]*={0,2}$'
    if re.match(base64_pattern, text) and len(text) % 4 == 0:
        return True
    return False

def check_hex(text):

    hex_pattern = '^[0-9A-Fa-f]+$'
    if re.match(hex_pattern, text):
        return True
    return False

def check_binary(text):

    binary_pattern = '^[01]+$'
    if re.match(binary_pattern, text) and len(text) % 8 == 0:
        return True
    return False

def check_morse(text):

    morse_pattern = '^[.\- ]+$'
    if re.match(morse_pattern, text):
        return True
    return False

def check_rot13(text):
    
    if not text.isascii():
        return False
    

    rot13_common = {'n': 'a', 'g': 't', 'h': 'u', 'v': 'i'}
    matches = 0
    text = text.lower()
    
    for rot, orig in rot13_common.items():
        if rot in text and orig in text:
            matches += 1
    
    return matches >= 2

def identify_encryption(text):
    possible_methods = []
    
    if check_base64(text):
        possible_methods.append("Base64")
    
    if check_hex(text):
        possible_methods.append("HEX")
    
    if check_binary(text):
        possible_methods.append("Binary")
    
    if check_morse(text):
        possible_methods.append("Morse Code")
    
    if check_caesar_cipher(text):
        possible_methods.append("Caesar Cipher")
    
    if check_rot13(text):
        possible_methods.append("ROT13")
    
    return possible_methods

def decrypt_base64(text):
    try:
        decoded = base64.b64decode(text).decode('utf-8')
        return decoded
    except:
        return None

def decrypt_hex(text):
    try:
        bytes_object = bytes.fromhex(text)
        decoded = bytes_object.decode('utf-8')
        return decoded
    except:
        return None

def decrypt_binary(text):
    try:
        binary_values = [text[i:i+8] for i in range(0, len(text), 8)]
        decoded = ''.join([chr(int(binary, 2)) for binary in binary_values])
        return decoded
    except:
        return None

def decrypt_morse(text):
    morse_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
        '...--': '3', '....-': '4', '.....': '5', '-....': '6',
        '--...': '7', '---..': '8', '----.': '9', ' ': ' '
    }
    try:
        words = text.split('  ')
        decoded = ''
        for word in words:
            letters = word.split()
            for letter in letters:
                decoded += morse_dict.get(letter, '')
            decoded += ' '
        return decoded.strip()
    except:
        return None

def decrypt_caesar(text, shift=None):
    if not shift:
        possible_results = []
        for shift in range(1, 26):
            result = ''
            for char in text:
                if char.isalpha():
                    ascii_offset = ord('A') if char.isupper() else ord('a')
                    result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                else:
                    result += char
            possible_results.append(result)
        return possible_results
    else:
        result = ''
        for char in text:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            else:
                result += char
        return result

def decrypt_rot13(text):
    try:
        return codecs.decode(text, 'rot_13')
    except:
        return None

def try_decrypt(text, method):
    print(f"\nAttempting to decrypt using {method}:")
    
    if method == "Base64":
        result = decrypt_base64(text)
        if result:
            print(f"Result: {result}")
            return True
    
    elif method == "HEX":
        result = decrypt_hex(text)
        if result:
            print(f"Result: {result}")
            return True
    
    elif method == "Binary":
        result = decrypt_binary(text)
        if result:
            print(f"Result: {result}")
            return True
    
    elif method == "Morse Code":
        result = decrypt_morse(text)
        if result:
            print(f"Result: {result}")
            return True
    
    elif method == "Caesar Cipher":
        results = decrypt_caesar(text)
        print("Possible variants:")
        for i, result in enumerate(results, 1):
            print(f"Shift {i}: {result}")
        return True
    
    elif method == "ROT13":
        result = decrypt_rot13(text)
        if result:
            print(f"Result: {result}")
            return True
    
    print("Failed to decrypt using this method")
    return False

def main():
    print("Enter encrypted string:")
    encrypted_text = input().strip()
    
    if not encrypted_text:
        print("Error: empty string")
        return
    
    methods = identify_encryption(encrypted_text)
    
    if methods:
        print("\nPossible encryption methods:")
        for method in methods:
            print(f"- {method}")
            
        print("\nAttempting decryption...")
        for method in methods:
            try_decrypt(encrypted_text, method)
    else:
        print("\nCould not identify encryption method or text is not encrypted")

if __name__ == "__main__":
    main()
