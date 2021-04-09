"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, num):
        """initialize new generator with start and current"""
        self.start = num
        self.current = num
    def generate(self):
        """return current number generator is at and increment current"""
        self.current += 1
        return self.current - 1
    def reset(self):
        """revert current to start"""
        self.current = self.start
    
