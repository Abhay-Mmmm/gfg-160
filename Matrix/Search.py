#User function Template for python3
class Solution:
	def matSearch(self, mat, x):
		n = len(mat)
		m = len(mat[0])
		
		for i in range(n):
			for j in range(m):
				if x == mat[i][j]:
					return True
		
		return False