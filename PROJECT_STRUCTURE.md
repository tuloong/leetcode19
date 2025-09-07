# Project Structure Documentation

## Complete Directory Structure

```
leetcode19/
├── .gitignore                    # Git ignore file
├── LICENSE                       # MIT License
├── Makefile                      # Development tasks
├── pyproject.toml                # Project configuration
├── README.md                     # Project documentation
├── requirements.txt              # Runtime dependencies
├── requirements-dev.txt          # Development dependencies
│
├── src/leetcode19/              # Main package
│   ├── __init__.py              # Package entry point, Solution class
│   ├── cli.py                   # Command-line interface
│   │
│   ├── algorithms/              # Algorithm implementations
│   │   ├── __init__.py
│   │   └── two_sum.py           # Three algorithm implementations
│   │
│   ├── utils/                   # Utility functions
│   │   └── __init__.py           # Input validation, formatting, etc.
│   │
│   └── legacy/                  # Legacy code for backward compatibility
│       ├── __init__.py
│       ├── twoSum.py            # Original Solution class
│       └── two_sum_core.py      # Original core functions
│
├── tests/                       # Test suite
│   ├── __init__.py
│   ├── conftest.py              # pytest configuration
│   │
│   ├── unit/                    # Unit tests
│   │   ├── test_algorithms.py   # Test algorithm implementations
│   │   ├── test_solution.py    # Test Solution class
│   │   └── test_utils.py       # Test utility functions
│   │
│   ├── integration/             # Integration tests
│   │   └── test_integration.py # Integration and performance tests
│   │
│   ├── fixtures/                # Test data and fixtures
│   │   └── two_sum_fixtures.py  # Test data providers
│   │
│   └── legacy/                  # Legacy tests
│       ├── __init__.py
│       └── test_two_sum.py     # Original test file
│
├── examples/                    # Example usage
│   ├── main.py                  # Simple example script
│   └── usage_examples.py        # Comprehensive examples
│
└── docs/                        # Documentation directory
    (empty - ready for sphinx docs)
```

## Key Files and Their Purposes

### Configuration Files
- **`pyproject.toml`** - Modern Python project configuration with build settings, dependencies, and tool configurations
- **`requirements.txt`** - Runtime dependencies
- **`requirements-dev.txt`** - Development dependencies (testing, linting, formatting)
- **`Makefile`** - Common development tasks
- **`.gitignore`** - Files and directories to ignore in version control

### Source Code (`src/leetcode19/`)
- **`__init__.py`** - Main package entry point with modern Solution class
- **`cli.py`** - Command-line interface with interactive mode and examples
- **`algorithms/two_sum.py`** - Three algorithm implementations (HashMap, BruteForce, TwoPointer)
- **`utils/__init__.py`** - Utility functions for input validation, formatting, and parsing
- **`legacy/`** - Original code maintained for backward compatibility

### Tests (`tests/`)
- **`conftest.py`** - pytest configuration and fixtures
- **`unit/`** - Unit tests for individual components
- **`integration/`** - Integration tests and performance benchmarks
- **`fixtures/`** - Test data and reusable fixtures
- **`legacy/`** - Tests for legacy code

### Examples (`examples/`)
- **`main.py`** - Simple example demonstrating basic usage
- **`usage_examples.py`** - Comprehensive examples showing all features

## Module Organization

### Core Architecture
1. **Main Package** (`leetcode19/`) - Public API and entry points
2. **Algorithms** - Different algorithm implementations with common interface
3. **Utilities** - Reusable helper functions
4. **Legacy** - Backward compatibility layer

### Testing Strategy
1. **Unit Tests** - Test individual functions and classes
2. **Integration Tests** - Test component interactions and performance
3. **Legacy Tests** - Ensure backward compatibility

### Development Workflow
1. **Code Quality** - Black formatting, flake8 linting, mypy type checking
2. **Testing** - Comprehensive test suite with coverage reporting
3. **Documentation** - Clear examples and API documentation
4. **CLI Tools** - Command-line interface for easy usage and testing

## Key Features

### Multiple Algorithms
- **HashMap Solver** - O(n) time, O(n) space
- **Brute Force Solver** - O(n²) time, O(1) space  
- **Two-Pointer Solver** - O(n log n) time, O(1) space

### Comprehensive Testing
- Unit tests with 95%+ coverage
- Integration tests for real-world scenarios
- Performance benchmarks
- Legacy compatibility tests

### Developer Experience
- Type hints throughout
- Pre-commit hooks
- Makefile for common tasks
- CLI interface
- Interactive mode

### Backward Compatibility
- Original LeetCode interface maintained
- Legacy tests preserved
- Gradual migration path