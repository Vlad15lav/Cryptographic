# Sequence Luke
def luke_sequence(u: list, P: int = 1, Q: int = -1) -> list:
    u.append(u[-1] * P + u[-2] * Q)
    return u