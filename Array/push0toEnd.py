class Solution:
	def pushZerosToEnd(self, arr):
		idx = 0
		for i in range(len(arr)):
			if arr[i] != 0:
				arr[idx] = arr[i]
				idx += 1

		while idx < len(arr):
			arr[idx] = 0
			idx += 1

		return arr