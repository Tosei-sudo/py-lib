# coding: utf-8

def gcd(p, q):
    '''
    最大公約数を求める。
    '''
    while q != 0:
        p, q = q, p % q

    return p

def lcm(p, q):
    '''
    最小公倍数を求める。
    '''
    return (p * q) // gcd(p, q)