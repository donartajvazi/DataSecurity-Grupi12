import hashlib
import random


def generate_key(seed: str, length: int) -> str:
    seed_hash = hashlib.md5(seed.encode()).digest()
    seed_int = int.from_bytes(seed_hash[:4], 'big')
    random.seed(seed_int)
    return ''.join(chr(random.randint(65, 90)) for _ in range(length))


def vigenere_encrypt(plaintext: str, key: str) -> str:
    ciphertext = []
    key_length = len(key)

    print("\n--- ENCRYPTION DETAILS ---")
    print(f"{'Index':<5} {'Plain':<6} {'P#':<4} {'Key':<6} {'K#':<4} {'Cipher':<7} {'C#':<4}")
    print("-" * 40)

    for i, char in enumerate(plaintext.upper()):
        if char.isalpha():
            p_num = ord(char) - ord('A')
            k_char = key[i % key_length]
            k_num = ord(k_char) - ord('A')
            c_num = (p_num + k_num) % 26
            c_char = chr(c_num + ord('A'))
            ciphertext.append(c_char)

            print(f"{i:<5} {char:<6} {p_num:<4} {k_char:<6} {k_num:<4} {c_char:<7} {c_num:<4}")
        else:
            ciphertext.append(char)

    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext: str, key: str) -> str:

    plaintext = []
    key_length = len(key)

    print("\n--- DECRYPTION DETAILS ---")
    print(f"{'Index':<5} {'Cipher':<7} {'C#':<4} {'Key':<6} {'K#':<4} {'Plain':<6} {'P#':<4}")
    print("-" * 40)

    for i, char in enumerate(ciphertext.upper()):
        if char.isalpha():
            c_num = ord(char) - ord('A')
            k_char = key[i % key_length]
            k_num = ord(k_char) - ord('A')
            p_num = (c_num - k_num + 26) % 26
            p_char = chr(p_num + ord('A'))
            plaintext.append(p_char)

            print(f"{i:<5} {char:<7} {c_num:<4} {k_char:<6} {k_num:<4} {p_char:<6} {p_num:<4}")
        else:
            plaintext.append(char)

    return ''.join(plaintext)

