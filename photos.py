#! /usr/bin/python3
import sys

FILE_NAME = sys.argv[1]
first_line = True

photos = []
# tags = dict()

class Photo:
  def __init__(self, orientation, tags):
    self.orientation = orientation
    self.tags = tags

def interest(i, j):
  return min(len(i.tags & j.tags), len(i.tags - j.tags), len(j.tags - i.tags))

with open(FILE_NAME) as f:
  for line in f:
    if first_line:
      N = int(line)
      first_line = False
    else:
      orientation = line[0]
      tags = set(line.split()[2:])
      photos.append(Photo(orientation,tags))
      
# print(photos[2].tags)
print(interest(photos[1], photos[2]))

print(len(list(filter(lambda p: p.orientation == 'H', photos))))
for p in range(len(photos)):
  if photos[p].orientation == 'H':
    print(p)
