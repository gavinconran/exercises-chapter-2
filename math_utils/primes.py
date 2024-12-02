import numpy as np

def isprime(x):
    if x == 1:
        return 1 == 0
    else:    
        square_root_x = np.round(np.sqrt(x))
        test_array = [x % i for i in np.arange(2, square_root_x + 1)]
        return 0 not in test_array

