# from testheap import EmptyHeapException


def left(index):
    '''Return index's left child index.
    '''
    return index * 2 + 1


def right(index):
    '''Return index's left child index.
    '''
    return index * 2 + 2


def parent(index):
    '''Return index's parent index.'''

    return (index - 1) // 2


class MinHeap:

    def __init__(self, L=None):
        '''Create a new MinHeap.
        This method is complete.'''

        if not L:
            self._data = []
        else:
            self._data = L
            self._min_heapify()

    def __len__(self):
        '''Return the length of the MinHeap.
        This method is complete.'''

        return len(self._data)

    def __str__(self):
        '''Return a string representation of the heap.
        This method is complete.'''

        return str(self._data)

    def insert(self, v):
        """Insert v in self. Maintain heap property."""

        self._data.append(v)
        self._percolate_up()

    def extract_min(self):
        """Remove minimal value in self. Restore heap property.
        Raise EmptyHeapException if heap is empty."""
        if len(self._data) == 0:
            raise Exception('heap is empty')
        temp = self._data[0]
        self._data[0] = self._data[-1]
        self._data.pop()
        self._percolate_down(0)

    def _percolate_up(self):
        """Restore heap property of self after
        adding new item"""

        index = len(self._data) - 1
        while index > 0:
            if self._data[parent(index)] > self._data[index]:
                self._data[parent(index)], self._data[index] = self._data[index], self._data[index // 2]
            else:
                break

    def _percolate_down(self, i):
        """ Restore heap property of subtree
        rooted at index i.
        """

        # while larger than at least one child

        while left(i) <= self.__len__() - 1:
            if right(i) > self.__len__() - 1:
                min_child = left(i)
            else:
                if self._data[left(i)] < self._data[right(i)]:
                    min_child = left(i)
                else:
                    min_child = right(i)
            # swap with smaller child and repeat
            if self._data[min_child] < self._data[i]:
                self._data[i], self._data[min_child] = self._data[min_child], self._data[i]
            i = min_child

    def _min_heapify(self):
        """Turn unordered list into min-heap."""

        # for each node in the first half of the list
        node = left(self.__len__() - 1)
        for i in range (left(node), -1, -1):
            # percolate down
            self._percolate_down(i)

