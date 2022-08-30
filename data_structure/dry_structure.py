
# array
class MyArray():
    def __init__(self, capacity) -> None:
        self.array = [None] * capacity
        self.size = 0

    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise Exception("超出数据实际元素范围！")

        # 从右向左循环，逐个元素向右挪一位
        for i in range(self.size-1, -1, -1):
            self.array[i+1] = self.array
        # 腾出的位置放入新元素
        self.array[index] = element
        self.size += 1

    def insert_v2(self, index, element):
        if index < 0 or index > self.size:
            raise Exception("超出数据实际元素范围！")
        if self.size >= len(self.array):
            self.resize()

        # 从右向左循环，逐个元素向右挪一位
        for i in range(self.size-1, -1, -1):
            self.array[i+1] = self.array
        # 腾出的位置放入新元素
        self.array[index] = element
        self.size += 1

    def resize(self):
        array_new = [None] * len(self.array) * 2

        for i in range(self.size):
            array_new[i] = self.array[i]
        self.array = array_new

    def output(self):
        for i in range(self.size):
            print(self.array[i])


array = MyArray(4)
array.insert_v2(0, 10)
array.insert_v2(0, 11)
array.insert_v2(0, 12)
array.insert_v2(0, 13)
array.insert_v2(0, 14)
array.insert_v2(0, 15)
array.insert_v2(6, 16)
array.output()
