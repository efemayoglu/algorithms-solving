class Queue2Stacks(object):
    def __init__(self):

        self.instack = []
        self.outstack = []

    def enqueue(self, element):
        self.instack.append(element)

        #[0,1,2,3,4]


    def dequeue(self):
        # self.stack2 = list(reversed(self.stack1))
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        
        return self.outstack.pop()


q2 = Queue2Stacks()

for i in range(5):
    q2.enqueue(i)

for i in range(5):
    print(q2.dequeue())