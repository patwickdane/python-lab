import sys

def byIndex(index):
  def sorter(tup):
    return tup[index]

  return sorter

def sort_by_first(pair_list):
  return sorted(pair_list, key=byIndex(0))


def sort_by_second(pair_list):
  return sorted(pair_list, key=byIndex(1))



