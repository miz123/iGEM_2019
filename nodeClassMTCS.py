#Node Class for MTCS_With Distances

import math

class Node:

	#Initial state of the node
	def __init__(self,distance=0,state=None,Q=None,N=None,parent=None):
		self.Q = Q
		self.N = N
		self.distance = distance
		self.children = {}
		self.visited = 0
		self.parent = parent

	#Add child to the node
	def add_child(self,child):
		self.children.append(child)
		child.parent = self

	def add_children(self,children):
		for child in children:
			self.addchild(child)

	#Update Node
	def update(self,distance):
		self.distance = distance
		self.visited+=1

	#Expand Node
	def expand(self,action,state):
		child = Node(state=state,distance=distance,parent=self,Q=Q,N=N)
		self.children.append(child)
		return child
