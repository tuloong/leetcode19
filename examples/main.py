"""Main module for running the two-sum solution."""

from leetcode19 import Solution


def run_example():
    """Run example two-sum problem."""
    # Example 1
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(f"Example 1: nums = {nums}, target = {target}")
    print(f"Result: indices {result} (nums[{result[0]}] + nums[{result[1]}] = {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]})")
    print()
    
    # Example 2
    nums = [3, 2, 4]
    target = 6
    result = solution.twoSum(nums, target)
    print(f"Example 2: nums = {nums}, target = {target}")
    print(f"Result: indices {result} (nums[{result[0]}] + nums[{result[1]}] = {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]})")
    print()
    
    # Example 3
    nums = [3, 3]
    target = 6
    result = solution.twoSum(nums, target)
    print(f"Example 3: nums = {nums}, target = {target}")
    print(f"Result: indices {result} (nums[{result[0]}] + nums[{result[1]}] = {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]})")


def run_interactive():
    """Run interactive two-sum problem solver."""
    print("=== Two Sum Problem Solver ===")
    print("Enter a list of numbers (comma-separated) and a target sum.")
    print("Type 'quit' to exit.")
    print()
    
    while True:
        try:
            nums_input = input("Enter numbers (comma-separated): ").strip()
            if nums_input.lower() == 'quit':
                break
            
            target_input = input("Enter target sum: ").strip()
            if target_input.lower() == 'quit':
                break
            
            # Parse input
            nums = [int(x.strip()) for x in nums_input.split(',')]
            target = int(target_input)
            
            # Solve
            solution = Solution()
            result = solution.twoSum(nums, target)
            
            print(f"Result: indices {result}")
            print(f"nums[{result[0]}] + nums[{result[1]}] = {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]}")
            print()
            
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")
            print()
        except Exception as e:
            print(f"Unexpected error: {e}")
            print("Please try again.")
            print()


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--interactive':
        run_interactive()
    else:
        print("Running examples...")
        print()
        run_example()