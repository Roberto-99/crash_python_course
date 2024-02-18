def find_primes(n):
    """A function that calculates the prime numbers up to a number n
    Parameters
    ----------
    n : int 
        the upper boundary of the range of numbers we want to check for primes in, must be a positive integer

    Returns
    -------
    : list
        a list of prime numbers from 2 to n
    """
    #check that the input is valid
    if not(isinstance(n,int) and n>0):
        print("Invalid Input only positive integers allowed")
    #creating a list of all numbers from 2 to n
    primes=list(range(2,n+1))
    i=0
    #removing all elements of the list that can be divided by 2 and then doing the same for the next prime number until there
    #are no more prime numbers smaller then n
    for i in range(len(primes)):
        if i>=len(primes):
            pass
        else:
            p=primes[i]
            for a in range(p,(n//p)+1):
                try:
                    primes.remove(p*a)
                except ValueError:
                    pass
    return primes
#here I check if functions work by printing the primes smaller then 100 ,
#the printed list should be: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
if __name__ == '__main__' :
    print("the primes smaller then 100 are: ")
    print(find_primes(100))