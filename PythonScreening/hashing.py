def sieve(limit):
    if limit < 2:
        return []

    if limit == 2:
        return [2]

    if limit == 3:
        return [2, 3]

    res = [False] * (limit + 1)

    i = 1
    while i <= limit:
        j = 1
        while j <= limit:
            n = (4 * i * i) + (j * j)

            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                res[n] ^= True

            n = (3 * i * i) + (j * j)

            if n <= limit and n % 12 == 7:
                res[n] ^= True

            n = (3 * i * i) - (j * j)

            if i > j and n <= limit and n % 12 == 11:
                res[n] ^= True

            j += 1
        i += 1


    r = 5
    while r * r <= limit:
        if res[r]:
            for i in range(r * r, limit + 1, r * r):
                res[i] = False
        r += 1

    out = [2, 3]
    for a in range(5, limit+1):
        if res[a]:
            out.append(a)

    return out


def pick_prime(primes, min_size=1000):
    """returns a suitable prime to use as modulus"""

    for prime in primes:

        if prime >= min_size:
            return prime

    # if no prime large enough exists, use last one on list

    return primes[-1]


def hash(string, modulus, base=31):
    """implements polynomial rolling of string keys"""

    hash_value = 0
    power = 1

    for char in string:
        hash_value = (hash_value + (ord(char) * power)) % modulus
        power = (power * base) % modulus

    return hash_value

if __name__ == '__main__':

    # generate primes list to use as modulus

    primes = sieve(10000)  # modify limit based on your needs

    modulus = pick_prime(primes, 1000)

    test_array = ["alpha", "beta", "gamma", "delta", "epsilon"]

    for string in test_array:
        hash_value = hash(string, modulus)

        print(f"Hash of {string} is {hash_value}")
