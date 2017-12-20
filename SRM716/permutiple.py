import unittest
import itertools


class Permutiple(unittest.TestCase):

	def counts_from_int(self, integer):
		int_list = [i for i in str(integer)]
		int_counts = {element:int_list.count(element) for element in int_list}
		return int_counts

	def isPermutiple_hard(self, x):
		x_counts = self.counts_from_int(x)
		for c in range(2,10):
			multiple = x * c
			multiple_counts = self.counts_from_int(multiple)
			if set(x_counts) == set(multiple_counts):
				return "Possible"
		return "Impossible"


	def isPermutiple(self, x):
		x_list = [i for i in str(x)]
		permutations = itertools.permutations(x_list)
		for perm in permutations:
			num = int("".join(list(perm)))
			if num != x and num % x == 0:
				# print("num {0} multiple of {1}".format(num, x))
				return "Possible"
		return "Impossible"

	def test_inputs(self):
		test_cases = [
			(142857, "Possible"),
			(14, "Impossible"),
			(1035, "Possible"),
			(1000000, "Impossible"),
			(100035, "Possible"),
			(4, "Impossible")
		]
		for (test_input, expected_output) in test_cases:
			self.assertEqual(self.isPermutiple_hard(test_input), expected_output)


if __name__ == '__main__':
	unittest.main()