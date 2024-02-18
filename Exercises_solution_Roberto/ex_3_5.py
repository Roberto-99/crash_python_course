from ex_3_1 import divisible
from ex_3_4 import find_primes


def find_factors(n):
    """A function that calculates the prime factors of a number n
    Parameters
    ----------
    n : int 
        must be a positive integer

    Returns
    -------
    : list
        a list of all the prime factors of n
    """
    #check that the input is valid
    if not(isinstance(n,int) and n>=0):
        raise TypeError("Invalid Input only positive integers allowed")

    
    #adding an exception the edge case of n=1 
    if n<=1:
        f=[n]
    #find all the prime numbers up to n 
    else:
        f=[]
        p=find_primes(n)
        #for each of the primes if n is divisible by it divide by it and then add it to the list of factors,
        #repeat until n is not divisible by that prime anymore
        for i in p:
            while divisible(n,i):
                f.append(i)
                n=n/i
    return f



    
        
        
        
#here I check if functions work by introducing a test when the file is run   
if __name__ == '__main__' :
    def _test (x) :
        #find the primes up to x 
        p=find_primes(x)
        #check that the function works for 1
        c=find_factors(1)==[1]
        #for each number up to 100 check that the function returns a list whose elements are primes 
        #which when multiplied together give back the initial number, if this is false for any element in x
        #the test will print False, if it works for every element, it will print True
        for i in range(2,x+1):
            f=find_factors(i)
            m=1
            for a in f:
                m=m*a
                if not(a in p):
                    c=False
            if not(m==i):
                c=False
        return c
    #test for all numbers up to 100
    print(_test(100))
