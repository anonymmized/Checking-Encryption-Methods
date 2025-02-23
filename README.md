# Checking-Encryption-Methods

A Python tool that identifies and attempts to decrypt text using various encryption methods.

## Features

The program can detect and decrypt the following encryption methods:
- Base64
- Hexadecimal (HEX)
- Binary
- Morse Code
- Caesar Cipher
- ROT13

## Requirements

- Python 3.6 or higher
- Required Python packages:
  - `re`
  - `collections`
  - `base64`
  - `codecs`

All required packages are included in Python's standard library, so no additional installation is needed.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/anonymmized/Checking-Encryption-Methods.git
cd Checking-Encryption-Methods
```

2. Run the program:
```bash
python main.py
```

## Usage

1. Run the program
2. Enter your encrypted text when prompted
3. The program will:
   - Identify possible encryption methods
   - Attempt to decrypt the text using each identified method
   - Display the results

## Examples

### Base64 Example
```projects/Checking-Encryption-Methods/README.md
Enter encrypted string:
SGVsbG8gV29ybGQ=

Possible encryption methods:
- Base64

Attempting decryption...
Attempting to decrypt using Base64:
Result: Hello World
```

### ROT13 Example
```
Enter encrypted string:
Uryyb Jbeyq

Possible encryption methods:
- ROT13
- Caesar Cipher

Attempting decryption...
Attempting to decrypt using ROT13:
Result: Hello World

Attempting to decrypt using Caesar Cipher:
Possible variants:
Shift 1: Tqxxn Vnqxc
...
Shift 13: Hello World
...
```

### Morse Code Example
```projects/Checking-Encryption-Methods/README.md
Enter encrypted string:
.... . .-.. .-.. ---

Possible encryption methods:
- Morse Code

Attempting decryption...
Attempting to decrypt using Morse Code:
Result: HELLO
```

## Supported Encryption Methods Details

### Base64
- Detects standard Base64 encoded strings
- Checks for valid Base64 characters and padding

### Hexadecimal (HEX)
- Identifies hexadecimal strings
- Supports both uppercase and lowercase hex values

### Binary
- Detects binary strings (0s and 1s)
- Validates 8-bit grouping

### Morse Code
- Recognizes dots, dashes, and spaces
- Supports letters, numbers, and basic punctuation

### Caesar Cipher
- Attempts all possible shift values (1-25)
- Shows all possible decryption results

### ROT13
- Special case of Caesar Cipher with 13-character shift
- Detects common ROT13 patterns

## Limitations

- The program may identify multiple possible encryption methods for the same input
- Some encrypted texts might not be recognized if they don't match the expected patterns
- The Caesar Cipher detection might give false positives for regular text
- Only supports ASCII characters for certain encryption methods

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.
