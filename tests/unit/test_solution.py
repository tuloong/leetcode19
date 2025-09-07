"""Unit tests for the main Solution class."""

import pytest
from unittest.mock import Mock, patch
from leetcode19 import Solution
from tests.fixtures.two_sum_fixtures import TwoSumTestData


class TestSolutionClass:
    """Test cases for the Solution class."""
    
    def test_default_algorithm(self):
        """Test Solution with default algorithm."""
        solution = Solution()
        assert isinstance(solution.solver, type(solution.solver))
    
    def test_hashmap_algorithm(self):
        """Test Solution with hashmap algorithm."""
        solution = Solution("hashmap")
        result = solution.twoSum([2, 7, 11, 15], 9)
        assert sorted(result) == [0, 1]
    
    def test_bruteforce_algorithm(self):
        """Test Solution with bruteforce algorithm."""
        solution = Solution("bruteforce")
        result = solution.twoSum([2, 7, 11, 15], 9)
        assert sorted(result) == [0, 1]
    
    def test_twopointer_algorithm(self):
        """Test Solution with twopointer algorithm."""
        solution = Solution("twopointer")
        result = solution.twoSum([2, 7, 11, 15], 9)
        assert sorted(result) == [0, 1]
    
    def test_algorithm_case_insensitive(self):
        """Test that algorithm names are case insensitive."""
        solution1 = Solution("HASHMAP")
        solution2 = Solution("hashmap")
        solution3 = Solution("HashMap")
        
        nums = [2, 7, 11, 15]
        target = 9
        
        result1 = solution1.twoSum(nums, target)
        result2 = solution2.twoSum(nums, target)
        result3 = solution3.twoSum(nums, target)
        
        assert sorted(result1) == sorted(result2) == sorted(result3) == [0, 1]
    
    @pytest.mark.parametrize("test_case", TwoSumTestData.BASIC_CASES)
    def test_basic_cases(self, test_case):
        """Test Solution with basic test cases."""
        solution = Solution()
        nums = test_case["nums"]
        target = test_case["target"]
        expected = test_case["expected"]
        
        result = solution.twoSum(nums, target)
        assert sorted(result) == sorted(expected)
    
    @pytest.mark.parametrize("test_case", TwoSumTestData.EDGE_CASES)
    def test_edge_cases(self, test_case):
        """Test Solution with edge cases."""
        solution = Solution()
        nums = test_case["nums"]
        target = test_case["target"]
        expected = test_case["expected"]
        
        result = solution.twoSum(nums, target)
        assert sorted(result) == sorted(expected)
    
    @pytest.mark.parametrize("test_case", TwoSumTestData.NO_SOLUTION_CASES)
    def test_no_solution_cases(self, test_case):
        """Test Solution with no solution cases."""
        solution = Solution()
        nums = test_case["nums"]
        target = test_case["target"]
        expected_error = test_case["expected_error"]
        
        with pytest.raises(ValueError, match="No two sum solution"):
            solution.twoSum(nums, target)
    
    def test_invalid_algorithm(self):
        """Test Solution with invalid algorithm."""
        with pytest.raises(ValueError, match="Unsupported algorithm"):
            Solution("invalid_algorithm")
    
    def test_solution_compatibility(self):
        """Test that Solution class maintains backward compatibility."""
        # Test that it works exactly like the original Solution class
        solution = Solution()
        
        # Test the original examples
        result1 = solution.twoSum([2, 7, 11, 15], 9)
        assert sorted(result1) == [0, 1]
        
        result2 = solution.twoSum([3, 2, 4], 6)
        assert sorted(result2) == [1, 2]
        
        result3 = solution.twoSum([3, 3], 6)
        assert sorted(result3) == [0, 1]
    
    def test_solution_with_different_algorithms(self):
        """Test Solution with different algorithms on same input."""
        nums = [2, 7, 11, 15]
        target = 9
        
        # Test with different algorithms
        solvers = [
            Solution("hashmap"),
            Solution("bruteforce"),
            Solution("twopointer")
        ]
        
        results = []
        for solver in solvers:
            result = solver.twoSum(nums, target)
            results.append(sorted(result))
        
        # All should produce the same result
        assert all(r == [0, 1] for r in results)
    
    def test_solution_error_handling(self):
        """Test Solution error handling."""
        solution = Solution()
        
        # Test invalid inputs
        with pytest.raises(TypeError):
            solution.twoSum("not a list", 5)
        
        with pytest.raises(TypeError):
            solution.twoSum([1, 2, 3], "not a number")
        
        with pytest.raises(TypeError):
            solution.twoSum([1], 5)
    
    def test_solution_method_signature(self):
        """Test that Solution.twoSum method has correct signature."""
        solution = Solution()
        
        # Test that it accepts list and int, returns list
        result = solution.twoSum([2, 7, 11, 15], 9)
        assert isinstance(result, list)
        assert len(result) == 2
        assert all(isinstance(i, int) for i in result)
    
    def test_solution_multiple_calls(self):
        """Test that Solution can be used multiple times."""
        solution = Solution()
        
        # Multiple calls should work independently
        result1 = solution.twoSum([2, 7, 11, 15], 9)
        result2 = solution.twoSum([3, 2, 4], 6)
        result3 = solution.twoSum([3, 3], 6)
        
        assert sorted(result1) == [0, 1]
        assert sorted(result2) == [1, 2]
        assert sorted(result3) == [0, 1]