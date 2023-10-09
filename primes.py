"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("You must enter an integer number greater than 0")

    list = []
    prime_counter = 0
    trial_number = 2 # initialize it to first prime number

    while prime_counter < number_of_primes:
        is_prime = True
        if len(list) != 0:
            for prime_number in list:
                if trial_number % prime_number == 0:
                    is_prime = False
        
        if is_prime == True:
            list.append(trial_number)
            prime_counter += 1
        
        trial_number += 1
    
    return list
