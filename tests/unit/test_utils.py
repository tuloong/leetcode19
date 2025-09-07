"""Unit tests for two-sum core utilities."""

import pytest
from unittest.mock import Mock, patch
from leetcode19.utils import (
    calculate_complement,
    build_number_index_map,
    validate_input,
    format_result,
    parse_input_string,
    InputValidator
)


class TestCalculateComplement:
    """Test cases for calculate_complement function."""
    
    def test_positive_numbers(self):
        """Test with positive numbers."""
        assert calculate_complement(10, 3) == 7
        assert calculate_complement(5, 2) == 3
        assert calculate_complement(100, 50) == 50
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        assert calculate_complement(-5, -3) == -2
        assert calculate_complement(0, -5) == 5
        assert calculate_complement(-10, 3) == -13
    
    def test_zero_cases(self):
        """Test with zero values."""
        assert calculate_complement(0, 0) == 0
        assert calculate_complement(5, 0) == 5
        assert calculate_complement(0, 5) == -5


class TestBuildNumberIndexMap:
    """Test cases for build_number_index_map function."""
    
    def test_unique_numbers(self):
        """Test with unique numbers."""
        nums = [2, 7, 11, 15]
        expected = {2: 0, 7: 1, 11: 2, 15: 3}
        assert build_number_index_map(nums) == expected
    
    def test_duplicate_numbers(self):
        """Test with duplicate numbers (should keep last index)."""
        nums = [1, 1, 1]
        expected = {1: 2}  # Last index for duplicate values
        assert build_number_index_map(nums) == expected
    
    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers."""
        nums = [-1, 2, -1, 3]
        expected = {-1: 2, 2: 1, 3: 3}
        assert build_number_index_map(nums) == expected
    
    def test_empty_list(self):
        """Test with empty list."""
        assert build_number_index_map([]) == {}


class TestValidateInput:
    """Test cases for validate_input function."""
    
    def test_valid_inputs(self):
        """Test with valid inputs."""
        assert validate_input([1, 2, 3], 5) is True
        assert validate_input([0, 0], 0) is True
        assert validate_input([-1, 1], 0) is True
        assert validate_input([1, 2], 3) is True
    
    def test_invalid_list_type(self):
        """Test with invalid list type."""
        assert validate_input("not a list", 5) is False
        assert validate_input(123, 5) is False
        assert validate_input(None, 5) is False
    
    def test_invalid_target_type(self):
        """Test with invalid target type."""
        assert validate_input([1, 2, 3], "not a number") is False
        assert validate_input([1, 2, 3], None) is False
        assert validate_input([1, 2, 3], [1, 2]) is False
    
    def test_invalid_list_length(self):
        """Test with invalid list length."""
        assert validate_input([], 5) is False
        assert validate_input([1], 5) is False
    
    def test_invalid_element_types(self):
        """Test with invalid element types."""
        assert validate_input([1, 2, "three"], 5) is False
        assert validate_input([1, 2, None], 5) is False
        assert validate_input([1, 2, []], 5) is False


class TestFormatResult:
    """Test cases for format_result function."""
    
    def test_valid_result(self):
        """Test with valid result."""
        nums = [2, 7, 11, 15]
        indices = [0, 1]
        expected = "nums[0] + nums[1] = 2 + 7 = 9"
        assert format_result(nums, indices) == expected
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        nums = [-1, -2, -3, -4]
        indices = [2, 3]
        expected = "nums[2] + nums[3] = -3 + -4 = -7"
        assert format_result(nums, indices) == expected
    
    def test_invalid_result_format(self):
        """Test with invalid result format."""
        nums = [1, 2, 3]
        assert format_result(nums, []) == "Invalid result format"
        assert format_result(nums, [0]) == "Invalid result format"
        assert format_result(nums, [0, 1, 2]) == "Invalid result format"


class TestParseInputString:
    """Test cases for parse_input_string function."""
    
    def test_valid_input(self):
        """Test with valid input."""
        assert parse_input_string("1,2,3,4") == [1, 2, 3, 4]
        assert parse_input_string("-1,-2,-3") == [-1, -2, -3]
        assert parse_input_string("0,1,0") == [0, 1, 0]
    
    def test_input_with_spaces(self):
        """Test with input containing spaces."""
        assert parse_input_string("1, 2, 3") == [1, 2, 3]
        assert parse_input_string(" 1 , 2 , 3 ") == [1, 2, 3]
    
    def test_invalid_input(self):
        """Test with invalid input."""
        with pytest.raises(ValueError):
            parse_input_string("1,2,three")
        
        with pytest.raises(ValueError):
            parse_input_string("1,2,3.5")
        
        with pytest.raises(ValueError):
            parse_input_string("1;2;3")


class TestInputValidator:
    """Test cases for InputValidator class."""
    
    def test_validate_list_length(self):
        """Test list length validation."""
        # Valid cases
        assert InputValidator.validate_list_length([1, 2]) is True
        assert InputValidator.validate_list_length([1, 2, 3]) is True
        
        # Invalid cases
        assert InputValidator.validate_list_length([1]) is False
        assert InputValidator.validate_list_length([]) is False
        
        # Custom bounds
        assert InputValidator.validate_list_length([1, 2, 3, 4, 5], min_length=5) is True
        assert InputValidator.validate_list_length([1, 2, 3, 4, 5], max_length=3) is False
    
    def test_validate_number_range(self):
        """Test number range validation."""
        # Valid cases
        assert InputValidator.validate_number_range([1, 2, 3]) is True
        assert InputValidator.validate_number_range([-5, 0, 5]) is True
        
        # Invalid cases
        assert InputValidator.validate_number_range([1000000001]) is False
        assert InputValidator.validate_number_range([-1000000001]) is False
        
        # Custom bounds
        assert InputValidator.validate_number_range([1, 2, 3], min_val=1, max_val=3) is True
        assert InputValidator.validate_number_range([1, 2, 3], min_val=2) is False
    
    def test_validate_target_range(self):
        """Test target range validation."""
        # Valid cases
        assert InputValidator.validate_target_range(5) is True
        assert InputValidator.validate_target_range(-5) is True
        assert InputValidator.validate_target_range(0) is True
        
        # Invalid cases
        assert InputValidator.validate_target_range(1000000001) is False
        assert InputValidator.validate_target_range(-1000000001) is False
        
        # Custom bounds
        assert InputValidator.validate_target_range(5, min_val=0, max_val=10) is True
        assert InputValidator.validate_target_range(5, min_val=10) is False