import random
import logging

# Configure logging to display all the steps
logging.basicConfig(level=logging.INFO, format='%(message)s')

def miller_rabin(n, k=5):
    """ Miller-Rabin primality test with logging.
        n: the number to test for primality
        k: number of iterations (more iterations = higher confidence)
    """
    if n <= 1:
        logging.info(f"{n} is not prime (less than or equal to 1).")
        return False
    if n <= 3:
        logging.info(f"{n} is prime (2 or 3).")
        return True  # 2 and 3 are prime
    if n % 2 == 0:
        logging.info(f"{n} is not prime (even number).")
        return False  # Even number and not 2, so not prime
    
    # Step 1: Write n-1 as 2^s * d
    s, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    logging.info(f"Step 1: n-1 = {n-1} = 2^{s} * {d}")
    
    # Step 2: Test k random bases
    for i in range(k):
        a = random.randint(2, n - 2)
        logging.info(f"Iteration {i+1}: Chose random base a = {a}")
        
        # Compute a^d % n
        x = pow(a, d, n)
        logging.info(f"a^d % n = {a}^{d} % {n} = {x}")
        
        if x == 1 or x == n - 1:
            logging.info("Base passes first check (x == 1 or x == n-1)")
            continue
        
        # Square x repeatedly
        for r in range(s - 1):
            x = pow(x, 2, n)
            logging.info(f"Square x: x = {x}")
            if x == n - 1:
                logging.info("Base passes after squaring (x == n-1)")
                break
        else:
            logging.info(f"{n} is not prime (base failed all checks).")
            return False
    
    logging.info(f"{n} is probably prime (passed all rounds).")
    return True

# Ask the user to input a number
user_input = int(input("Enter a number to check if it's prime: "))
iterations = int(input("Iterations: "))
miller_rabin(user_input, k=iterations)
