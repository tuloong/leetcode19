"""Example usage of the leetcode19 package."""

from leetcode19 import Solution
from leetcode19.algorithms import get_solver
from leetcode19.utils import format_result, parse_input_string


def basic_usage_example():
    """Demonstrate basic usage of the Solution class."""
    print("=== Basic Usage Example ===")
    
    # Create solution with default algorithm
    solution = Solution()
    
    # Solve basic problem
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    
    print(f"Problem: Find two numbers in {nums} that sum to {target}")
    print(f"Solution: indices {result}")
    print(f"Verification: {format_result(nums, result)}")
    print()


def algorithm_comparison_example():
    """Demonstrate different algorithm implementations."""
    print("=== Algorithm Comparison Example ===")
    
    nums = [2, 7, 11, 15]
    target = 9
    
    algorithms = ["hashmap", "bruteforce", "twopointer"]
    
    for algorithm in algorithms:
        solution = Solution(algorithm)
        result = solution.twoSum(nums, target)
        print(f"{algorithm:12}: {result}")
    
    print()


def direct_algorithm_usage_example():
    """Demonstrate direct usage of algorithm classes."""
    print("=== Direct Algorithm Usage Example ===")
    
    from leetcode19.algorithms import HashMapSolver, BruteForceSolver, TwoPointerSolver
    
    nums = [3, 2, 4]
    target = 6
    
    solvers = [
        HashMapSolver(),
        BruteForceSolver(),
        TwoPointerSolver()
    ]
    
    for solver in solvers:
        result = solver.solve(nums, target)
        print(f"{solver.__class__.__name__:15}: {result}")
    
    print()


def utility_functions_example():
    """Demonstrate utility functions."""
    print("=== Utility Functions Example ===")
    
    # Parse input string
    input_str = "2, 7, 11, 15"
    nums = parse_input_string(input_str)
    print(f"Parsed input '{input_str}': {nums}")
    
    # Format result
    nums = [2, 7, 11, 15]
    indices = [0, 1]
    formatted = format_result(nums, indices)
    print(f"Formatted result: {formatted}")
    
    print()


def error_handling_example():
    """Demonstrate error handling."""
    print("=== Error Handling Example ===")
    
    solution = Solution()
    
    # Test cases that should raise errors
    test_cases = [
        {"nums": [], "target": 5, "error": "TypeError"},
        {"nums": [1], "target": 1, "error": "TypeError"},
        {"nums": [1, 2, 3], "target": 7, "error": "ValueError"},
        {"nums": "not a list", "target": 5, "error": "TypeError"},
    ]
    
    for case in test_cases:
        try:
            result = solution.twoSum(case["nums"], case["target"])
            print(f"Unexpected success: {case} -> {result}")
        except Exception as e:
            print(f"Expected error: {case} -> {type(e).__name__}: {e}")
    
    print()


def performance_comparison_example():
    """Demonstrate performance comparison."""
    print("=== Performance Comparison Example ===")
    
    import time
    
    # Create a larger dataset
    nums = list(range(1000))
    target = 1997  # 998 + 999
    
    algorithms = ["hashmap", "bruteforce", "twopointer"]
    
    print(f"Testing with {len(nums)} numbers, target = {target}")
    print(f"{'Algorithm':<12} {'Time (s)':<12} {'Result':<15}")
    print("-" * 45)
    
    for algorithm in algorithms:
        try:
            solution = Solution(algorithm)
            
            start_time = time.time()
            result = solution.twoSum(nums, target)
            end_time = time.time()
            
            execution_time = end_time - start_time
            print(f"{algorithm:<12} {execution_time:<12.6f} {str(result):<15}")
            
        except Exception as e:
            print(f"{algorithm:<12} {'Error':<12} {str(e):<15}")
    
    print()


def edge_cases_example():
    """Demonstrate edge cases."""
    print("=== Edge Cases Example ===")
    
    solution = Solution()
    
    edge_cases = [
        {"nums": [0, 0], "target": 0, "description": "Zero values"},
        {"nums": [-1, -2, -3, -4], "target": -7, "description": "Negative numbers"},
        {"nums": [1, 1, 1, 1], "target": 2, "description": "Duplicate values"},
        {"nums": [2147483647, -2147483648], "target": -1, "description": "32-bit limits"},
    ]
    
    for case in edge_cases:
        try:
            result = solution.twoSum(case["nums"], case["target"])
            print(f"{case['description']:20}: {result}")
        except Exception as e:
            print(f"{case['description']:20}: Error - {e}")
    
    print()


def main():
    """Run all examples."""
    print("LeetCode 19 - Two Sum Problem Examples")
    print("=" * 50)
    print()
    
    basic_usage_example()
    algorithm_comparison_example()
    direct_algorithm_usage_example()
    utility_functions_example()
    error_handling_example()
    performance_comparison_example()
    edge_cases_example()
    
    print("All examples completed!")


if __name__ == "__main__":
    main()