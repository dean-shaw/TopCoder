import unittest
import itertools



def lcs(a, b):
	lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
	# row 0 and column 0 are initialized to 0 already
	for i, x in enumerate(a):
		for j, y in enumerate(b):
			if x == y:
				lengths[i+1][j+1] = lengths[i][j] + 1
			else:
				lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
	# read the substring out from the matrix
	result = ""
	x, y = len(a), len(b)
	while x != 0 and y != 0:
		if lengths[x][y] == lengths[x-1][y]:
			x -= 1
		elif lengths[x][y] == lengths[x][y-1]:
			y -= 1
		else:
			assert a[x-1] == b[y-1]
			result = a[x-1] + result
			x -= 1
			y -= 1
	# print("LCS {0} {1} is {2}".format(a, b, result))
	return result

class ConstructLCSEasy(unittest.TestCase):

	def construct(self, AB, BC, CA):
		B = "1"*BC
		zero_A = CA - AB
		A = "1"*AB + "0"*zero_A
		zero_C = zero_A
		C = "1"*BC + "0"*zero_C
		# return "1111 101 1010101"
		print( A + " " + B + " " + C)
		return A + " " + B + " " + C

	def test_inputs(self):
		test_cases = [
			(2,3,4),
			(4,4,7),
			(6,7,8),
			(7,8,8),
			(15,17,19),
			(50,50,50)
		]
		for (AB, BC, CA) in test_cases:
			print("Test Case {0}".format((AB,BC,CA)))
			strings = self.construct(AB, BC, CA)
			(A, B, C) = strings.split(" ")
			self.assertEqual(len(lcs(A, B)), AB)
			self.assertEqual(len(lcs(B, C)), BC)
			self.assertEqual(len(lcs(C, A)), CA)


if __name__ == '__main__':
	unittest.main()