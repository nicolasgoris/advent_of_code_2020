import sys, re
from passport import passports_from_input

def part1(input):
  number_valid = 0
  for p in passports:
    number_valid += p.validate_simple()
  return number_valid

def part2(input):
  number_valid = 0
  for p in passports:
    number_valid += p.validate()
  return number_valid

assert len(sys.argv) == 2
passports = passports_from_input(open(sys.argv[1]).read().splitlines())

print(f'Part 1: {part1(passports)} - Part 2: {part2(passports)}')