class Graph(object):
	
	def __init__(self):
		self.graph = {}


	def add_edge(self, u, v):
		self.graph[u] = [v]


	# def BFS(self, origin):
	# 	q = []
	# 	q.append(origin)
	# 	tracker = (origin,)
	# 	while q:
	# 		cur = q.pop(0)
	# 		for el in self.graph[cur]:
	# 			if el not in tracker:
	# 				q.append(el)
	# 				tracker += (el,)
	# 	return tracker


	def BFS(self, origin):
		q, visited = [origin], ()
		while q:
			cur = q.pop(0)
			for n in self.graph[cur]:
				if cur not in visited:
					visited += (cur,)
					q.append(n)
		return visited


	def DFS(self, origin, tracker):
		if origin == None:
			return -1
		tracker += (origin,)
		for n in self.graph[origin]:
			print ng
			if n not in tracker:
				self.DFS(n, tracker)
		

g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 5)
g.add_edge(5, 7)
g.add_edge(7, 1)
# print g.BFS(2)



g.DFS(1, tracker=(1,))