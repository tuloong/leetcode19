#!/usr/bin/env python3
"""
Python script to replace Makefile commands for Windows users.
"""

import subprocess
import sys
import os
from pathlib import Path


def run_command(cmd, description=""):
    """Run a command and handle errors."""
    print(f"\n{'='*50}")
    print(f"Running: {description}")
    print(f"Command: {' '.join(cmd)}")
    print(f"{'='*50}")
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.stdout:
        print(result.stdout)
    
    if result.stderr:
        print(f"STDERR: {result.stderr}")
    
    if result.returncode != 0:
        print(f"Error: Command failed with return code {result.returncode}")
        return False
    
    return True


def test():
    """Run all tests."""
    return run_command(["pytest", "-v", "--tb=short"], "Running all tests")


def test_unit():
    """Run unit tests only."""
    return run_command(["pytest", "tests/unit/", "-v", "--tb=short"], "Running unit tests")


def test_integration():
    """Run integration tests only."""
    return run_command(["pytest", "tests/integration/", "-v", "--tb=short"], "Running integration tests")


def test_coverage():
    """Run tests with coverage."""
    return run_command(
        ["pytest", "--cov=src/leetcode19", "--cov-report=html", "--cov-report=term-missing"],
        "Running tests with coverage report"
    )


def lint():
    """Run linting."""
    return run_command(["flake8", "src/", "tests/"], "Running linting")


def format_code():
    """Format code."""
    return run_command(["black", "src/", "tests/"], "Formatting code")


def type_check():
    """Run type checking."""
    return run_command(["mypy", "src/"], "Running type checking")


def clean():
    """Clean build artifacts."""
    print("Cleaning build artifacts...")
    
    dirs_to_clean = [
        "build/",
        "dist/",
        "*.egg-info/",
        ".pytest_cache/",
        ".mypy_cache/",
        "htmlcov/",
        "__pycache__/",
    ]
    
    for pattern in dirs_to_clean:
        if pattern.endswith('/'):
            # Remove directory
            for path in Path(".").rglob(pattern.rstrip('/')):
                if path.is_dir():
                    print(f"Removing directory: {path}")
                    import shutil
                    shutil.rmtree(path, ignore_errors=True)
        else:
            # Remove files matching pattern
            for path in Path(".").glob(pattern):
                if path.is_file():
                    print(f"Removing file: {path}")
                    path.unlink()
                elif path.is_dir():
                    print(f"Removing directory: {path}")
                    import shutil
                    shutil.rmtree(path, ignore_errors=True)
    
    return True


def run_examples():
    """Run example scripts."""
    return run_command(["python", "examples/usage_examples.py"], "Running examples")


def check():
    """Run all checks (lint, type-check, test)."""
    success = True
    success &= lint()
    success &= type_check()
    success &= test()
    
    if success:
        print("\n" + "="*50)
        print("✅ All checks passed!")
        print("="*50)
    else:
        print("\n" + "="*50)
        print("❌ Some checks failed!")
        print("="*50)
    
    return success


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python build.py <command>")
        print("\nAvailable commands:")
        print("  test         - Run all tests")
        print("  test-unit    - Run unit tests only")
        print("  test-integration - Run integration tests only")
        print("  test-coverage - Run tests with coverage")
        print("  lint         - Run linting")
        print("  format       - Format code")
        print("  type-check   - Run type checking")
        print("  clean        - Clean build artifacts")
        print("  run-examples - Run example scripts")
        print("  check        - Run all checks")
        return
    
    command = sys.argv[1]
    
    commands = {
        'test': test,
        'test-unit': test_unit,
        'test-integration': test_integration,
        'test-coverage': test_coverage,
        'lint': lint,
        'format': format_code,
        'type-check': type_check,
        'clean': clean,
        'run-examples': run_examples,
        'check': check,
    }
    
    if command not in commands:
        print(f"Unknown command: {command}")
        print("Available commands:", ", ".join(commands.keys()))
        return
    
    success = commands[command]()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()