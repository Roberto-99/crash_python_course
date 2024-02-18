def divisible (n,d):
    """A function that checks if two numbers are divisible or not
    Parameters
    ----------
    n : int 
        the numerator
    d : int 
        the denominator

    Returns
    -------
    : boolean
        returns True if the two numbers are divisible,
        False otherwise
    """
    return 0==n%d


def IsDivisible_restricted():
    """A game to check if a number is divisible by 2,3,5,7, 
    the number is inputted by the player and must be a positive integer
    Parameters
    ----------
    None
    
    Returns
    -------
    : None
    """
    x=0
    #Here i keep asking the player to input a natural integer until they
    #give a valid value (a positive integer)
    while not(x>0):
        try:
          # try converting to integer
          x=int(input("Enter your number: "))
        except ValueError:
            x=0
        if not(x>0):
            print("Invalid Input, only positive integers allowed")
    #here I check in the number is divisible by 2, 3, 5 and 7 and
    #inform the player accordingly
    for i in [2,3,5,7]:
        if divisible (x,i):
            print(str(x)+" is divisible by "+ str(i))
        else:
            print(str(x)+" is not divisible by "+ str(i))     
                
def IsDivisible_free():
    """A game to check if 2 numbers are divisible by each other, 
    the numbers are inputted by the player and must be a positive integer
    Parameters
    ----------
    None
    
    Returns
    -------
    : None
    """
    x=0
    y=0
    #Here i keep asking the player to input a natural integer until they
    #give a valid value (a positive integer)
    while not(x>0):
        try:
          # try converting to integer
          x=int(input("Enter your number: "))
        except ValueError:
            x=0
        if not(x>0):
            print("Invalid Input, only positive integers allowed")
    #Here i keep asking the player to input a natural integer until they
    #give a valid value (a positive integer)
    while not(y>0):
        try:
          # try converting to integer
          y=int(input("Enter a second number: "))
        except ValueError:
            y=0
        if not(y>0):
            print("Invalid Input, only positive integers allowed")
    #here I check in the number are divisible by each other and
    #inform the player accordingly
    if divisible (x,y):
        print(str(x)+" is divisible by "+ str(y))
    else:
        print(str(x)+" is not divisible by "+ str(y))
    if divisible (y,x):
        print(str(y)+" is divisible by "+ str(x))
    else:
        print(str(y)+" is not divisible by "+ str(x))
        
        
#here I check if the games work when by testing the 2 functions when the file is read    
if __name__ == '__main__' :
    IsDivisible_restricted()
    IsDivisible_free()