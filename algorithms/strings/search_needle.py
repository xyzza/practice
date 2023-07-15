TEST = [
    ("sadbutsad", "sad", 0),
    ("lol", "lol", 0),
    ("hello", "gghjkhkjhkjasd", -1),
    ("hello", "llo", 2),
    ("hello", "gg", -1),
    ("mississippi", "pi", 9),
]


# def main(haystack: str, needle: str) -> int:
#     h = len(haystack)
#     n = len(needle)
#     if n > h:
#         return -1
#     for i in range(h - n + 1):
#         if haystack[i: i+ n] == needle:
#             return i
#     return -1

# limit the int overflow for hash
MOD = 10**3 + 33
# dimension of hash vector
# 26 lower English letter
DIM = 26


def _ord(c: str) -> int:
    # shifts 'a' to 0 and 'z' to 25
    return ord(c) - 97


def _hash(s: str) -> int:
    hash = 0
    factor = 1
    for i in range(len(s) - 1, -1, -1):
        hash += _ord(s[i]) * factor % MOD
        factor = factor * DIM % MOD

    return hash % MOD


def main(haystack: str, needle: str) -> int:
    h = len(haystack)
    n = len(needle)
    if n > h:
        return -1
    n_hash = _hash(needle)
    m_dim = DIM**n

    for i in range(h - n + 1):
        if not i:
            h_hash = _hash(haystack[:n])
        else:
            # we may do hash rollover
            h_hash = (
                (h_hash * DIM) % MOD
                - (_ord(haystack[i - 1]) * m_dim) % MOD
                + (_ord(haystack[i + n - 1]))
                + MOD
            ) % MOD

        if n_hash == h_hash:
            if haystack[i : i + n] == needle:
                return i
    return -1


if __name__ == "__main__":
    for (h, n, expected) in TEST:
        assert h
        assert n
        result = main(h, n)
        print(f"For haystack: {h} needle: {n} is at index: {result}")
        assert result == expected, (result, expected)
