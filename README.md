# Secure_Computer_System_Design_Lab1

All dependencies are stored in a virtual env, so it is enough to just have python3 for running the code, just make sure to run it with with virtual env turned on,
$ source env/bin/activate

The aesEnc.py uses AES (Advanced Encryption Standard), which is a symmetric block cipher standardized by NIST . It has a fixed data block size of 16 bytes. Its keys can be 128, 192, or 256 bits long.AES is imported through the PyCryptDome Library to encrypt the hard-coded string stored in the variable secret and create a key for decryption.

Running aesEnc.py will generate a key and an encrypted.bin file. The key is 16 bytes, which provides good security level provided our threat model. The key is stored in the same directory in a file called "key".

For encryption, EAX encryption alg is used, more information can be obtained from this paper http://csrc.nist.gov/groups/ST/toolkit/BCM/documents/proposedmodes/eax/eax-spec.pdf

The encrypt_and_digest() function is used to encrypt and use a signature on the file for verification. Then the decryption will have to use the decrypt_and_verifiy() function, the extra signature provided by the digest and the verify is for added message integrity.
