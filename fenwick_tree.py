class FenwickTree:
	def __init__(self, arr):              # Initialise Fenwick Tree with given array
		self.n = len(arr) 
		self.bit = [0]*self.n
		for i in range(len(arr)):
			self.add(i, arr[i])

	def add(self, ind, delta):            # Add 'delta' to index 'ind' of the array
		while ind < self.n:
			self.bit[ind] += delta
			ind = (ind | (ind + 1))

	def sum(self, idx):                   # Helper Function to answer for queries
		ans = 0
		while idx >= 0:
			ans += self.bit[idx]
			idx = (idx & (idx + 1)) - 1
		return ans

	def query(self, start, end):          # Find sum of the element of array in the range [start,end]
		return self.sum(end) - self.sum(start - 1)


n = int(input())
arr = list(map(int, input().split()))
FT = FenwickTree(arr)