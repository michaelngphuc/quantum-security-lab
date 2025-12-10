from pqcrypto.kem import ml_kem_512 as kem

def main():
    print("Using KEM scheme:", kem.__name__)

    # 1. Keypair generation
    pk, sk = kem.generate_keypair()
    print("Public key length:", len(pk))
    print("Secret key length:", len(sk))

    # 2. Encapsulation (encrypt)
    ciphertext, shared_secret_sender = kem.encrypt(pk)
    print("Ciphertext length:", len(ciphertext))
    print("Sender shared secret:", shared_secret_sender.hex())

    # 3. Decapsulation (decrypt)
    # Lưu ý: decrypt(secret_key, ciphertext) – SECRET KEY ĐI TRƯỚC
    shared_secret_receiver = kem.decrypt(sk, ciphertext)
    print("Receiver shared secret:", shared_secret_receiver.hex())

    # 4. Check correctness
    print("\nMatch:", shared_secret_sender == shared_secret_receiver)

if __name__ == "__main__":
    main()
