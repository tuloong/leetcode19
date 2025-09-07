"""Test fixtures and test data for two-sum problem tests."""

import pytest
from typing import List, Tuple


class TwoSumTestData:
    """Test data container for two-sum problem."""
    
    # Basic test cases
    BASIC_CASES = [
        {
            "name": "simple_case",
            "nums": [2, 7, 11, 15],
            "target": 9,
            "expected": [0, 1],
            "description": "Basic case with positive numbers"
        },
        {
            "name": "middle_indices",
            "nums": [3, 2, 4],
            "target": 6,
            "expected": [1, 2],
            "description": "Solution in middle of array"
        },
        {
            "name": "duplicate_numbers",
            "nums": [3, 3],
            "target": 6,
            "expected": [0, 1],
            "description": "Duplicate numbers"
        },
        {
            "name": "negative_numbers",
            "nums": [-1, -2, -3, -4],
            "target": -7,
            "expected": [2, 3],
            "description": "Negative numbers"
        },
        {
            "name": "mixed_numbers",
            "nums": [-1, 2, -3, 4],
            "target": 1,
            "expected": [0, 1],
            "description": "Mixed positive and negative numbers"
        },
        {
            "name": "zero_target",
            "nums": [0, 4, 3, 0],
            "target": 0,
            "expected": [0, 3],
            "description": "Zero target with zero values"
        }
    ]
    
    # Edge cases
    EDGE_CASES = [
        {
            "name": "minimum_length",
            "nums": [1, 2],
            "target": 3,
            "expected": [0, 1],
            "description": "Minimum valid array length"
        },
        {
            "name": "large_numbers",
            "nums": [1000000000, 1000000000],
            "target": 2000000000,
            "expected": [0, 1],
            "description": "Large numbers at limit"
        },
        {
            "name": "same_index_different_values",
            "nums": [1, 2, 1],
            "target": 2,
            "expected": [0, 2],
            "description": "Same value at different indices"
        }
    ]
    
    # Invalid input cases
    INVALID_CASES = [
        {
            "name": "empty_list",
            "nums": [],
            "target": 5,
            "expected_error": "TypeError",
            "description": "Empty list"
        },
        {
            "name": "single_element",
            "nums": [1],
            "target": 1,
            "expected_error": "TypeError",
            "description": "Single element list"
        },
        {
            "name": "non_list_input",
            "nums": "not a list",
            "target": 5,
            "expected_error": "TypeError",
            "description": "Non-list input"
        },
        {
            "name": "non_integer_elements",
            "nums": [1, 2, "three"],
            "target": 5,
            "expected_error": "TypeError",
            "description": "Non-integer elements"
        },
        {
            "name": "non_integer_target",
            "nums": [1, 2, 3],
            "target": "not a number",
            "expected_error": "TypeError",
            "description": "Non-integer target"
        }
    ]
    
    # No solution cases
    NO_SOLUTION_CASES = [
        {
            "name": "no_solution_positive",
            "nums": [1, 2, 3],
            "target": 7,
            "expected_error": "ValueError",
            "description": "No solution with positive numbers"
        },
        {
            "name": "no_solution_negative",
            "nums": [-1, -2, -3],
            "target": -7,
            "expected_error": "ValueError",
            "description": "No solution with negative numbers"
        },
        {
            "name": "no_solution_mixed",
            "nums": [1, -2, 3],
            "target": 10,
            "expected_error": "ValueError",
            "description": "No solution with mixed numbers"
        }
    ]
    
    # Performance test cases
    PERFORMANCE_CASES = [
        {
            "name": "large_array_1000",
            "nums": list(range(1000)),
            "target": 1997,
            "expected": [998, 999],
            "description": "Large array of 1000 elements"
        },
        {
            "name": "large_array_10000",
            "nums": list(range(10000)),
            "target": 19997,
            "expected": [9998, 9999],
            "description": "Large array of 10000 elements"
        }
    ]


@pytest.fixture
def basic_test_cases():
    """Fixture providing basic test cases."""
    return TwoSumTestData.BASIC_CASES


@pytest.fixture
def edge_test_cases():
    """Fixture providing edge test cases."""
    return TwoSumTestData.EDGE_CASES


@pytest.fixture
def invalid_test_cases():
    """Fixture providing invalid input test cases."""
    return TwoSumTestData.INVALID_CASES


@pytest.fixture
def no_solution_test_cases():
    """Fixture providing no solution test cases."""
    return TwoSumTestData.NO_SOLUTION_CASES


@pytest.fixture
def performance_test_cases():
    """Fixture providing performance test cases."""
    return TwoSumTestData.PERFORMANCE_CASES


@pytest.fixture
def sample_data():
    """Fixture providing sample data for testing."""
    return {
        "simple": {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},
        "negative": {"nums": [-1, -2, -3, -4], "target": -7, "expected": [2, 3]},
        "zero": {"nums": [0, 4, 3, 0], "target": 0, "expected": [0, 3]},
    }