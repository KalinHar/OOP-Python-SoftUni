# from itertools import permutations


def possible_permutations(elements):
    # return (list(p) for p in permutations(elements))

    perms = permutation(elements)
    for p in perms:
        yield p


def permutation(lst):
    if len(lst) <= 1:
        return [lst]
    perms = []
    for i in range(len(lst)):
        el = lst[i]
        rest_els = lst[:i] + lst[i + 1:]
        for p in permutation(rest_els):
            perms.append([el] + p)
    return perms


    # if len(elements) <= 1:
    #     yield elements
    # else:
    #     for perm in possible_permutations(elements[1:]):
    #         for i in range(len(elements)):
    #             yield perm[:i] + elements[0:1] + perm[i:]


[print(n) for n in possible_permutations([1, 2, 3])]
