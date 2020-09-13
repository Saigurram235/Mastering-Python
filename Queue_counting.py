import Queues


def Circles(item, num):
    q = Queues.Queue()
    for i in item:
        q.enqueue(i)
        # print(q.dequeue())
    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue() )
        q.dequeue()
    return q.dequeue()


print(Circles(["Bill", "David", "Susan", "Jane", "Kent","Brad"], 7))