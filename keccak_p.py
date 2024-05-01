from step_mappings import THETA, RHO, PI, CHI, IOTA
from converting import string_to_state_array, state_array_to_string
from math import log2


def keccak_p(s: str, b:int, nr: int) -> str:
    """
    Algorithm 7: KECCAK-p[b, nr](S)
    
    Input: string S of length b; number of rounds nr

    Output: string S′ of length b
    """
    if b not in (25, 50, 100, 200, 400, 800, 1600):
        raise Exception(f"You passed the wrong string, its length cannot be equal to {b}")
    w = b // 25
    l = int(log2(w))

    # first step
    state_A = string_to_state_array(s)

    # second step
    for ir in range(12 + 2*l - nr, 12 + 2*l):
        state_A = THETA(state_A, b)
        state_A = RHO(state_A, b)
        state_A = PI(state_A, b)
        state_A = CHI(state_A, b)
        state_A = IOTA(state_A, b, ir)

    # third step
    new_s = state_array_to_string(state_A)

    return new_s
