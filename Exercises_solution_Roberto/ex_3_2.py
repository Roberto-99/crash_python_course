def fibonacci (n) :
    """A function that calculates the Fibonacci sequence up to the n-th term

    Parameters
    ----------
    n : int 
        the n-th term of the sequence

    Returns
    -------
    : list
        a list with the Fibonacci sequence
    """
    #check that the input is valid
    if not(isinstance(n,int) and n>=0):
        print("Invalid Input only non-negative integers allowed")
    #adding two exception cases for the edge cases of an empty list or a list of size 1
    elif n==0:
        return []
    elif n==1:
        return [0]
    #calculating the terms of the fibonacci sequence up to the nth term
    else:
        fib=[0,1]
        for i in range(n-2):
            fib.append(fib[-1]+fib[-2])
        return fib

def fibonacci_odd (n) :
    """A function that calculates the odd index Fibonacci sequence up to the n-th term

    Parameters
    ----------
    n : int 
        the n-th term of the sequence

    Returns
    -------
    : list
        a list with the odd terms of the Fibonacci sequence
    """
    #check that the input is valid
    if not(isinstance(n,int) and n>=0):
        print("Invalid Input only non-negative integers allowed")
    #adding an exception the edge case of list of size smaller then 1
    elif n==0:
        return []
    #calculating the off terms of the fibonacci sequence up to the nth term
    else:
        fib=[0]
        even=1
        for i in range((n-1)//2):
            even=even+fib[-1]
            fib.append(fib[-1]+even)
        return fib
def fibonacci_even (n) :
    """A function that calculates the even index Fibonacci sequence up to the n-th term

    Parameters
    ----------
    n : int 
        the n-th term of the sequence

    Returns
    -------
    : list
        a list with the even terms of Fibonacci sequence
    """
    #check that the input is valid
    if not(isinstance(n,int) and n>=0):
        print("Invalid Input only non-negative integers allowed")
    #adding an exception cases for the edge case a list of size smaller then 2
    elif (n)//2==0:
        return []
    #calculating the even terms of the fibonacci sequence up to the nth term
    else:
        fib=[1]
        odd=0
        for i in range((n-2)//2):
            odd=odd+fib[-1]
            fib.append(fib[-1]+odd)
        return fib
    
        
        
        
#here I check if functions work by introducing various test when the file is read, 
#all tests print True if the function is working as expected, False otherwhise          
if __name__ == '__main__' :
    #here i introduce the actual Fibonacci sequence values to check against
    Fibonacci10=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    Fibonacci10_odd=[0, 1, 3, 8, 21]
    Fibonacci10_even=[1, 2, 5, 13, 34]
    #here i introduce the tests for the various functions
    def _test (x) :
        result = fibonacci(x)
        if isinstance(x,int) and x>=0:
            print(result==Fibonacci10[:x])
        else:
            print(result==None)
    def _test_odd (x) :
        result = fibonacci_odd(x)
        if isinstance(x,int) and x>=0:
            print(result==Fibonacci10_odd[:(x+1)//2])
        else:
            print(result==None)
    def _test_even (x) :
        result = fibonacci_even(x)
        if isinstance(x,int) and x>=0:
            print(result==Fibonacci10_even[:x//2])
        else:
            print(result==None)
    #here i execute the tests    
    _test(0)
    _test(1)
    _test(2)
    _test(3)
    _test(-1)
    _test(5.2)
    _test("string")
    _test("10")
    _test(10.0)
    _test(10)
    _test_odd(0)
    _test_odd(1)
    _test_odd(2)
    _test_odd(3)
    _test_odd(-1)
    _test_odd(5.2)
    _test_odd("string")
    _test_odd("10")
    _test_odd(10.0)
    _test_odd(10)
    _test_even(0)
    _test_even(1)
    _test_even(2)
    _test_even(3)
    _test_even(-1)
    _test_even(5.2)
    _test_even("string")
    _test_even("10")
    _test_even(10.0)
    _test_even(10)
   # 3. eventually finalize the program
