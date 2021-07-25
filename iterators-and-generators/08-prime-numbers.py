def get_primes(nums):
    for num in nums:
        if num > 1:
            count = 0
            for div in range(2, num + 1):
                if num % div == 0:
                    count += 1
                    if count > 1:
                        break
            if count == 1:
                yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))