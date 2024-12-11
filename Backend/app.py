from flask import Flask, request, jsonify  # type: ignore
from flask_cors import CORS  # type: ignore

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:5173"]}})

# Substitution Cipher
def substitution_cipher(text, key, decode=False):
    shift = int(key) if not decode else -int(key)
    result = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - start + shift) % 26 + start))
        else:
            result.append(char)
    return ''.join(result)

# Transposition Cipher
def transposition_cipher(text, key, decode=False):
    key = int(key)
    if decode:
        # Calculate the number of columns and rows in the grid
        num_cols = key
        num_rows = (len(text) + key - 1) // key  # Ceiling division
        num_shaded_boxes = (num_cols * num_rows) - len(text)

        # Create a list for the plaintext
        plaintext = [''] * num_rows

        col = 0
        row = 0

        for symbol in text:
            plaintext[row] += symbol
            row += 1

            # If we've reached the end of a column or hit a shaded box, move to the next column
            if row == num_rows or (row == num_rows - 1 and col >= num_cols - num_shaded_boxes):
                row = 0
                col += 1

        # Reconstruct the original text by reading row-wise
        return ''.join(plaintext)
    else:
        # Encode transposition: Arrange text column-wise
        ciphertext = [''] * key
        for col in range(key):
            pointer = col
            while pointer < len(text):
                ciphertext[col] += text[pointer]
                pointer += key
        return ''.join(ciphertext)

# Complex Cipher (Combines Substitution and Transposition)
def complex_cipher(text, key, decode=False):
    # First apply substitution, then transposition
    sub_text = substitution_cipher(text, key, decode)
    return transposition_cipher(sub_text, key, decode)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    text = data.get('text', '')
    key = data.get('key', 0)
    mode = data.get('mode', '1')

    if mode == '1':  # Substitution cipher
        encrypted = substitution_cipher(text, key)
    elif mode == '2':  # Transposition cipher
        encrypted = transposition_cipher(text, key)
    elif mode == '3':  # Complex cipher
        encrypted = complex_cipher(text, key)
    else:
        encrypted = text  # Unsupported mode, return as-is

    return jsonify({'encrypted': encrypted})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    text = data.get('text', '')
    key = data.get('key', 0)
    mode = data.get('mode', '1')

    if mode == '1':  # Substitution cipher
        decrypted = substitution_cipher(text, key, decode=True)
    elif mode == '2':  # Transposition cipher
        decrypted = transposition_cipher(text, key, decode=True)
    elif mode == '3':  # Complex cipher
        decrypted = complex_cipher(text, key, decode=True)
    else:
        decrypted = text  # Unsupported mode, return as-is

    return jsonify({'decrypted': decrypted})

if __name__ == '__main__':
    app.run(debug=True)
