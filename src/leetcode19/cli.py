"""Command-line interface for leetcode19."""

import argparse
import sys
from typing import List, Optional
from leetcode19 import Solution
from leetcode19.utils import parse_input_string, format_result
from leetcode19.algorithms import get_solver


def run_examples():
    """Run example two-sum problems."""
    examples = [
        {
            "nums": [2, 7, 11, 15],
            "target": 9,
            "description": "Basic example"
        },
        {
            "nums": [3, 2, 4],
            "target": 6,
            "description": "Middle indices example"
        },
        {
            "nums": [3, 3],
            "target": 6,
            "description": "Duplicate values example"
        },
        {
            "nums": [-1, -2, -3, -4],
            "target": -7,
            "description": "Negative numbers example"
        },
        {
            "nums": [0, 4, 3, 0],
            "target": 0,
            "description": "Zero target example"
        }
    ]
    
    print("=== Two Sum Examples ===\n")
    
    for i, example in enumerate(examples, 1):
        print(f"Example {i}: {example['description']}")
        print(f"Input: nums = {example['nums']}, target = {example['target']}")
        
        try:
            solution = Solution()
            result = solution.twoSum(example['nums'], example['target'])
            print(f"Result: indices {result}")
            print(f"Verification: {format_result(example['nums'], result)}")
        except Exception as e:
            print(f"Error: {e}")
        
        print()


def run_interactive():
    """Run interactive two-sum problem solver."""
    print("=== Two Sum Interactive Solver ===")
    print("Enter a list of numbers (comma-separated) and a target sum.")
    print("Available commands:")
    print("  'quit' or 'q' - Exit the program")
    print("  'help' or 'h' - Show this help message")
    print("  'examples' or 'e' - Show example problems")
    print("  'algorithms' or 'a' - Show available algorithms")
    print()
    
    while True:
        try:
            # Get algorithm choice
            algorithm = input("Choose algorithm (hashmap/bruteforce/twopointer) [hashmap]: ").strip()
            if not algorithm:
                algorithm = "hashmap"
            
            if algorithm.lower() in ['quit', 'q']:
                break
            elif algorithm.lower() in ['help', 'h']:
                print("Available commands:")
                print("  'quit' or 'q' - Exit the program")
                print("  'help' or 'h' - Show this help message")
                print("  'examples' or 'e' - Show example problems")
                print("  'algorithms' or 'a' - Show available algorithms")
                print()
                continue
            elif algorithm.lower() in ['examples', 'e']:
                run_examples()
                continue
            elif algorithm.lower() in ['algorithms', 'a']:
                print("Available algorithms:")
                print("  hashmap     - O(n) time, O(n) space (default)")
                print("  bruteforce  - O(n²) time, O(1) space")
                print("  twopointer  - O(n log n) time, O(1) space")
                print()
                continue
            
            # Validate algorithm
            try:
                solver = get_solver(algorithm)
                print(f"Using {algorithm} algorithm")
            except ValueError:
                print(f"Invalid algorithm: {algorithm}")
                print("Available algorithms: hashmap, bruteforce, twopointer")
                print()
                continue
            
            # Get input
            nums_input = input("Enter numbers (comma-separated): ").strip()
            if nums_input.lower() in ['quit', 'q']:
                break
            
            target_input = input("Enter target sum: ").strip()
            if target_input.lower() in ['quit', 'q']:
                break
            
            # Parse input
            nums = parse_input_string(nums_input)
            target = int(target_input)
            
            # Solve
            solution = Solution(algorithm)
            result = solution.twoSum(nums, target)
            
            # Display results
            print(f"\nResult: indices {result}")
            print(f"Verification: {format_result(nums, result)}")
            print(f"Algorithm used: {algorithm}")
            print()
            
        except ValueError as e:
            print(f"Input error: {e}")
            print("Please try again.\n")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            print("Please try again.\n")


def run_single_problem(nums_str: str, target: int, algorithm: str = "hashmap"):
    """Run a single two-sum problem."""
    try:
        nums = parse_input_string(nums_str)
        solution = Solution(algorithm)
        result = solution.twoSum(nums, target)
        
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Algorithm: {algorithm}")
        print(f"Result: indices {result}")
        print(f"Verification: {format_result(nums, result)}")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def run_benchmark(nums_str: str, target: int):
    """Run benchmark comparison of all algorithms."""
    try:
        import time
        
        nums = parse_input_string(nums_str)
        algorithms = ["hashmap", "bruteforce", "twopointer"]
        
        print(f"Benchmarking with nums = {nums}, target = {target}")
        print("-" * 60)
        print(f"{'Algorithm':<12} {'Time (s)':<12} {'Result':<15} {'Status'}")
        print("-" * 60)
        
        for algorithm in algorithms:
            try:
                solution = Solution(algorithm)
                
                start_time = time.time()
                result = solution.twoSum(nums, target)
                end_time = time.time()
                
                execution_time = end_time - start_time
                status = "Success" if result else "Failed"
                
                print(f"{algorithm:<12} {execution_time:<12.6f} {str(result):<15} {status}")
                
            except Exception as e:
                print(f"{algorithm:<12} {'N/A':<12} {'Error':<15} {str(e)}")
        
        print("-" * 60)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Two Sum Problem Solver",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  leetcode19 --examples                    # Show example problems
  leetcode19 --interactive                 # Interactive mode
  leetcode19 --nums "2,7,11,15" --target 9  # Single problem
  leetcode19 --nums "1,2,3,4,5" --target 9 --benchmark  # Benchmark
        """
    )
    
    parser.add_argument(
        "--examples", "-e",
        action="store_true",
        help="Run example problems"
    )
    
    parser.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="Run in interactive mode"
    )
    
    parser.add_argument(
        "--nums", "-n",
        type=str,
        help="Comma-separated list of numbers"
    )
    
    parser.add_argument(
        "--target", "-t",
        type=int,
        help="Target sum"
    )
    
    parser.add_argument(
        "--algorithm", "-a",
        choices=["hashmap", "bruteforce", "twopointer"],
        default="hashmap",
        help="Algorithm to use (default: hashmap)"
    )
    
    parser.add_argument(
        "--benchmark", "-b",
        action="store_true",
        help="Run benchmark comparison of all algorithms"
    )
    
    parser.add_argument(
        "--version", "-v",
        action="version",
        version="leetcode19 0.1.0"
    )
    
    args = parser.parse_args()
    
    # Handle different modes
    if args.examples:
        run_examples()
    elif args.interactive:
        run_interactive()
    elif args.nums and args.target:
        if args.benchmark:
            run_benchmark(args.nums, args.target)
        else:
            run_single_problem(args.nums, args.target, args.algorithm)
    elif args.nums or args.target:
        print("Error: Both --nums and --target are required")
        parser.print_help()
        sys.exit(1)
    else:
        # Default to interactive mode
        run_interactive()


if __name__ == "__main__":
    main()