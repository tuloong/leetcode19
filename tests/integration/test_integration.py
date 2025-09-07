"""Integration tests for two-sum functionality."""

import pytest
import time
from leetcode19 import Solution
from leetcode19.algorithms import get_solver
from tests.fixtures.two_sum_fixtures import TwoSumTestData


class TestPerformanceIntegration:
    """Integration tests for performance and large datasets."""
    
    @pytest.mark.parametrize("test_case", TwoSumTestData.PERFORMANCE_CASES)
    def test_hashmap_performance(self, test_case):
        """Test HashMapSolver performance with large datasets."""
        solver = get_solver("hashmap")
        nums = test_case["nums"]
        target = test_case["target"]
        expected = test_case["expected"]
        
        start_time = time.time()
        result = solver.solve(nums, target)
        end_time = time.time()
        
        assert sorted(result) == sorted(expected)
        
        # Should complete in reasonable time (less than 1 second for these sizes)
        assert end_time - start_time < 1.0
    
    @pytest.mark.slow
    def test_bruteforce_performance_limitations(self):
        """Test that BruteForceSolver has performance limitations."""
        solver = get_solver("bruteforce")
        
        # Small dataset should work
        nums = list(range(100))
        target = 197
        result = solver.solve(nums, target)
        assert sorted(result) == [98, 99]
        
        # Large dataset should be slow (but we won't test very large ones in CI)
        # This is more of a conceptual test
    
    @pytest.mark.slow
    def test_twopointer_performance(self):
        """Test TwoPointerSolver performance."""
        solver = get_solver("twopointer")
        
        # Large dataset
        nums = list(range(10000))
        target = 19997
        expected = [9998, 9999]
        
        start_time = time.time()
        result = solver.solve(nums, target)
        end_time = time.time()
        
        assert sorted(result) == sorted(expected)
        
        # Should complete in reasonable time
        assert end_time - start_time < 1.0


class TestSolutionIntegration:
    """Integration tests for the complete Solution class."""
    
    def test_end_to_end_workflow(self):
        """Test complete workflow from input to result."""
        # Test with multiple scenarios
        test_scenarios = [
            {
                "input": {"nums": [2, 7, 11, 15], "target": 9},
                "expected": [0, 1]
            },
            {
                "input": {"nums": [3, 2, 4], "target": 6},
                "expected": [1, 2]
            },
            {
                "input": {"nums": [-1, -2, -3, -4], "target": -7},
                "expected": [2, 3]
            }
        ]
        
        for scenario in test_scenarios:
            solution = Solution()
            result = solution.twoSum(**scenario["input"])
            assert sorted(result) == sorted(scenario["expected"])
    
    def test_multiple_algorithm_usage(self):
        """Test using multiple algorithms in sequence."""
        nums = [2, 7, 11, 15]
        target = 9
        
        algorithms = ["hashmap", "bruteforce", "twopointer"]
        results = []
        
        for algorithm in algorithms:
            solution = Solution(algorithm)
            result = solution.twoSum(nums, target)
            results.append(sorted(result))
        
        # All algorithms should produce the same result
        assert all(r == [0, 1] for r in results)
    
    def test_error_handling_integration(self):
        """Test error handling across the entire integration."""
        solution = Solution()
        
        # Test various error scenarios
        error_scenarios = [
            {
                "input": {"nums": [], "target": 5},
                "error": "TypeError"
            },
            {
                "input": {"nums": [1], "target": 1},
                "error": "TypeError"
            },
            {
                "input": {"nums": "not a list", "target": 5},
                "error": "TypeError"
            },
            {
                "input": {"nums": [1, 2, 3], "target": "not a number"},
                "error": "TypeError"
            },
            {
                "input": {"nums": [1, 2, 3], "target": 7},
                "error": "ValueError"
            }
        ]
        
        for scenario in error_scenarios:
            with pytest.raises(eval(scenario["error"])):
                solution.twoSum(**scenario["input"])


class TestRealWorldScenarios:
    """Integration tests for real-world scenarios."""
    
    def test_large_random_dataset(self):
        """Test with a large pseudo-random dataset."""
        import random
        
        # Generate a large dataset with known solution
        random.seed(42)  # For reproducible tests
        nums = [random.randint(-1000, 1000) for _ in range(1000)]
        
        # Insert a known solution
        nums[100] = 500
        nums[200] = 300
        target = 800
        
        solution = Solution("hashmap")
        result = solution.twoSum(nums, target)
        
        # Should find our inserted solution
        assert sorted(result) == [100, 200]
    
    def test_edge_case_combinations(self):
        """Test combinations of edge cases."""
        edge_cases = [
            {
                "name": "minimum_values",
                "nums": [-2147483648, 2147483647],
                "target": -1,
                "description": "32-bit integer limits"
            },
            {
                "name": "zero_sum",
                "nums": [0, 0, 0, 1, -1],
                "target": 0,
                "description": "Multiple zero sum pairs"
            },
            {
                "name": "repeated_values",
                "nums": [1, 1, 1, 1, 1, 1],
                "target": 2,
                "description": "All identical values"
            }
        ]
        
        for case in edge_cases:
            solution = Solution()
            result = solution.twoSum(case["nums"], case["target"])
            
            # Verify it's a valid solution
            i, j = result
            assert i != j
            assert case["nums"][i] + case["nums"][j] == case["target"]
    
    def test_concurrent_usage(self):
        """Test concurrent usage of the solution."""
        import threading
        
        results = []
        errors = []
        
        def worker(nums, target, algorithm):
            try:
                solution = Solution(algorithm)
                result = solution.twoSum(nums, target)
                results.append(result)
            except Exception as e:
                errors.append(str(e))
        
        # Create multiple threads
        threads = []
        test_data = [
            ([2, 7, 11, 15], 9, "hashmap"),
            ([3, 2, 4], 6, "bruteforce"),
            ([3, 3], 6, "twopointer")
        ]
        
        for nums, target, algorithm in test_data:
            thread = threading.Thread(target=worker, args=(nums, target, algorithm))
            threads.append(thread)
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        
        # Verify results
        assert len(errors) == 0
        assert len(results) == 3
        assert sorted(results[0]) == [0, 1]
        assert sorted(results[1]) == [1, 2]
        assert sorted(results[2]) == [0, 1]


class TestBackwardCompatibility:
    """Integration tests for backward compatibility."""
    
    def test_original_interface_compatibility(self):
        """Test that the new implementation maintains the original interface."""
        # Test that it works exactly like the original LeetCode solution
        solution = Solution()
        
        # Test cases that would be used in LeetCode
        test_cases = [
            {"nums": [2, 7, 11, 15], "target": 9},
            {"nums": [3, 2, 4], "target": 6},
            {"nums": [3, 3], "target": 6}
        ]
        
        expected_results = [[0, 1], [1, 2], [0, 1]]
        
        for i, test_case in enumerate(test_cases):
            result = solution.twoSum(test_case["nums"], test_case["target"])
            assert sorted(result) == sorted(expected_results[i])
    
    def test_import_compatibility(self):
        """Test that imports work as expected."""
        # Test various import patterns
        from leetcode19 import Solution
        from leetcode19.algorithms import HashMapSolver
        from leetcode19.utils import calculate_complement
        
        # All should work without errors
        solution = Solution()
        solver = HashMapSolver()
        complement = calculate_complement(10, 3)
        
        assert complement == 7
        assert sorted(solution.twoSum([2, 7, 11, 15], 9)) == [0, 1]
        assert sorted(solver.solve([2, 7, 11, 15], 9)) == [0, 1]