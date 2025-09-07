"""Core module for the leetcode19 package."""

from .algorithms import TwoSumSolver, HashMapSolver, get_solver
from .utils import calculate_complement, validate_input, format_result, parse_input_string

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

__all__ = [
    "TwoSumSolver",
    "HashMapSolver", 
    "get_solver",
    "calculate_complement",
    "validate_input",
    "format_result",
    "parse_input_string",
]


class Solution:
    """LeetCode Two Sum Problem Solution class."""
    
    def __init__(self, algorithm: str = "hashmap"):
        """Initialize solution with specified algorithm.
        
        Args:
            algorithm: Algorithm to use ('hashmap', 'bruteforce', 'twopointer')
        """
        self.solver = get_solver(algorithm)
    
    def twoSum(self, nums: list, target: int) -> list:
        """Find two numbers that sum to target.
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List of two indices that sum to target
            
        Raises:
            ValueError: If no solution found
            TypeError: If input validation fails
        """
        return self.solver.solve(nums, target)