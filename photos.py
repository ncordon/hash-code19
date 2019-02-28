#! /usr/bin/python3
import sys

O = dict(h = 'H', v = 'V')

class Photo:
  def __init__(self, orientation, tags):
    self.orientation = orientation
    self.tags = tags

def interest(i, j):
  return min(len(i.tags & j.tags), len(i.tags - j.tags), len(j.tags - i.tags))

def photosum(i, j):
  return Photo(O.h, i.tags | j.tags)

def difference(i, j):
  return len(i.tags) + len(j.tags) - len(i.tags | j.tags)


def read_photos(filename):
  photos = []
  first_line = True

  with open(filename) as f:
    for line in f:
      if first_line:
        N = int(line)
        first_line = False
      else:
        orientation = line[0]
        tags = frozenset(line.split()[2:])
        photos.append(Photo(orientation,tags))

  return photos


if __name__ == '__main__':
  photos = read_photos(sys.argv[1])

  print(len(list(filter(lambda p: p.orientation == 'H', photos))) +
        len(list(filter(lambda p: p.orientation == 'V', photos)))//2)

  verts = []

  for p in range(len(photos)):
    if photos[p].orientation == 'H':
      print(p)
    else:
      verts.append(p)

  for p in range(0, len(verts)-1, 2):
    print(verts[p], verts[p+1])
