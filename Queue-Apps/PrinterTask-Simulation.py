import random
class Queue:
    class Stack:
        def __init__(self):
            self.items = []

        def enqueue(self, item):
            self.items.insert(0, item)

        def dequeue(self):
            return self.items.pop(0)

        def size(self):
            return len(self.items)

        def isEmpty(self):
            return self.items == []


class Printer:
    def __init__(self, pageperminute):
        self.pagerate = pageperminute
        self.currenttask = None
        self.timeremaining = 0

    def tick(self):
        if self.currenttask:
            self.timeremaining -= 1
            if self.timeremaining == 0:
                self.currenttask = None

    def busy(self):
        return self.currenttask != None

    def startnext(self, newtask):
        self.currenttask = newtask
        self.timeremaining = newtask.getpages() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getstamp(self):
        return self.timestamp

    def getpages(self):
        return self.pages

    def waittime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numseconds, pagerate):
    labprinter=Printer()
    Queueprinter=Queue()
    averagtime=[]
    for currenttime in range(numseconds):
        if random.randrange(1,181)==180:
            newtask=Task(currenttime)
            Queueprinter.enqueue(newtask)
        if (not Queueprinter.isEmpty() and not labprinter.busy()):
            temp=Queueprinter.dequeue()
            averagtime.append(temp.waittime(currenttime))
            labprinter.startnext(temp)
        labprinter.tick()
    averagewait=sum(averagtime)/len(averagtime)
