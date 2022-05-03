from typing import List

DATA = [
    (["code", "anagram", "doce", "marganana", "wut"], ["anagram", "code"]),
    (["idea", "god", "daidee", "marganana", "odog"], ["god", "idea"]),
]


def fun_anagram(words: List[str]) -> List[str]:
    result = {}
    for word in words:
        key = frozenset(word)
        if key in result:
            result[key] = (result[key][0], result[key][1] + 1)
        else:
            result[key] = (word, 1)
    return sorted([x[0] for x in result.values() if x[1] > 1])


def main():
    for words, expected in DATA:
        print(words)
        result = fun_anagram(words=words)
        print(result)
        assert result == expected, "Test case failed!"
        print("OK!\n")


if __name__ == "__main__":
    main()
