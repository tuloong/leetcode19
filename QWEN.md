# LeetCode 19 - Two Sum Problem

## Project Overview

The leetcode19 project is a modular, well-tested solution to the classic Two Sum LeetCode problem, implemented in Python. It features multiple algorithm implementations (HashMap, Brute Force, and Two-Pointer approaches) with comprehensive testing, type safety, and a command-line interface. The project emphasizes code quality with Black formatting, flake8 linting, and mypy type checking, along with backward compatibility for the original LeetCode interface.

## Key Features

- **Multiple Algorithms**: HashMap (O(n) time), Brute Force (O(n²) time), and Two-Pointer (O(n log n) time) approaches
- **Comprehensive Testing**: Unit tests, integration tests, and performance tests with pytest
- **Type Safety**: Full type hints and mypy support
- **Code Quality**: Black formatting, flake8 linting, and pre-commit hooks
- **Performance Optimized**: Efficient algorithms with benchmarking capabilities
- **CLI Interface**: Command-line interface for easy usage
- **Backward Compatible**: Maintains the original LeetCode interface

## Architecture

### Core Components
- **`Solution` Class**: Main class that uses a factory pattern to select between different algorithm implementations
- **Algorithm Implementations**: Three solver classes (`HashMapSolver`, `BruteForceSolver`, `TwoPointerSolver`) all inheriting from `TwoSumSolver`
- **Utility Functions**: Helper functions for input validation, parsing, formatting, and validation
- **CLI Module**: Command-line interface with interactive mode, examples, and benchmarking

### Project Structure
```
leetcode19/
├── src/
│   └── leetcode19/
│       ├── __init__.py
│       ├── algorithms/
│       │   ├── __init__.py
│       │   └── two_sum.py
│       ├── utils/
│       │   └── __init__.py
│       └── cli.py
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── fixtures/
│   └── legacy/
├── examples/
├── docs/
├── pyproject.toml
├── README.md
└── Makefile
```

## Building and Running

### Installation
```bash
# From source
pip install -e .

# For development
pip install -e ".[dev]"
pre-commit install
```

### Basic Usage
```python
from leetcode19 import Solution

# Create solution with default algorithm (hashmap)
solution = Solution()
result = solution.twoSum([2, 7, 11, 15], 9)
print(result)  # [0, 1]
```

### Using Different Algorithms
```python
# HashMap (default, O(n) time, O(n) space)
solution = Solution("hashmap")

# Brute Force (O(n²) time, O(1) space)
solution = Solution("bruteforce")

# Two-Pointer (O(n log n) time, O(1) space, requires sorting)
solution = Solution("twopointer")
```

### Command Line Interface
```bash
# Interactive mode
leetcode19 --interactive

# Run examples
leetcode19 --examples

# Single problem
leetcode19 --nums "2,7,11,15" --target 9

# Benchmark different algorithms
leetcode19 --nums "2,7,11,15" --target 9 --benchmark
```

### Testing
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/leetcode19 --cov-report=html

# Run specific test files
pytest tests/unit/test_solution.py

# Run unit tests
make test-unit

# Run integration tests
make test-integration

# Run tests with coverage
make test-coverage
```

### Development Commands
```bash
# Install package
make install

# Install development dependencies
make install-dev

# Format code
make format

# Lint code
make lint

# Type checking
make type-check

# Run all checks (lint, type-check, test)
make check

# Run pre-commit hooks
pre-commit run --all-files

# Clean build artifacts
make clean

# Run examples
make run-examples

# Interactive mode
make interactive

# Run demo
make demo

# Run benchmark
make benchmark
```

## Algorithm Comparison

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|--------|
| HashMap | O(n) | O(n) | Fastest, uses extra space |
| Brute Force | O(n²) | O(1) | Simple, slow for large inputs |
| Two-Pointer | O(n log n) | O(1) | Requires sorting, good for sorted arrays |

## Development Conventions

- **Code Formatting**: Black with 88 character line length
- **Linting**: flake8 with standard Python conventions
- **Type Checking**: mypy with strict settings
- **Testing**: pytest with 95%+ coverage requirement
- **Git Hooks**: Pre-commit hooks for formatting and linting
- **Documentation**: Type hints and docstrings for all public APIs

## API Reference

### Solution Class
```python
class Solution:
    def __init__(self, algorithm: str = "hashmap")
    def twoSum(self, nums: List[int], target: int) -> List[int]
```

### Algorithm Classes
```python
class HashMapSolver(TwoSumSolver)
class BruteForceSolver(TwoSumSolver)
class TwoPointerSolver(TwoSumSolver)
```

### Utility Functions
```python
calculate_complement(target: int, num: int) -> int
validate_input(nums: List[int], target: int) -> bool
format_result(nums: List[int], indices: List[int]) -> str
parse_input_string(input_str: str) -> List[int]
```