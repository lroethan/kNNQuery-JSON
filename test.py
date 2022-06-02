from fibonacci_heap import FibonacciHeap


# 初始化斐波那契堆
f = FibonacciHeap()

f.insert(10)
f.insert(2)
f.insert(15)
f.insert(6)

m = f.find_min()
print(m.data) # 2

q = f.extract_min()
print(q.data) # 2

q = f.extract_min()
print(q.data) # 6

f2 = FibonacciHeap()
f2.insert(100)
f2.insert(56)

f3 = f.merge(f2)
x = f3.root_list.right # pointer to random node
f3.decrease_key(x, 1)

# print the root list using the iterate class method
print([x.data for x in f3.iterate(f3.root_list)]) # [10, 1, 56]

q = f3.extract_min()
print(q.data) # 1