# Kyber KEM Demo

This module contains an implementation and demonstration of the CRYSTALS-Kyber
Key Encapsulation Mechanism (PQC finalist selected by NIST).

## Goals
- Implement Kyber512 key generation, encryption (encapsulation), and decryption (decapsulation)
- Show how lattice-based cryptography resists quantum attacks
- Compare performance vs RSA/ECC
- Provide clean Python example using pqcrypto library

## Status
- Done

## ML-KEM (Kyber) Working Demo

This module includes a fully working implementation of the NIST-selected
post-quantum KEM **ML-KEM-512** using the `pqcrypto` Python library.

### ✔ What works
- Keypair generation (800-byte public key, 1632-byte secret key)
- Encapsulation (ciphertext + shared secret)
- Decapsulation (recovered shared secret)
- Verified: `Match: True` between sender and receiver secrets

### ✔ Why this matters
ML-KEM (Kyber) is the official NIST PQC KEM replacing RSA and ECC in the future.
This demo proves practical understanding of quantum-safe cryptography.

### ✔ Files
- `kyber_demo.py` — runnable PQC demo

# ML-KEM Implementation Notes

## Algorithm
- Based on Module-LWE hardness.
- Security equivalent: ~AES-128 for ML-KEM-512.
- Resistant to Shor's algorithm.

## Performance benchmark (to add)
- Keygen time
- Encapsulation time
- Decapsulation time
- Key sizes

