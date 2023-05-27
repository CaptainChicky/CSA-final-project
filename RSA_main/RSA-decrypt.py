def decrypt(msg_ciphertext, package): # ciper is a list
    n, d = package
    msg_plaintext = [chr(pow(c, d, n)) for c in msg_ciphertext]
    # No need to use ord() since c is now a number
    # After decryption, we cast it back to character
    # to be joined in a string for the final result
    return (''.join(msg_plaintext))

#-------------------------------------------------------------
#driver program

if __name__ == "__main__":

    private_input = input("Enter private key with format (n, d): ")
    private = eval(private_input)

    encrypted_msg_input = input("Enter encrypted msg list: ")
    encrypted_msg = eval(encrypted_msg_input)
    
    print("Decrypted msg: ")
    print(decrypt(encrypted_msg, private))
