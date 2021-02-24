# ALL VALUES OF LINKED LIST

# return all values in a linked list
# convert binary number to integer

# create linked list
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  # print method for the linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next

# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert(1)
LL.insert(0)
LL.insert(1)
LL.printLL()

# getting all values in linked list
s = ''
node = LL.head
while node:
    s += str(node.data)
    node = node.next

# return binary number to decimal value
print(int(s, 2))