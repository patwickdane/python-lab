from functools import reduce
import sys
from random import randint

def generate_random_numbers(size):
  def reducer(acc, curr):
    random_number = randint(0, 100)
    return acc + [random_number]

  numbers_list = reduce(reducer, range(0,size), [])

  return numbers_list

def get_occurences(number_list):
  number_set = set(number_list)
  occ_dict = { o: 0 for o in number_set }

  def reducer(acc, curr):
    new_count = acc.get(curr, 0) + 1

    return acc | { curr: new_count }

  result = reduce(reducer, number_list, occ_dict)
  print(result)
      
    

if __name__ == '__main__':
  size = int(sys.argv[1])
  print(get_occurences(generate_random_numbers(size)))
    
