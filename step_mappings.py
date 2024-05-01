import numpy as np
from math import log2


def THETA(state_A: np.array, b: int) -> np.array: 
    """
    Algorithm 1: θ(A)

    Input: state array A

    Output: state array A′
    """
    w = b // 25
    state_C = np.array(np.zeros((5, w)), dtype=int)
    state_D = np.array(np.zeros((5, w)), dtype=int)
    new_state_A = np.array(np.zeros((5, 5, w)), dtype=int)
    
    # first step
    for x in range(0, 5):
        for z in range(0, w):
            state_C[x, z] = state_A[x, 0, z] ^ state_A[x, 1, z] ^ state_A[x, 2, z] ^ state_A[x, 3, z] ^ state_A[x, 4, z]

    # second step
    for x in range(0, 5):
        for z in range(0, w):
            state_D[x, z] = state_C[(x - 1) % 5, z] ^ state_C[(x + 1) % 5, (z - 1) % w]

    # third step 
    for x in range(0, 5):
        for y in range(0, 5):
            for z in range(0, w):
                new_state_A[x, y, z] = state_A[x, y, z] ^ state_D[x, z]
    
    return new_state_A


def RHO(state_A: np.array, b: int) -> np.array:
    """
    Algorithm 2: ρ(A)

    Input: state array A

    Output: state array A′
    """
    w = b // 25
    new_state_A = np.array(np.zeros((5, 5, w)), dtype=int)

    # first step
    for z in range(0, w):
        new_state_A[0, 0, z] = state_A[0, 0, z]

    # second step
    x, y = 1, 0

    # third step
    for t in range(0, 24):
        for z in range(0, w):
            new_state_A[x, y, z] = state_A[x, y, (z - (t + 1) * (t + 2) // 2) % w]
        x, y = y, (2 * x + 3 * y) % 5

    return new_state_A


def PI(state_A: np.array, b: int) -> np.array:
    """
    Algorithm 3: π(A)

    Input: state array A

    Output: state array A′

    """
    w = b // 25
    new_state_A = np.array(np.zeros((5, 5, w)), dtype=int)

    # first step
    for x in range(0, 5):
        for y in range(0, 5):
            for z in range(0, w):
                new_state_A[x, y, z] = state_A[(x + (3 * y)) % 5, x, z]

    return new_state_A


def CHI(state_A: np.array, b: int) -> np.array:
    """
    Algorithm 4: χ(A) 
    
    Input: state array A

    Output: state array A′
    """
    w = b // 25
    new_state_A = np.array(np.zeros((5, 5, w)), dtype=int)
    # first step
    for x in range(0, 5):
        for y in range(0, 5):
            for z in range(0, w):
                new_state_A[x, y, z] = state_A[x, y, z] ^ ((state_A[(x + 1) % 5, y, z] ^ 1) * state_A[(x + 2) % 5, y, z])

    return new_state_A


def rc(t: int) -> int:
    """
    Algorithm 5: rc(t)
    
    Input: integer t

    Output: bit rc(t)
    """

    # first step
    if t % 255 == 0:
        return 1
    
    # second step
    r = [1, 0, 0, 0, 0, 0, 0, 0]

    # third step
    for i in range(1, (t % 255) + 1):
        r.insert(0, 0)
        r[0] = r[0] ^ r[8]
        r[4] = r[4] ^ r[8]
        r[5] = r[5] ^ r[8]
        r[6] = r[6] ^ r[8]
        r = r[:8]

    return r[0]


def IOTA(state_A: np.array, b: int, ir: int) -> np.array:
    """
    Algorithm 6: ι(A, ir)

    Input: state array A; round index ir
    
    Output: state array A′
    """
    w = b // 25
    l = int(log2(w))

    # first step
    new_state_A = state_A.copy()

    # second step
    RC = [False] * w
    
    # third step
    for j in range(0, l + 1):
        RC[2**j - 1] = rc(j + 7 * ir)

    # fourth step 
    for z in range(0, w):
        new_state_A[0, 0, z] = (new_state_A[0, 0, z] + RC[z]) % 2
        
    return new_state_A