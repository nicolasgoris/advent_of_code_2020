import sys, re

def part1and2(lines):
  part1 = part2 = 0
  for line in lines:
    number1, number2, letter, password = re.search('([0-9]+)-([0-9]+) (.): (.+)', line).groups()
    number1, number2 = int(number1), int(number2)
    part1 += number1 <= password.count(letter) <= number2
    part2 += (password[number1 - 1] == letter) != (password[number2 - 1] == letter)
  return part1, part2

assert len(sys.argv) == 2
passwords = open(sys.argv[1]).read().splitlines()
result = part1and2(passwords)
print(f'Part 1: {result[0]} - Part 2: {result[1]}')