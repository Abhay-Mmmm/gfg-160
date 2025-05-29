class Solution:
	def addBinary(self, s1, s2):
		a = int(s1, 2)  # int(string,base) so for binary we put base = 2
		b = int(s2, 2)

		result = a + b

		return bin(result)[2:]  # Return a binary starting with '0b' this is a way of python showing
		# the number is a binary one!!!