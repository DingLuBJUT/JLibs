from itertools import chain,repeat,islice


# ** Iterable objects is implements with __len__ 、__getitem__、__iter__ ** #
class Data:
    def __init__(self):
        self.data = ['title', 'title2', 'title3']

    def __len__(self):
        # get length
        return len(self.data)

    def __getitem__(self, i):
        # get element with index
        return self.data[i]

    def __iter__(self):
        # get element
        for titles in self.data:
            yield titles
# create iterable object
data = Data()
# iterate iterable object
print([e for e in data])
print([data[index] for index in range(len(data))])


# ** Iterator is implements with __iter__ and __next__ ** #
class Data:
    def __init__(self):
        self.data = ['title', 'title2', 'title3']
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.data):
            raise StopIteration()
        return self.data[self.index]
# create Iterator
data = Data()
# iterate Iterator
e1 = next(data)
e2 = next(data)
e3 = next(data)
print(e1,e2,e3)

# ** zip、zip(*) ** #
# [(1,1),(2,2),(3,3)]
print([e for e in zip([1,2,3],[1,2,3])])
# [1,2,3],[1,2,3]
print([e for e in zip(*[(1,1,1),(2,2,2),(3,3,3)])])

# ** chain、repeat、islice ** #
# flatten [1,2,3,4,5]
print(list(chain(*[[1, 2],[3],[4,5]])))
# repeat [0,0,0,0,0]
print(list(repeat(0,5)))
# cut [0,0]
print(list(islice([0,0,0,0],2)))

# ** data expand ** #
# [0, 0, 0, 0, 0]
print([0] * 5)
# (1, 1, 1, 1, 1) 5
print((1,) * 5,(1) * 5)













