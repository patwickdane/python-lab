import sys

def open_file(url):
  lines = []
  with open(url) as file:
    lines.append(file.readline())  

  return lines
