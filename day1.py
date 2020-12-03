import sys

def part1(numbers, target, left):
  right = len(numbers) - 1
  while left < right:
    tuple = numbers[left], numbers[right]
    if sum(tuple) == target:
      return tuple[0] * tuple[1]
    if sum(tuple) > target:
      right -= 1
    else:
      left += 1

def part2(numbers, target):
  for i, number in enumerate(numbers):
    result = part1(numbers, target - number, i + 1)
    if result:
      return result * number

assert len(sys.argv) == 2
numbers = list(map(int, open(sys.argv[1]).read().split()))
numbers.sort()
print(f'Part 1: {part1(numbers, 2020, 0)} - Part 2: {part2(numbers, 2020)}')