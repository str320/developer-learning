def classify(number):
    """ A perfect number equals the sum of its positive divisors."""
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    total = aliquot_sum(number)

    if total == number:
        return "perfect"
    
    if total > number:
        return "abundant"
    
    return "deficient"

def aliquot_sum(number):
    factors = []

    for candidate in range(1, number):
        if number % candidate == 0:
            factors.append(candidate)

    return sum(factors)