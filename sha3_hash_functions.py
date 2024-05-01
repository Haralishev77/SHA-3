from sponge import keccak


def sha3_224(m: str) -> str:
    return keccak(m + '01', 224, 448)


def sha3_256(m: str) -> str:
    return keccak(m + '01', 256, 512)


def sha3_384(m: str) -> str:
    return keccak(m + '01', 384, 768)   


def sha3_512(m: str) -> str:
    return keccak(m + '01', 512, 1024)


def shake128(m: str, d: int) -> str:
    return keccak(m + '1111', d, 256)


def shake256(m: str, d: int) -> str:
    return keccak(m + '1111', d, 512)