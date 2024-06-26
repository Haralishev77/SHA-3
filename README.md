# SHA-3
SHA-3 (Secure Hash Algorithm 3) is a set of cryptographic hash functions defined in FIPS 202: SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions.
The SHA-3 family consists of six hash functions with digests (hash values) that are 128, 224, 256, 384 or 512 bits: SHA3-224, SHA3-256, SHA3-384, SHA3-512, SHAKE128, SHAKE256.

## Test
In the *test_files* folder, there are files with input messages of different length and output hashes for SHA3-224, SHA3-256, SHA3-384, SHA3-512, SHAKE128, SHAKE256. [Source](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines/example-values)

To run the tests, simply execute:
```
python -m unittest -v test.py
```

## User input
The *user* folder contains *input.md* and *outout.md*, which contain the input message and the result of the hash function that the user called. To start working with the user input, simply execute:
```
python main.py
```
