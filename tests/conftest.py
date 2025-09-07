"""Configuration and initialization for pytest."""

import pytest
import sys
import os
from pathlib import Path

# Add the src directory to Python path
project_root = Path(__file__).parent.parent
src_path = project_root / "src"
sys.path.insert(0, str(src_path))

# Configure pytest
pytest_plugins = []


@pytest.fixture(scope="session")
def project_root():
    """Fixture providing the project root directory."""
    return project_root


@pytest.fixture(scope="session")
def src_path():
    """Fixture providing the source directory path."""
    return src_path


@pytest.fixture
def sample_test_data():
    """Fixture providing sample test data."""
    return {
        "basic": {
            "nums": [2, 7, 11, 15],
            "target": 9,
            "expected": [0, 1]
        },
        "negative": {
            "nums": [-1, -2, -3, -4],
            "target": -7,
            "expected": [2, 3]
        },
        "zero": {
            "nums": [0, 4, 3, 0],
            "target": 0,
            "expected": [0, 3]
        }
    }


# Custom markers
def pytest_configure(config):
    """Configure custom pytest markers."""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "unit: marks tests as unit tests"
    )
    config.addinivalue_line(
        "markers", "performance: marks tests as performance tests"
    )


@pytest.fixture
def mock_solver():
    """Fixture providing a mock solver for testing."""
    from unittest.mock import Mock
    from leetcode19.algorithms import TwoSumSolver
    
    class MockSolver(TwoSumSolver):
        def __init__(self):
            self.call_count = 0
            self.last_args = None
            self.mock_result = [0, 1]
        
        def solve(self, nums, target):
            self.call_count += 1
            self.last_args = (nums, target)
            return self.mock_result
    
    return MockSolver()


@pytest.fixture
def performance_benchmark():
    """Fixture for performance benchmarking."""
    import time
    
    def benchmark(func, *args, **kwargs):
        """Benchmark a function call."""
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        return {
            "result": result,
            "execution_time": end_time - start_time,
            "function": func.__name__
        }
    
    return benchmark


@pytest.fixture
def temp_test_file(tmp_path):
    """Fixture for creating temporary test files."""
    def create_test_file(content, filename="test_input.txt"):
        file_path = tmp_path / filename
        file_path.write_text(content)
        return str(file_path)
    
    return create_test_file


@pytest.fixture
def console_output_capture(capsys):
    """Fixture for capturing console output."""
    def capture_output(func, *args, **kwargs):
        func(*args, **kwargs)
        captured = capsys.readouterr()
        return captured.out, captured.err
    
    return capture_output