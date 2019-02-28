#! /usr/bin/python3
import sys

FILE_NAME = sys.argv[1]
first_line = True

photos = []

class Photo:
  def __init__(self, orientation, tags):
    self.orientation = orientation
    self.tags = tags


with open(FILE_NAME) as f:
  for line in f:
    if first_line:
      N = int(line)
      first_line = False
    else:
      orientation = line[0]
      tags = line.split()[2:]
      photos.append(Photo(orientation,tags))

print(photos[2].tags)
