import itertools

def combinations(word: str):
    combinations = set()
    for i in range(1, len(word) + 1):
        for combination in itertools.permutations(word, i):
            combinations.add(''.join(combination))
    return combinations

print(combinations("привет"))