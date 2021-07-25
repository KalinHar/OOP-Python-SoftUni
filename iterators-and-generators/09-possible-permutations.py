from itertools import permutations


def possible_permutations(elements):
    return (list(p) for p in permutations(elements))

    # if len(elements) <= 1:
    #     yield elements
    # else:
    #     for perm in possible_permutations(elements[1:]):
    #         for i in range(len(elements)):
    #             yield perm[:i] + elements[0:1] + perm[i:]


[print(n) for n in possible_permutations([1, 2, 3])]
