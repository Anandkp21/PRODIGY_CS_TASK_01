
---
# Caesar Cipher Tool

A simple command-line tool for encrypting and decrypting messages using the Caesar cipher technique.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)

## Overview

The Caesar Cipher Tool allows users to encrypt and decrypt messages using a Caesar cipher. This cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Features

- **Encryption:** Convert plain text to cipher text by shifting characters by a specified value.
- **Decryption:** Convert cipher text back to plain text by reversing the shift.
- **User-friendly Interface:** Simple menu-driven command-line interface.

## Installation

To run this project, you need to have Python installed on your machine. Follow the steps below to set up the project:

1. **Clone the repository:**
   ```sh
   git clone [https://github.com/yourusername/caesar-cipher-tool.git](https://github.com/Anandkp21/PRODIGY_CS_TASK_01.git)
   ```
   
2. **Navigate to the project directory:**
   ```sh
   cd caesar-cipher-tool
   ```
   
3. **Run the tool:**
   ```sh
   python caesar_cipher_tool.py
   ```

## Usage

1. **Run the tool:**
   ```sh
   python caesar_cipher_tool.py
   ```

2. **Choose an option from the menu:**
   - Enter `1` for encryption.
   - Enter `2` for decryption.
   - Enter `3` to exit the tool.

3. **Follow the prompts:**
   - For encryption, enter the message and shift value.
   - For decryption, enter the cipher text and shift value.

## Example

### Encryption
```
Menu:
1. Encryption
2. Decryption
3. Exit
Enter your choice (1, 2, or 3): 1
Enter the message to encrypt: hello
Enter the shift value: 3
Encrypted message: khoor
```

### Decryption
```
Menu:
1. Encryption
2. Decryption
3. Exit
Enter your choice (1, 2, or 3): 2
Enter the message to decrypt: khoor
Enter the shift value: 3
Decrypted message: hello


```
---
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.




