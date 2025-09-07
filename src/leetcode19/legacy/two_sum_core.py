"""Core logic module for two-sum problem solving."""

from typing import List, Dict, Optional, Tuple


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


def find_pair_with_hash_map(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """Find a pair of indices that sum to target using hash map approach.
    
    Args:
        nums: List of numbers
        target: Target sum
        
    Returns:
        Tuple of two indices if found, None otherwise
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = calculate_complement(target, num)
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None


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
    return True


def two_sum_core(nums: List[int], target: int) -> List[int]:
    """Core function to solve two-sum problem.
    
    Args:
        nums: List of numbers
        target: Target sum
        
    Returns:
        List of two indices that sum to target
        
    Raises:
        ValueError: If no solution found
        TypeError: If input validation fails
    """
    if not validate_input(nums, target):
        raise TypeError("Invalid input parameters")
    
    result = find_pair_with_hash_map(nums, target)
    if result is None:
        raise ValueError("No two sum solution")
    
    return list(result)