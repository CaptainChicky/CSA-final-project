from rsa import generate_keypair

if __name__ == "__main__":
    bit_length = int(input("Enter bit length: "))
    public, private = generate_keypair(bit_length)
    print("Public Key:", public)
    print("Private Key:", private)