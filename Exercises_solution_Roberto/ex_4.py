from ex_3_5 import find_factors  # importing find_factors which is defined in ex_3_5 module

class rational:
    """
    Represents a rational number with a numerator and denominator, each with a precision factor.
    """

    def __init__(self, n, p=0.01):
        """
        Initializes a rational number with a given numerator, denominator precision.

        Parameters:
            n (int, float): Numerator of the rational number.
            p (float): Precision factor for denominator, default is 0.01.
        """
        if not isinstance(n, (int, float)):
            raise TypeError("The input number must be a float or an integer.")
        
        if p <= 0 or p > 1:
            raise ValueError("Precision must be between 0 and 1.")
        else:
            self.n = n
            self.p = p
            # Calculate rounded numerator and denominator based on precision (removing the integer value to increase efficiency)
            self.numerator, self.denominator = round((n-int(n))/p), round(1/p)
      
            # Reduce to simplest form and add back the integer value
            if self.numerator==0:
                self.denominator=1
            else:
                for i in self.find_common(abs(self.numerator), self.denominator):
                    self.numerator, self.denominator = self.numerator / i, self.denominator / i
            self.numerator, self.denominator = int(self.numerator+int(n)*self.denominator), int(self.denominator)

    def __abs__(self):
        """
        Returns the absolute value of the rational number.

        Returns:
            rational: The absolute value of the rational number.
        """
        abs_r = rational(1, 1)
        abs_r.n = abs(self.n)
        abs_r.p = self.p
        abs_r.denominator = abs(self.denominator)
        abs_r.numerator = abs(self.numerator)
        return abs_r

    def __add__(self, other):
        """
        Adds two rational numbers together.

        Parameters:
            other (rational): The rational number to be added.

        Returns:
            rational: The result of the addition.
        """
        if not isinstance(other, rational):
            raise TypeError("Unsupported operand type(s) for +: 'rational' and '{}'"
                            .format(type(other).__name__))
        return rational(self.n + other.n, max(self.p, other.p))
    def __sub__(self, other):
        """
        subtracts two rational numbers together.

        Parameters:
            other (rational): The rational number to be subtracted.

        Returns:
            rational: The result of the subtraction.
        """
        if not isinstance(other, rational):
            raise TypeError("Unsupported operand type(s) for +: 'rational' and '{}'"
                            .format(type(other).__name__))
        return rational(self.n - other.n, max(self.p, other.p))
    def __pos__(self):
        """
        returns itself

        Returns:
            rational: itself.
        """
        
        return self
    def __neg__(self):
        """
        returns minus itself

        Returns:
            rational: minus itself.
        """
        
        return rational(-self.n, self.p)

    def __mul__(self, other):
        """
        Multiplies two rational numbers together.

        Parameters:
            other (rational): The rational number to be multiplied.

        Returns:
            rational: The result of the multiplication.
        """
        if not isinstance(other, rational):
            raise TypeError("Unsupported operand type(s) for *: 'rational' and '{}'"
                            .format(type(other).__name__))
        return rational(self.n * other.n, max(self.p, other.p))

    def __eq__(self, other):
        """
        Checks if two rational numbers are equal.

        Parameters:
            other (rational): The rational number to be compared.

        Returns:
            bool: True if the numbers are equal, False otherwise.
        """
        if not isinstance(other, rational):
            return False
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __gt__(self, other):
        """
        Checks if the current rational number is greater than another.

        Parameters:
            other (rational): The rational number to be compared.

        Returns:
            bool: True if the current number is greater, False otherwise.
        """
        if not isinstance(other, rational):
            raise TypeError("Unsupported operand type(s) for >: 'rational' and '{}'"
                            .format(type(other).__name__))
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __int__(self):
        """
        Converts the rational number to an integer.

        Returns:
            int: The integer representation of the rational number.
        """
        return int(self.n)

    def __float__(self):
        """
        Converts the rational number to a float.

        Returns:
            float: The float representation of the rational number.
        """
        return float(self.n)
        
    def __str__(self):
        """
        Returns the string representation of the rational number.

        Returns:
            str: The string representation of the rational number.
        """
        return f'{self.numerator}/{self.denominator}'

    def __repr__(self):
        """
        Returns the official string representation of the rational number.

        Returns:
            str: The official string representation of the rational number.
        """
        return f'rational({self.n}, precision={self.p})'
    
    def find_common(self, n, m):
        """
        Finds common factors between two numbers.

        Parameters:
            n (int): First number.
            m (int): Second number.

        Returns:
            list: List of common factors between n and m.
        """
        fn, fm = find_factors(n), find_factors(m)
        fc = []
        for a in fn:
            if a in fm:
                fm.remove(a)
                fc.append(a)
        return fc
