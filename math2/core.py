# coding: utf-8

def gcd(p, q):
    '''
    最大公約数を求める。
    @param p: int
    @param q: int
    '''
    while q != 0:
        p, q = q, p % q

    return p

def lcm(p, q):
    '''
    最小公倍数を求める。
    @param p: int
    @param q: int
    '''
    return (p * q) // gcd(p, q)

def is_prime(n):
    '''
    素数かどうかを判定する。
    @param n: int
    '''
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True