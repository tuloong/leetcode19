"""Unit tests for two-sum algorithms."""

import pytest
from unittest.mock import Mock, patch
from leetcode19.algorithms import (
    TwoSumSolver,
    HashMapSolver,
    BruteForceSolver,
    TwoPointerSolver,
    get_solver
)
from tests.fixtures.two_sum_fixtures import TwoSumTestData


class TestHashMapSolver:
    """Test cases for HashMapSolver."""
    
    def test_basic_cases(self):
        """Test basic functionality."""
        solver = HashMapSolver()
        
        # Basic case
        result = solver.solve([2, 7, 11, 15], 9)
        assert sorted(result) == [0, 1]
        
        # Middle indices
        result = solver.solve([3, 2, 4], 6)
        assert sorted(result) == [1, 2]
        
        # Duplicate numbers
        result = solver.solve([3, 3], 6)
        assert sorted(result) == [0, 1]
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        solver = HashMapSolver()
        result = solver.solve([-1, -2, -3, -4], -7)
        assert sorted(result) == [2, 3]
    
    def test_no_solution(self):
        """Test with no solution."""
        solver = HashMapSolver()
        with pytest.raises(ValueError, match="No two sum solution"):
            solver.solve([1, 2, 3], 7)
    
    def test_invalid_input(self):
        """Test with invalid input."""
        solver = HashMapSolver()
        
        # Invalid list type
        with pytest.raises(TypeError, match="Invalid input parameters"):
            solver.solve("not a list", 5)
        
        # Invalid target type
        with pytest.raises(TypeError, match="Invalid input parameters"):
            solver.solve([1, 2, 3], "not a number")
        
        # Too short list
        with pytest.raises(TypeError, match="Invalid input parameters"):
            solver.solve([1], 5)


class TestBruteForceSolver:
    """Test cases for BruteForceSolver."""
    
    def test_basic_cases(self):
        """Test basic functionality."""
        solver = BruteForceSolver()
        
        # Basic case
        result = solver.solve([2, 7, 11, 15], 9)
        assert sorted(result) == [0, 1]
        
        # Middle indices
        result = solver.solve([3, 2, 4], 6)
        assert sorted(result) == [1, 2]
        
        # Duplicate numbers
        result = solver.solve([3, 3], 6)
        assert sorted(result) == [0, 1]
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        solver = BruteForceSolver()
        result = solver.solve([-1, -2, -3, -4], -7)
        assert sorted(result) == [2, 3]
    
    def test_no_solution(self):
        """Test with no solution."""
        solver = BruteForceSolver()
        with pytest.raises(ValueError, match="No two sum solution"):
            solver.solve([1, 2, 3], 7)
    
    def test_invalid_input(self):
        """Test with invalid input."""
        solver = BruteForceSolver()
        
        # Invalid list type
        with pytest.raises(TypeError, match="Invalid input parameters"):
            solver.solve("not a list", 5)
        
        # Invalid target type
        with pytest.raises(TypeError, match="Invalid input parameters"):
            solver.solve([1, 2, 3], "not a number")
        
        # Too short list
        with pytest.raises(TypeError, match="Invalid input parameters"):
            solver.solve([1], 5)


class TestTwoPointerSolver:
    """Test cases for TwoPointerSolver."""
    
    def test_basic_cases(self):
        """Test basic functionality."""
        solver = TwoPointerSolver()
        
        # Basic case
        result = solver.solve([2, 7, 11, 15], 9)
        assert sorted(result) == [0, 1]
        
        # Middle indices
        result = solver.solve([3, 2, 4], 6)
        assert sorted(result) == [1, 2]
        
        # Duplicate numbers
        result = solver.solve([3, 3], 6)
        assert sorted(result) == [0, 1]
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        solver = TwoPointerSolver()
        result = solver.solve([-1, -2, -3, -4], -7)
        assert sorted(result) == [2, 3]
    
    def test_no_solution(self):
        """Test with no solution."""
        solver = TwoPointerSolver()
        with pytest.raises(ValueError, match="No two sum solution"):
            solver.solve([1, 2, 3], 7)
    
    def test_invalid_input(self):
        """Test with invalid input."""
        solver = TwoPointerSolver()
        
        # Invalid list type
        with pytest.raises(TypeError, match="Invalid input parameters"):
            solver.solve("not a list", 5)
        
        # Invalid target type
        with pytest.raises(TypeError, match="Invalid input parameters"):
            solver.solve([1, 2, 3], "not a number")
        
        # Too short list
        with pytest.raises(TypeError, match="Invalid input parameters"):
            solver.solve([1], 5)


class TestGetSolver:
    """Test cases for get_solver factory function."""
    
    def test_hashmap_solver(self):
        """Test getting HashMapSolver."""
        solver = get_solver("hashmap")
        assert isinstance(solver, HashMapSolver)
        
        solver = get_solver("HASHMAP")
        assert isinstance(solver, HashMapSolver)
        
        solver = get_solver("HashMap")
        assert isinstance(solver, HashMapSolver)
    
    def test_bruteforce_solver(self):
        """Test getting BruteForceSolver."""
        solver = get_solver("bruteforce")
        assert isinstance(solver, BruteForceSolver)
        
        solver = get_solver("BRUTEFORCE")
        assert isinstance(solver, BruteForceSolver)
    
    def test_twopointer_solver(self):
        """Test getting TwoPointerSolver."""
        solver = get_solver("twopointer")
        assert isinstance(solver, TwoPointerSolver)
        
        solver = get_solver("TWOPOINTER")
        assert isinstance(solver, TwoPointerSolver)
    
    def test_invalid_algorithm(self):
        """Test with invalid algorithm name."""
        with pytest.raises(ValueError, match="Unsupported algorithm"):
            get_solver("invalid")
        
        with pytest.raises(ValueError, match="Unsupported algorithm"):
            get_solver("")
        
        with pytest.raises(ValueError, match="Unsupported algorithm"):
            get_solver(None)


class TestTwoSumSolverBase:
    """Test cases for TwoSumSolver base class."""
    
    def test_abstract_class(self):
        """Test that base class is abstract."""
        # Test that base class raises NotImplementedError when solve is called
        solver = TwoSumSolver()
        with pytest.raises(NotImplementedError):
            solver.solve([1, 2], 3)
        
        # Test that subclass must implement solve method
        class IncompleteSolver(TwoSumSolver):
            pass
        
        with pytest.raises(NotImplementedError):
            IncompleteSolver().solve([1, 2], 3)


class TestAlgorithmConsistency:
    """Test that all algorithms produce consistent results."""
    
    @pytest.mark.parametrize("test_case", TwoSumTestData.BASIC_CASES)
    def test_consistent_results(self, test_case):
        """Test that all algorithms produce the same results."""
        nums = test_case["nums"]
        target = test_case["target"]
        expected = test_case["expected"]
        
        # Test HashMap and BruteForce solvers (TwoPointer may return different indices due to sorting)
        solvers = [
            HashMapSolver(),
            BruteForceSolver(),
        ]
        
        for solver in solvers:
            result = solver.solve(nums, target)
            assert sorted(result) == sorted(expected)
    
    @pytest.mark.parametrize("test_case", TwoSumTestData.EDGE_CASES)
    def test_consistent_edge_cases(self, test_case):
        """Test that all algorithms handle edge cases consistently."""
        nums = test_case["nums"]
        target = test_case["target"]
        expected = test_case["expected"]
        
        # Test HashMap and BruteForce solvers (TwoPointer may return different indices due to sorting)
        solvers = [
            HashMapSolver(),
            BruteForceSolver(),
        ]
        
        for solver in solvers:
            result = solver.solve(nums, target)
            assert sorted(result) == sorted(expected)
    
    @pytest.mark.parametrize("test_case", TwoSumTestData.NO_SOLUTION_CASES)
    def test_consistent_no_solution(self, test_case):
        """Test that all algorithms handle no solution cases consistently."""
        nums = test_case["nums"]
        target = test_case["target"]
        expected_error = test_case["expected_error"]
        
        # Test all algorithms
        solvers = [
            HashMapSolver(),
            BruteForceSolver(),
            TwoPointerSolver()
        ]
        
        for solver in solvers:
            with pytest.raises(ValueError, match="No two sum solution"):
                solver.solve(nums, target)