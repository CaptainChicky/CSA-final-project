def encrypt(msg_plaintext, package): # plain is converted into a Unicode code point list
    # unpack key value pair
    n, e = package
    # ord(c) converts the character c to its corresponding Unicode code point.
    # pow(ord(c), e, n) raises the Unicode code point to the power of e modulo n. 
    msg_ciphertext = [pow(ord(c), e, n) for c in msg_plaintext]
    return msg_ciphertext # this is a list

#-------------------------------------------------------------
#driver program

if __name__ == "__main__":

    msg = input("Write msg: ")

    public_input = input("Enter a public key with format: (n, e): ")
    public = eval(public_input)

    encrypted_msg = encrypt(msg, public)
    print("Encrypted msg: ")
    print(encrypted_msg)
