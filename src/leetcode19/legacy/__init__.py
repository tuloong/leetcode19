"""Legacy implementations for backward compatibility."""

from .two_sum_core import (
    calculate_complement,
    build_number_index_map,
    find_pair_with_hash_map,
    validate_input,
    two_sum_core
)
from .twoSum import Solution

__all__ = [
    "calculate_complement",
    "build_number_index_map", 
    "find_pair_with_hash_map",
    "validate_input",
    "two_sum_core",
    "Solution",
]