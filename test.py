import unittest
from sha3_hash_functions import sha3_224, sha3_256, sha3_384, sha3_512, shake128, shake256

class TestSHA3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("SHA-3/test_files/Messages.md", "r") as file:
            cls.messages = {}
            lines = file.read().splitlines()
            for line in lines:
                message, length = line.split("|")
                cls.messages[length] = message
        with open("SHA-3/test_files/True_hashes.md", "r") as file:
            cls.hashes = {}
            lines = file.read().splitlines()
            for line in lines:
                name, values = line.split("||")
                cls.hashes[name] = {}
                elements = values.split("|")
                for element in elements:
                    hash, length = element.split(";")
                    cls.hashes[name][length] = hash

    def test_sha3_224(self):
        self.assertEqual(self.hashes["SHA224"]["0"], sha3_224(self.messages["0"]).upper())
        self.assertEqual(self.hashes["SHA224"]["5"], sha3_224(self.messages["5"]).upper())
        self.assertEqual(self.hashes["SHA224"]["30"], sha3_224(self.messages["30"]).upper())
        self.assertEqual(self.hashes["SHA224"]["1600"], sha3_224(self.messages["1600"]).upper())
        self.assertEqual(self.hashes["SHA224"]["1605"], sha3_224(self.messages["1605"]).upper())
        self.assertEqual(self.hashes["SHA224"]["1630"], sha3_224(self.messages["1630"]).upper())

    def test_sha3_256(self):
        self.assertEqual(self.hashes["SHA256"]["0"], sha3_256(self.messages["0"]).upper())
        self.assertEqual(self.hashes["SHA256"]["5"], sha3_256(self.messages["5"]).upper())
        self.assertEqual(self.hashes["SHA256"]["30"], sha3_256(self.messages["30"]).upper())
        self.assertEqual(self.hashes["SHA256"]["1600"], sha3_256(self.messages["1600"]).upper())
        self.assertEqual(self.hashes["SHA256"]["1605"], sha3_256(self.messages["1605"]).upper())
        self.assertEqual(self.hashes["SHA256"]["1630"], sha3_256(self.messages["1630"]).upper())

    def test_sha3_384(self):
        self.assertEqual(self.hashes["SHA384"]["0"], sha3_384(self.messages["0"]).upper())
        self.assertEqual(self.hashes["SHA384"]["5"], sha3_384(self.messages["5"]).upper())
        self.assertEqual(self.hashes["SHA384"]["30"], sha3_384(self.messages["30"]).upper())
        self.assertEqual(self.hashes["SHA384"]["1600"], sha3_384(self.messages["1600"]).upper())
        self.assertEqual(self.hashes["SHA384"]["1605"], sha3_384(self.messages["1605"]).upper())
        self.assertEqual(self.hashes["SHA384"]["1630"], sha3_384(self.messages["1630"]).upper())

    def test_sha3_512(self):
        self.assertEqual(self.hashes["SHA512"]["0"], sha3_512(self.messages["0"]).upper())
        self.assertEqual(self.hashes["SHA512"]["5"], sha3_512(self.messages["5"]).upper())
        self.assertEqual(self.hashes["SHA512"]["30"], sha3_512(self.messages["30"]).upper())
        self.assertEqual(self.hashes["SHA512"]["1600"], sha3_512(self.messages["1600"]).upper())
        self.assertEqual(self.hashes["SHA512"]["1605"], sha3_512(self.messages["1605"]).upper())
        self.assertEqual(self.hashes["SHA512"]["1630"], sha3_512(self.messages["1630"]).upper())

    def test_shake128(self):
        self.assertEqual(self.hashes["SHAKE128"]["0"], shake128(self.messages["0"], 4096).upper())
        self.assertEqual(self.hashes["SHAKE128"]["5"], shake128(self.messages["5"], 4096).upper())
        self.assertEqual(self.hashes["SHAKE128"]["30"], shake128(self.messages["30"], 4096).upper())
        self.assertEqual(self.hashes["SHAKE128"]["1600"], shake128(self.messages["1600"], 4096).upper())
        self.assertEqual(self.hashes["SHAKE128"]["1605"], shake128(self.messages["1605"], 4096).upper())
        self.assertEqual(self.hashes["SHAKE128"]["1630"], shake128(self.messages["1630"], 4096).upper())

    def test_shake256(self):
        self.assertEqual(self.hashes["SHAKE256"]["0"], shake256(self.messages["0"], 4096).upper())
        self.assertEqual(self.hashes["SHAKE256"]["5"], shake256(self.messages["5"], 4096).upper())
        self.assertEqual(self.hashes["SHAKE256"]["30"], shake256(self.messages["30"], 4096).upper())
        self.assertEqual(self.hashes["SHAKE256"]["1600"], shake256(self.messages["1600"], 4096).upper())
        self.assertEqual(self.hashes["SHAKE256"]["1605"], shake256(self.messages["1605"], 4096).upper())
        self.assertEqual(self.hashes["SHAKE256"]["1630"], shake256(self.messages["1630"], 4096).upper())

if __name__ == "__main__":
    unittest.main()
