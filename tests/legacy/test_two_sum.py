"""Unit tests for two-sum core functions."""

import unittest
from leetcode19.legacy.two_sum_core import (
    calculate_complement,
    build_number_index_map,
    find_pair_with_hash_map,
    validate_input,
    two_sum_core
)


class TestTwoSumCore(unittest.TestCase):
    """Test cases for two-sum core functions."""

    def test_calculate_complement(self):
        """Test complement calculation."""
        self.assertEqual(calculate_complement(10, 3), 7)
        self.assertEqual(calculate_complement(5, 2), 3)
        self.assertEqual(calculate_complement(0, 0), 0)
        self.assertEqual(calculate_complement(-5, -3), -2)

    def test_build_number_index_map(self):
        """Test building number to index mapping."""
        nums = [2, 7, 11, 15]
        expected = {2: 0, 7: 1, 11: 2, 15: 3}
        self.assertEqual(build_number_index_map(nums), expected)
        
        nums = [1, 1, 1]
        expected = {1: 2}  # Last index for duplicate values
        self.assertEqual(build_number_index_map(nums), expected)

    def test_find_pair_with_hash_map(self):
        """Test finding pairs using hash map approach."""
        # Test case 1: Normal case
        nums = [2, 7, 11, 15]
        target = 9
        result = find_pair_with_hash_map(nums, target)
        self.assertEqual(result, (0, 1))
        
        # Test case 2: Different positions
        nums = [3, 2, 4]
        target = 6
        result = find_pair_with_hash_map(nums, target)
        self.assertEqual(result, (1, 2))
        
        # Test case 3: No solution
        nums = [1, 2, 3]
        target = 7
        result = find_pair_with_hash_map(nums, target)
        self.assertIsNone(result)
        
        # Test case 4: Negative numbers
        nums = [-1, -2, -3, -4]
        target = -7
        result = find_pair_with_hash_map(nums, target)
        self.assertEqual(result, (2, 3))

    def test_validate_input(self):
        """Test input validation."""
        # Valid inputs
        self.assertTrue(validate_input([1, 2, 3], 5))
        self.assertTrue(validate_input([0, 0], 0))
        self.assertTrue(validate_input([-1, 1], 0))
        
        # Invalid inputs
        self.assertFalse(validate_input("not a list", 5))
        self.assertFalse(validate_input([1], 5))  # Too short
        self.assertFalse(validate_input([1, 2], "not a number"))
        self.assertFalse(validate_input([], 5))

    def test_two_sum_core_success(self):
        """Test successful two-sum core function."""
        # Test case 1: Basic case
        nums = [2, 7, 11, 15]
        target = 9
        result = two_sum_core(nums, target)
        self.assertEqual(sorted(result), [0, 1])
        
        # Test case 2: Different target
        nums = [3, 2, 4]
        target = 6
        result = two_sum_core(nums, target)
        self.assertEqual(sorted(result), [1, 2])
        
        # Test case 3: Negative numbers
        nums = [-1, -2, -3, -4]
        target = -7
        result = two_sum_core(nums, target)
        self.assertEqual(sorted(result), [2, 3])

    def test_two_sum_core_no_solution(self):
        """Test two-sum core function with no solution."""
        nums = [1, 2, 3]
        target = 7
        with self.assertRaises(ValueError) as context:
            two_sum_core(nums, target)
        self.assertEqual(str(context.exception), "No two sum solution")

    def test_two_sum_core_invalid_input(self):
        """Test two-sum core function with invalid input."""
        # Invalid nums type
        with self.assertRaises(TypeError) as context:
            two_sum_core("not a list", 5)
        self.assertEqual(str(context.exception), "Invalid input parameters")
        
        # Invalid target type
        with self.assertRaises(TypeError) as context:
            two_sum_core([1, 2, 3], "not a number")
        self.assertEqual(str(context.exception), "Invalid input parameters")
        
        # Too short list
        with self.assertRaises(TypeError) as context:
            two_sum_core([1], 5)
        self.assertEqual(str(context.exception), "Invalid input parameters")


class TestSolutionClass(unittest.TestCase):
    """Test cases for the Solution class."""

    def setUp(self):
        """Set up test fixtures."""
        from leetcode19.legacy.twoSum import Solution
        self.solution = Solution()

    def test_solution_basic_case(self):
        """Test Solution class with basic case."""
        nums = [2, 7, 11, 15]
        target = 9
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), [0, 1])

    def test_solution_edge_cases(self):
        """Test Solution class with edge cases."""
        # Test with negative numbers
        nums = [-1, -2, -3, -4]
        target = -7
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), [2, 3])
        
        # Test with zero
        nums = [0, 4, 3, 0]
        target = 0
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), [0, 3])


if __name__ == '__main__':
    unittest.main()