"""Core utilities for the leetcode19 package."""

from typing import List, Dict, Optional, Tuple, Union, Any


def calculate_complement(target: int, num: int) -> int:
    """Calculate the complement number needed to reach the target.
    
    Args:
        target: The target sum
        num: The current number
        
    Returns:
        The complement number (target - num)
    """
    return target - num


def build_number_index_map(nums: List[int]) -> Dict[int, int]:
    """Build a mapping of numbers to their indices.
    
    Args:
        nums: List of numbers
        
    Returns:
        Dictionary mapping each number to its index
    """
    return {num: i for i, num in enumerate(nums)}


def validate_input(nums: List[int], target: int) -> bool:
    """Validate input parameters.
    
    Args:
        nums: List of numbers
        target: Target sum
        
    Returns:
        True if input is valid, False otherwise
    """
    if not isinstance(nums, list):
        return False
    if not isinstance(target, int):
        return False
    if len(nums) < 2:
        return False
    if not all(isinstance(x, int) for x in nums):
        return False
    return True


def format_result(nums: List[int], indices: List[int]) -> str:
    """Format the result for display.
    
    Args:
        nums: Original list of numbers
        indices: List of indices found
        
    Returns:
        Formatted string representation
    """
    if len(indices) != 2:
        return "Invalid result format"
    
    i, j = indices
    return f"nums[{i}] + nums[{j}] = {nums[i]} + {nums[j]} = {nums[i] + nums[j]}"


def parse_input_string(input_str: str) -> List[int]:
    """Parse a comma-separated string of integers.
    
    Args:
        input_str: String containing comma-separated integers
        
    Returns:
        List of integers
        
    Raises:
        ValueError: If input cannot be parsed
    """
    try:
        return [int(x.strip()) for x in input_str.split(',')]
    except ValueError as e:
        raise ValueError(f"Invalid input format: {e}")


class InputValidator:
    """Input validation utility class."""
    
    @staticmethod
    def validate_list_length(nums: List[int], min_length: int = 2, max_length: int = 10000) -> bool:
        """Validate list length constraints.
        
        Args:
            nums: List to validate
            min_length: Minimum allowed length
            max_length: Maximum allowed length
            
        Returns:
            True if valid, False otherwise
        """
        return min_length <= len(nums) <= max_length
    
    @staticmethod
    def validate_number_range(nums: List[int], min_val: int = -1000000000, max_val: int = 1000000000) -> bool:
        """Validate number range constraints.
        
        Args:
            nums: List to validate
            min_val: Minimum allowed value
            max_val: Maximum allowed value
            
        Returns:
            True if valid, False otherwise
        """
        return all(min_val <= x <= max_val for x in nums)
    
    @staticmethod
    def validate_target_range(target: int, min_val: int = -1000000000, max_val: int = 1000000000) -> bool:
        """Validate target range constraints.
        
        Args:
            target: Target to validate
            min_val: Minimum allowed value
            max_val: Maximum allowed value
            
        Returns:
            True if valid, False otherwise
        """
        return min_val <= target <= max_val