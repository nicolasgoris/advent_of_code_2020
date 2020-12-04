import re

def passports_from_input(input):
  passports, clean_attributes = [], {}
  for i in range(len(input)):
    if input[i] != '':
      attributes = re.findall(r'([a-z]+):(#?\w*)', input[i])
      for a in attributes:
        clean_attributes[a[0]] = a[1]
      if i == len(input) - 1:
        passports.append(Passport(clean_attributes))
    elif input[i] == '':
      passports.append(Passport(clean_attributes))
      clean_attributes = {}
  return passports

class Passport:
  needs = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
  validation = {
    'byr': {'type': 'int', 'digits': 4, 'min': 1920, 'max': 2002 },
    'iyr': {'type': 'int', 'digits': 4, 'min': 2010, 'max': 2020 },
    'eyr': {'type': 'int', 'digits': 4, 'min': 2020, 'max': 2030 },
    'hgt': {'type': 'hgt', 'regex': '([0-9]*(cm|in)+)', 'in': { 'min': 59, 'max': 76 }, 'cm': { 'min': 150, 'max': 193 } },
    'hcl': {'type': 'reg', 'regex': '(#?[a-f0-9]*)', 'length': 7 },
    'ecl': {'type': 'str', 'list': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] },
    'pid': {'type': 'reg', 'regex': '([0-9]*)', 'length': 9 }
  }

  def __init__(self, attributes):
    self.attributes = attributes
  
  def __repr__(self):
    return str(self)
  
  def __str__(self):
    id = '<ZERO>'
    if 'cid' in self.attributes.keys():
      id = self.attributes['cid']
    return f'\n\tPassport with id: {id}, having attributes: {str(self.attributes)}\n'

  def validate_simple(self):
    for n in Passport.needs:
      if n not in self.attributes.keys():
        return False
    return True

  def validate(self):
    for v in Passport.validation:
      try:
        self.attributes[v]
        if Passport.validation[v]['type'] == 'int':
          assert(Passport.validation[v]['min'] <= int(self.attributes[v]) <= Passport.validation[v]['max'])
        if Passport.validation[v]['type'] == 'str':
          assert(self.attributes[v] in Passport.validation[v]['list'])
        if Passport.validation[v]['type'] == 'reg' and v != 'hgt':
          assert(len(re.search(r'' + Passport.validation[v]['regex'], self.attributes[v]).group(1)) == Passport.validation[v]['length'])
        if Passport.validation[v]['type'] == 'hgt' and re.search(r'' + Passport.validation[v]['regex'], self.attributes[v]).group(1):
          if 'in' in self.attributes[v]:
            assert(Passport.validation[v]['in']['min'] <= int(self.attributes[v][:-2]) <= Passport.validation[v]['in']['max'])
          if 'cm' in self.attributes[v]:
            assert(Passport.validation[v]['cm']['min'] <= int(self.attributes[v][:-2]) <= Passport.validation[v]['cm']['max'])
      except:
        return False
    return True