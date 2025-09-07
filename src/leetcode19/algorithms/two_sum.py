"""Two-sum algorithm implementations."""

from typing import List, Dict, Optional, Tuple
from ..utils import calculate_complement, validate_input


class TwoSumSolver:
    """Base class for two-sum problem solvers."""
    
    def solve(self, nums: List[int], target: int) -> List[int]:
        """Solve the two-sum problem.
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List of two indices that sum to target
            
        Raises:
            ValueError: If no solution found
            TypeError: If input validation fails
        """
        raise NotImplementedError("Subclasses must implement solve method")


class HashMapSolver(TwoSumSolver):
    """Two-sum solver using hash map approach."""
    
    def solve(self, nums: List[int], target: int) -> List[int]:
        """Solve using hash map for O(n) time complexity.
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List of two indices that sum to target
            
        Raises:
            ValueError: If no solution found
            TypeError: If input validation fails
        """
        if not validate_input(nums, target):
            raise TypeError("Invalid input parameters")
        
        seen = {}
        for i, num in enumerate(nums):
            complement = calculate_complement(target, num)
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        
        raise ValueError("No two sum solution")


class BruteForceSolver(TwoSumSolver):
    """Two-sum solver using brute force approach."""
    
    def solve(self, nums: List[int], target: int) -> List[int]:
        """Solve using brute force for O(n²) time complexity.
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List of two indices that sum to target
            
        Raises:
            ValueError: If no solution found
            TypeError: If input validation fails
        """
        if not validate_input(nums, target):
            raise TypeError("Invalid input parameters")
        
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        raise ValueError("No two sum solution")


class TwoPointerSolver(TwoSumSolver):
    """Two-sum solver using two-pointer approach (requires sorted array)."""
    
    def solve(self, nums: List[int], target: int) -> List[int]:
        """Solve using two-pointer approach for sorted arrays.
        
        Args:
            nums: List of integers (will be sorted)
            target: Target sum
            
        Returns:
            List of two indices that sum to target
            
        Raises:
            ValueError: If no solution found
            TypeError: If input validation fails
        """
        if not validate_input(nums, target):
            raise TypeError("Invalid input parameters")
        
        # Create list of (value, index) pairs and sort by value
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        indexed_nums.sort()
        
        left, right = 0, len(indexed_nums) - 1
        
        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            
            if current_sum == target:
                return [indexed_nums[left][1], indexed_nums[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        raise ValueError("No two sum solution")


def get_solver(algorithm: str = "hashmap") -> TwoSumSolver:
    """Factory function to get the appropriate solver.
    
    Args:
        algorithm: Algorithm type ('hashmap', 'bruteforce', 'twopointer')
        
    Returns:
        Instance of the requested solver
        
    Raises:
        ValueError: If algorithm is not supported
    """
    solvers = {
        "hashmap": HashMapSolver,
        "bruteforce": BruteForceSolver,
        "twopointer": TwoPointerSolver,
    }
    
    if algorithm is None or algorithm.lower() not in solvers:
        raise ValueError(f"Unsupported algorithm: {algorithm}")
    
    return solvers[algorithm.lower()]()