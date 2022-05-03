from typing import List

DATA = [
    (["code", "anagram", "doce", "marganana", "wut"], ["anagram", "code", "wut"]),
    (["idea", "god", "daidee", "marganana", "odog"], ["god", "idea", "marganana"]),
]


def fun_anagram(words: List[str]) -> List[str]:
    _words = set()
    result = []
    for word in words:
        _key = frozenset(word)
        if _key not in _words:
            _words.add(_key)
            result.append(word)
    return sorted(result)


def main():
    for words, expected in DATA:
        print(words)
        result = fun_anagram(words=words)
        print(result)
        assert result == expected, "Test case failed!"
        print("OK!\n")


if __name__ == "__main__":
    main()
