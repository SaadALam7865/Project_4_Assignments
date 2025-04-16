
# def even_num():
#     return [i * 2  for i in range(20)]
# even = map(str,even_num())
# print(' '.join(even))

# def odd_num():
#     return [i * 2 + 1 for i in range(20)]

# odd = map(str,odd_num())
# print(' '.join(odd))

# def prime_num():
#     n = 20
#     prime = [True] * (n + 1)  # Indexes 0 to 20
#     prime[0] = prime[1] = False  # 0 and 1 are not primes
    
#     p = 2
#     while p * p <= n:
#         if prime[p]:
#             for i in range(p * p, n + 1, p):
#                 prime[i] = False
#         p += 1

#     # Yield all prime numbers
#     for p in range(2, n + 1):
#         if prime[p]:
#             yield p

# # Convert the generator to a string and print primes
# prime = map(str, prime_num())
# print(' '.join(prime))


# even odd numbers
# even_num = [i * 2 for i in range(40)]
# odd_num = [i * 2 + 1 for i in range(40)]
# even = map(str, even_num)
# odd = map(str, odd_num)
# print('Even numbers')
# print(' '.join(even))
# print('Odd numbers')
# print(" ".join(odd))


