#Node Class for MTCS_With Distances

import math

class Node:

	#Initial state of the node -Done initially by Michael, made some changes I've signed
    #have commented Michaels original code so we can see
	def __init__(self, distance = 0, Q = None,N = None, parent = None):
		self.Q = Q
		self.N = N
		self.distance = distance
        #Changed the set data structure that was originally for children
        #self.children = {} -Michael
        self.children = []
        #I like this addtition as it allows to see how many paths in game
        #use this node in the tree -IR
		self.visited = 0
        #action/move the node plays in the game tree
        #self.action = state
		self.parent = parent

	#Add child to the node
	def add_child(self, child):
		self.children.append(child)
		child.parent = self
	
    #adds multiple children to the node
	def add_children(self, children):
		for child in children:
			self.addchild(child)

	#Updates node, sets number of times visited and distance
	def update(self, distance):
		self.distance = distance
		self.visited += 1

	#Adds a child given all of the necessary initializers
	def expand(self, action, state):
		child = Node(state=state,distance=distance,parent=self,Q=Q,N=N)
		self.children.append(child)
		return child

    #Get the child based off of a given index for the children list
    def getChild(childIndex):
        return children[childIndex]

    #sets the distance of a child node given it's index and the updated distance
    def updateChild(childIndex, childDistance):
        children[childIndex].distance = childDistance

    #gets parent node
    def getParent():
        return parent

    #sets parent distance given a distance
    def setParent(parentDistance):
        parent.distance = parentDistance
		
