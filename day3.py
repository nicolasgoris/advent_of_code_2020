import sys

def tree_count(forest, r_slope, c_slope):
  r_max, c_max = len(forest), len(forest[0])
  row = col = trees = 0
  while row < r_max:
    trees += forest[row][col] == '#'
    row += r_slope
    col = (col + c_slope) % c_max
  return trees

def part2(forest, move_paterns):
  result = 1
  for m in move_paterns:
    trees = tree_count(forest, m[0], m[1])
    result *= trees
  return result

assert len(sys.argv) == 2
forest = open(sys.argv[1]).read().splitlines()
move_paterns = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

print(f'Part 1: {tree_count(forest, 1, 3)} - Part 2: {part2(forest, move_paterns)}')