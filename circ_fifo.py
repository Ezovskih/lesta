class CircularBufferList:
    """
    + Нет зависимости от дополнительных библиотек.
    + Больше возможностей для расширения логики.
    - Большой недозаполненный буфер может занимать память.
    - На выполнение операций (сдвига) требуется больше времени.
    """
    def __init__(self, size):
        self.size = size
        self.buffer = []
        self.start = 0

    def append(self, item):
        if len(self.buffer) < self.size:
            self.buffer.append(item)
        else:
            self.buffer[self.start] = item
            self.start = (self.start + 1) % self.size

    def get(self):
        return self.buffer

    def __len__(self):
        return len(self.buffer)


class CircularBufferDeque:
    """
    + Операции оптимизированы и выполняются за O(1).
    + Не требует отслеживания положения и размера буфера.
    - Использует дополнительную библиотеку, что не всегда допустимо.
    - Больший расход памяти при малом количестве элементов.
    """
    def __init__(self, size):
        from collections import deque
        self.buffer = deque(maxlen=size)

    def append(self, item):
        self.buffer.append(item)

    def get(self):
        return list(self.buffer)

    def __len__(self):
        return len(self.buffer)


if __name__ == "__main__":
    BUFFER_SIZE = 10
    VALUES = range(100)


    def test_list():
        cb_list = CircularBufferList(BUFFER_SIZE)
        for i in VALUES:
            cb_list.append(i)
            cb_list.get()


    def test_deque():
        cb_deque = CircularBufferDeque(BUFFER_SIZE)
        for i in VALUES:
            cb_deque.append(i)
            cb_deque.get()


    from timeit import timeit

    TIMES = 1000000
    print("LIST TIME:", timeit(test_list, number=TIMES))  # ~ 8.16
    print("DEQUE TIME:", timeit(test_list, number=TIMES))  # ~ 8.13

'''
В общем случае, `collections.deque` будет быстрее, особенно если предполагается
частая вставка и удаление элементов.
Значительная разница в производительности будет заметна при больших размерах буфера
и частых операциях добавления/удаления.
Для небольших буферов и небольшого числа операций разница может быть менее заметной.
'''
