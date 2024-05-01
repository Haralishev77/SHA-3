from keccak_p import keccak_p


def xor_string(s1: str, s2: str) -> str:
    if len(s1) != len(s2):
        raise Exception("s1 and s2 have different lengths")

    return "".join([str(int(s1[i] != s2[i])) for i in range(len(s1))])


def pad10_1(x: int, m: int) -> str:
    """
    Algorithm 9: pad10*1(x, m)
    
    Input: positive integer x; non-negative integer m
    
    Output: string P such that m + len(P) is a positive multiple of x
    """

    return "1" + "0" * ((-m - 2) % x) + "1"


def keccak(n: str, d: int, c:int, f=keccak_p, pad=pad10_1) -> str: # keccak[c] = sponge[keccak-p[1600, 24], pad10*1, 1600–c]
    """
    Algorithm 8: SPONGE[f, pad, r](N, d)
    
    Input: string N, nonnegative integer d

    Output: string Z such that len(Z)=d
    """
    b = 1600
    nr = 24
    r = b - c

    p = n + pad(r, len(n))
    n = len(p) // r
    s = "0" * b
    z = ""

    for i in range(0, n):
        s = f(xor_string(s, p[i * r:(i + 1) * r] + ("0" * c)), b, nr)

    z += s[:r]
    while len(z) < d:
        s = f(s, b, nr)
        z += s[:r]
        
    z = z[:d]

    result = ''
    for i in range(0, len(z), 8):
        bit_s2 = z[i:i+4]
        bit_s1 = z[i+4:i+8]
        s1 = str(hex(int(bit_s1[::-1], 2)))[2:]
        s2 = str(hex(int(bit_s2[::-1], 2)))[2:]
        result += s1 + s2

    return result



    