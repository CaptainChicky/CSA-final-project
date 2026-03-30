import ast
from rsa import decrypt

if __name__ == "__main__":
    private_input = input("Enter private key with format (n, d): ")
    private = ast.literal_eval(private_input)
    encrypted_msg_input = input("Enter encrypted msg list: ")
    encrypted_msg = ast.literal_eval(encrypted_msg_input)
    print("Decrypted msg:")
    print(decrypt(encrypted_msg, private))