import random

def miller_rabin(n, k=5):
    """ Miller-Rabin primality test without logging or extra code.
        n: the number to test for primality
        k: number of iterations (more iterations = higher confidence)
    """
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2 and 3 are prime
    if n % 2 == 0:
        return False  # Even number and not 2, so not prime
    
    # Step 1: Write n-1 as 2^s * d
    s, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    
    # Step 2: Test k random bases
    for _ in range(k):
        a = random.randint(2, n - 2)
        
        # Compute a^d % n
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        # Square x repeatedly
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True

