import hashlib
import random


def generate_key(seed: str, length: int) -> str:
    seed_hash = hashlib.md5(seed.encode()).digest()
    seed_int = int.from_bytes(seed_hash[:4], 'big')
    random.seed(seed_int)
    return ''.join(chr(random.randint(65, 90)) for _ in range(length))
