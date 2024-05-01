import numpy as np

def string_to_state_array(s: str) -> np.array:
    b = len(s)
    if b not in (25, 50, 100, 200, 400, 800, 1600):
        raise Exception(f"You passed the wrong string, its length cannot be equal to {b}")
    w = b // 25

    state_A = np.array(np.zeros((5, 5, w)), dtype=int)

    for x in range(0, 5):
        for y in range(0, 5):
            for z in range(0, w):
                state_A[x, y, z] = s[w * (5 * y + x) + z]
    
    return state_A


def state_array_to_string(state_A: np.array) -> str:
    w = state_A.shape[2]
    if w not in (1, 2, 4, 8, 16, 32, 64):
        raise Exception(f"You passed the wrong state array, its length cannot be equal to {w}")
    
    lanes = list([0]*5 for _ in range(0, 5))
    for x in range(0, 5):
        for y in range(0, 5):
            lane = ''
            for z in range(0, w):
                lane += str(state_A[x, y, z])
            lanes[x][y] = lane

    planes = [0]*5
    for y in range(0, 5):
        plane = ''
        for x in range(0, 5):
            plane += lanes[x][y]
        planes[y] = plane

    s = ''
    for y in range(0, 5):
        s += planes[y]

    return s