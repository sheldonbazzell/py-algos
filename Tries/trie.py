class TrieNode(object):

	def __init__(self, data):
		self.data = data
		self.next = {}
		self.end = False

		
	def __repr__(self):
		return "data: {}, end: {}, next: {}\n".format(self.data, self.end, self.next)

class Trie(object):

	def __init__(self):
		self.root = {}


	def __repr__(self):
		return "root: {}".format(self.root)


	def insert(self, word):
		if word[0] not in self.root:
			self.root[word[0]] = TrieNode(word[0])
		cur = self.root[word[0]]
		for ch in word[1:]:
			if ch not in cur.next:
				cur.next[ch] = TrieNode(ch)
			cur = cur.next[ch]
		cur.end = True
		return self


	def validWord(self, word):
		if word[0] not in self.root:
			return False
		else:
			cur = self.root[word[0]]
			for ch in word[1:]:
				if ch not in cur.next:
					break
				cur = cur.next[ch]
			return cur.end == True


my_trie = Trie()
my_trie.insert('hello').insert('hey').insert('cat')
print my_trie.validWord('cat')
