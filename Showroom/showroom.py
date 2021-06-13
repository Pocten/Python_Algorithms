class Node:
    def __init__(self, nextNode, prevNode, data):
        self.nextNode = None
        self.prevNode = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None


    def put_in_list(self, newData):
        newNode = Node(None, None, newData)
        if self.head is None:
            self.head = newNode
            return

        if newNode.data.price < self.head.data.price:
            newNode.nextNode = self.head
            self.head.prevNode = newNode
            self.head = newNode
            return

        cartime = self.head
        while cartime.data.price <= newNode.data.price and cartime.nextNode is not None:
            cartime = cartime.nextNode

        trueNextNode = cartime.nextNode
        if newNode.data.price >= cartime.data.price:
            if trueNextNode is not None:
                trueNextNode.prevNode = newNode
            newNode.prevNode = cartime
            newNode.nextNode = cartime.nextNode
            cartime.nextNode = newNode
            return

        truePrevNode = cartime.prevNode
        newNode.nextNode = cartime
        cartime.prevNode = newNode
        newNode.prevNode = truePrevNode
        truePrevNode.nextNode = newNode



class Car:
    def __init__(self, identification, name, brand, price, active):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active





db = LinkedList()





def init(cars):
    for car in cars:
        db.put_in_list(car)


def add(car):
    db.put_in_list(car)


def updateName(identification, name):
    cartime = db.head
    while cartime is not None:
        if cartime.data.identification == identification:
            cartime.data.name = name
            return
        cartime = cartime.nextNode

def updateBrand(identification, brand):
    cartime = db.head
    while cartime is not None:
        if cartime.data.identification == identification:
            cartime.data.brand = brand
            return
        cartime = cartime.nextNode

def activateCar(identification):
    cartime = db.head
    while cartime is not None:
        if cartime.data.identification == identification:
            cartime.data.active = True
            return
        cartime = cartime.nextNode

def deactivateCar(identification):
    cartime = db.head
    while cartime is not None:
        if cartime.data.identification == identification:
            cartime.data.active = False
            return
        cartime = cartime.nextNode


def getDatabaseHead():
    return db.head


def getDatabase():
    return db


def calculateCarPrice():
    cartime = db.head
    result = 0
    while cartime is not None:
        if cartime.data.active:
            result += cartime.data.price
        cartime = cartime.nextNode
    return result



def clean():
    db.head = None











