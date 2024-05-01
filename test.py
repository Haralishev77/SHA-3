import unittest
from sha3_hash_functions import sha3_224, sha3_256, sha3_384, sha3_512, shake128, shake256

class TestSHA3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("SHA-3/test_files/Msg_1630bit.md", "r") as file:
            cls.message = file.read()
        with open("SHA-3/test_files/True_hashes_1630bit.md", "r") as file:
            cls.hashes = {}
            lines = file.read().splitlines()
            for line in lines:
                hash, name = line.split(";")
                cls.hashes[name] = hash

    def test_sha3_224(self):
        true_hash = self.hashes["SHA224"]
        self.assertEqual(true_hash, sha3_224(self.message).upper())

    def test_sha3_256(self):
        true_hash = self.hashes["SHA256"]
        self.assertEqual(true_hash, sha3_256(self.message).upper())

    def test_sha3_384(self):
        true_hash = self.hashes["SHA384"]
        self.assertEqual(true_hash, sha3_384(self.message).upper())

    def test_sha3_512(self):
        true_hash = self.hashes["SHA512"]
        self.assertEqual(true_hash, sha3_512(self.message).upper())

    def test_shake128(self):
        true_hash = self.hashes["SHAKE128"]
        self.assertEqual(true_hash, shake128(self.message, 4096).upper())

    def test_shake256(self):
        true_hash = self.hashes["SHAKE256"]
        self.assertEqual(true_hash, shake256(self.message, 4096).upper())

if __name__ == "__main__":
    unittest.main()
