import ast
from rsa import encrypt

if __name__ == "__main__":
    msg = input("Write msg: ")
    public_input = input("Enter a public key with format (n, e): ")
    public = ast.literal_eval(public_input)
    encrypted_msg = encrypt(msg, public)
    print("Encrypted msg:")
    print(encrypted_msg)