import sys
import argparse

BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def encode_base64(text):
    binary_str = ''.join([format(ord(char), '08b') for char in text])
    padding_length = (6 - len(binary_str) % 6) % 6
    binary_str_padded = binary_str + '0' * padding_length
    encoded = ''
    for i in range(0, len(binary_str_padded), 6):
        chunk = binary_str_padded[i:i+6]
        index = int(chunk, 2)
        encoded += BASE64_CHARS[index]
    padding = '=' * ((4 - len(encoded) % 4) % 4)
    return encoded + padding

def decode_base64(encoded_text):
    """Decodes Base64 text to original text."""
    encoded_text = encoded_text.rstrip('=')
    binary_str = ''
    for char in encoded_text:
        if char in BASE64_CHARS:
            index = BASE64_CHARS.index(char)
            binary_str += format(index, '06b')
    decoded = ''
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        if len(byte) == 8:
            decoded += chr(int(byte, 2))
    return decoded

def encode_hex(text):
    hex_str = ''
    for char in text:
        hex_char = format(ord(char), '02x')
        hex_str += hex_char
    return hex_str

def decode_hex(encoded_text):
    decoded = ''
    for i in range(0, len(encoded_text), 2):
        byte = encoded_text[i:i+2]
        decoded += chr(int(byte, 16))
    return decoded

def encode_binary(text):
    binary_str = ''
    for char in text:
        binary_char = format(ord(char), '08b')
        binary_str += binary_char + ' '
    return binary_str.strip()

def decode_binary(encoded_text):
    binary_values = encoded_text.split()
    decoded = ''
    for binary in binary_values:
        decoded += chr(int(binary, 2))
    return decoded

def encode_octal(text):
    octal_str = ''
    for char in text:
        octal_char = format(ord(char), '03o')
        octal_str += octal_char + ' '
    return octal_str.strip()

def decode_octal(encoded_text):
    octal_values = encoded_text.split()
    decoded = ''
    for octal in octal_values:
        if len(octal) != 3 or not octal.isdigit():
            print("Error: Each octal value must be 3 digits long and contain only numbers.")
            sys.exit(1)
        decoded += chr(int(octal, 8))
    return decoded

def interactive_mode():
    mode = input("Enter 'encode' or 'decode': ").strip().lower()
    if mode not in ['encode', 'decode']:
        print("Invalid mode. Please enter 'encode' or 'decode'.")
        return

    scheme = input("Enter encoding scheme (b64, hex, bin, oct): ").strip().lower()
    if scheme not in ['b64', 'hex', 'bin', 'oct']:
        print("Invalid encoding scheme. Choose from b64, hex, bin, oct.")
        return

    text = input("Enter text: ")

    if mode == 'encode':
        if scheme == 'b64':
            result = encode_base64(text)
        elif scheme == 'hex':
            result = encode_hex(text)
        elif scheme == 'bin':
            result = encode_binary(text)
        elif scheme == 'oct':
            result = encode_octal(text)
    else:
        if scheme == 'b64':
            result = decode_base64(text)
        elif scheme == 'hex':
            result = decode_hex(text)
        elif scheme == 'bin':
            result = decode_binary(text)
        elif scheme == 'oct':
            result = decode_octal(text)

    print(f"Result: {result}")

def command_line_mode(mode, scheme, text):
    if scheme == 'b64':
        if mode == 'encode':
            result = encode_base64(text)
        else:
            result = decode_base64(text)
    elif scheme == 'hex':
        if mode == 'encode':
            result = encode_hex(text)
        else:
            result = decode_hex(text)
    elif scheme == 'bin':
        if mode == 'encode':
            result = encode_binary(text)
        else:
            result = decode_binary(text)
    elif scheme == 'oct':
        if mode == 'encode':
            result = encode_octal(text)
        else:
            result = decode_octal(text)
    else:
        print("Error: Invalid encoding scheme. Choose from b64, hex, bin, oct.")
        sys.exit(1)

    print(result)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Simple Data Encoder and Decoder")
    parser.add_argument('mode', nargs='?', help="Mode: encode or decode")
    parser.add_argument('scheme', nargs='?', help="Scheme: b64, hex, bin, oct")
    parser.add_argument('text', nargs='?', help="Text to encode/decode")
    return parser.parse_args()

def main():
    args = parse_arguments()
    if args.mode and args.scheme and args.text:
        mode = args.mode.lower()
        if mode not in ['encode', 'decode']:
            print("Error: Mode must be 'encode' or 'decode'.")
            sys.exit(1)
        scheme = args.scheme.lower()
        text = args.text
        command_line_mode(mode, scheme, text)
    else:
        interactive_mode()

main()
