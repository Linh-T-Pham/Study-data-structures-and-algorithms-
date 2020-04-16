# https://fellowship.hackbrightacademy.com/materials/challenges/circular-array/index.html

class CircularArray(object):
    """An array that may be rotated, and items retrieved by index"""

    def __init__(self):
        """Instantiate CircularArray."""
        self.items = []


    def add_item(self, item):
        """Add item to array, at the end of the current rotation."""
        self.items.append(item)


    def get_by_index(self, index):
        """Return the data at a particular index."""
        return self.items[index]

    def rotate(self, rotate_by):
        rotate_by %= len(self.items)
    
        if rotate_by == 0:
            return

        self.items = [rotate_by:] + [:rotate_by]