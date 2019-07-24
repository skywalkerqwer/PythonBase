# class NumberIterator:
#     def __init__(self, stop):
#         self.stop = stop
#         self.start = 0
#
#     def __next__(self):
#         if self.start >= self.stop:
#             raise StopIteration
#         temp = self.start
#         self.start += 1
#         return temp

"""
class MyRange:
    def __init__(self, stop):
        self.stop = stop


    def gogogo(self):
        start = 0
        while start< self.stop:
            yield start
            start += 1


for item in MyRange(5).gogogo():
    print(item)
"""


def my_range(stop):
    start = 0
    while start < stop:
        yield start
        start += 1


for item in my_range(5):
    print(item)
