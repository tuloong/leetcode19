# LeetCode 19 - Two Sum Problem

A modular, well-tested solution to the classic two-sum problem with multiple algorithm implementations and comprehensive testing.

## Features

- **Multiple Algorithms**: HashMap, Brute Force, and Two-Pointer approaches
- **Comprehensive Testing**: Unit tests, integration tests, and performance tests
- **Type Safety**: Full type hints and mypy support
- **Code Quality**: Black formatting, flake8 linting, and pre-commit hooks
- **Performance Optimized**: Efficient algorithms with benchmarking
- **CLI Interface**: Command-line interface for easy usage
- **Backward Compatible**: Maintains the original LeetCode interface

## Installation

### From Source

```bash
git clone https://github.com/yourusername/leetcode19.git
cd leetcode19
pip install -e .
```

### Development Installation

```bash
git clone https://github.com/yourusername/leetcode19.git
cd leetcode19
pip install -e ".[dev]"
pre-commit install
```

## Quick Start

### Basic Usage

```python
from leetcode19 import Solution

# Create solution with default algorithm (hashmap)
solution = Solution()
result = solution.twoSum([2, 7, 11, 15], 9)
print(result)  # [0, 1]
```

### Different Algorithms

```python
from leetcode19 import Solution

# HashMap (default, O(n) time, O(n) space)
solution = Solution("hashmap")

# Brute Force (O(n²) time, O(1) space)
solution = Solution("bruteforce")

# Two-Pointer (O(n log n) time, O(1) space, requires sorting)
solution = Solution("twopointer")
```

### Direct Algorithm Usage

```python
from leetcode19.algorithms import get_solver

solver = get_solver("hashmap")
result = solver.solve([2, 7, 11, 15], 9)
print(result)  # [0, 1]
```

## Command Line Interface

### Interactive Mode

```bash
leetcode19 --interactive
```

### Run Examples

```bash
leetcode19 --examples
```

### Single Problem

```bash
leetcode19 --nums "2,7,11,15" --target 9
```

## Testing

### Run All Tests

```bash
pytest
```

### Run Unit Tests Only

```bash
pytest tests/unit/
```

### Run Integration Tests Only

```bash
pytest tests/integration/
```

### Run with Coverage

```bash
pytest --cov=src/leetcode19 --cov-report=html
```

### Run Performance Tests

```bash
pytest -m performance
```

## Development

### Code Quality

```bash
# Format code
black src/ tests/

# Lint code
flake8 src/ tests/

# Type checking
mypy src/
```

### Pre-commit Hooks

```bash
# Run all pre-commit hooks
pre-commit run --all-files

# Run specific hook
pre-commit run black
```

## Project Structure

```
leetcode19/
├── src/
│   └── leetcode19/
│       ├── __init__.py
│       ├── algorithms/
│       │   ├── __init__.py
│       │   └── two_sum.py
│       └── utils/
│           └── __init__.py
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── fixtures/
│   └── conftest.py
├── docs/
├── examples/
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## Algorithm Comparison

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|---------|
| HashMap | O(n) | O(n) | Fastest, uses extra space |
| Brute Force | O(n²) | O(1) | Simple, slow for large inputs |
| Two-Pointer | O(n log n) | O(1) | Requires sorting, good for sorted arrays |

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

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

### [0.1.0] - 2024-01-01

- Initial release
- Multiple algorithm implementations
- Comprehensive test suite
- CLI interface
- Full type safety
- Documentation and examples