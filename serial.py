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
    def __init__(self, start=100):
        self.start = self.next = start

    def __repr__(self):
        """this will show the respresentation"""
        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """returns the next serial"""
        self.next +=1
        return self.next -1

    def reset(self):
        "Resets the number to the original starting number"

        self.next = self.start