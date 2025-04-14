# Name: Miguel Angelo B. Basinillo
# Section: BSIT 2A
# MODULE 8 - Formative Test
# 3. Define a class called MyRange that acts as an iterator and generates numbers from a start value to an end value (inclusive). Implement the __iter__() and __next__() methods to iterate through the range.

class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            num = self.current
            self.current += 1
            return num

my_range = MyRange(1, 5)

for num in my_range:
    print(num, end=" ")