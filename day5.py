import sys

def getSeatList(input, nr_rows, nr_seats):
  list = []
  for bsp in input:
    n, row, seat = 0, (0, nr_rows - 1), (0, nr_seats - 1)
    while n < len(bsp):
      if bsp[n] == 'F':
        row = (row[0], row[1] - ( (row[1] - row[0]) // 2 ) - 1)
      elif bsp[n] == 'B':
        row = (row[0] + ( (row[1] - row[0]) // 2 ) + 1, row[1])
      elif bsp[n] == 'L':
        seat = (seat[0], seat[1] - ( (seat[1] - seat[0]) // 2 ) - 1)
      elif bsp[n] == 'R': 
        seat = (seat[0] + ( (seat[1] - seat[0]) // 2 ) + 1, seat[1]) 
      n += 1
    list.append(row[0] * nr_seats + seat[0])
  list.sort()
  return list

def part1(input, nr_rows, nr_seats):
  return max(getSeatList(input, nr_rows, nr_seats))

def part2(input, nr_rows, nr_seats):
  list = getSeatList(input, nr_rows, nr_seats)
  s_min, s_max = min(list), max(list)
  for i in range(s_min+8, s_max-8):
    if i not in list:
      return i

assert len(sys.argv) == 2
input = open(sys.argv[1]).read().split()

print(f'Part 1: {part1(input, 128, 8)} - Part 2: {part2(input, 128, 8)}')