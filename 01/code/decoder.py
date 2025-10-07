try:
    from config import key
except ImportError:
    raise ImportError("\nYou need a config.py file with a key")
# key is the secret key
chunk_len = 10

def char_to_int(c):
    number_repr = ord(c)*key
    return str(number_repr).zfill(chunk_len)

def intstring_to_char(istr: str) -> str:
    return chr(int(int(istr)/key))

def code_to_char(code: str) -> str:
    chunks = [code[i : i + chunk_len] for i in range(0, len(code), chunk_len)]
    return "".join([intstring_to_char(chunk) for chunk in chunks])


def text_to_code(text: str) -> str:
    return "".join([char_to_int(c) for c in text])


def str_encoder_decoder(source: str) -> str:
    if source.isdecimal():
        return code_to_char(source)
    else:
        return text_to_code(source)

def make_sure():
    import random
    import string
    print("\n\n\n",30*"#","\n\tRunning self tests\n",30*"#","\n\n\n")
    for i in range(40):
        length = random.randint(20, 40)
        rand_str = "".join(
            random.choices(
                string.ascii_letters + string.digits + string.punctuation + " ", k=length
            )
        )
        encoded = str_encoder_decoder(rand_str)
        decoded = str_encoder_decoder(encoded)
        print(decoded)
        print(rand_str)
        assert rand_str == decoded, f"Failed for {rand_str}"
    print("\n\n\n",30*"#","\n\tAll tests passed!\n",30*"#","\n\n\n")

# added this just for testing, remove when done, this is insecure
key_limit = 100
if not isinstance(key, int):
    raise ValueError("Key must be an integer")
if key > key_limit:
    raise ValueError(f"Key too large, max is {key_limit}")
elif key < 1:
    raise ValueError("Key too small, min is 1")

make_sure()

if __name__ == "__main__":
    make_sure()