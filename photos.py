#! /usr/bin/python3
import sys

FILE_NAME = sys.argv[1]
first_line = True

O = dict(h = 'H', v = 'V')

photos = []
# tags = dict()

class Photo:
  def __init__(self, orientation, tags):
    self.orientation = orientation
    self.tags = tags

def interest(i, j):
  return min(len(i.tags & j.tags), len(i.tags - j.tags), len(j.tags - i.tags))

def photosum(i, j):
  return Photo('H', i.tags | j.tags)

def difference(i, j):
  return len(i.tags) + len(j.tags) - len(i.tags | j.tags)

with open(FILE_NAME) as f:
  for line in f:
    if first_line:
      N = int(line)
      first_line = False
    else:
      orientation = line[0]
      tags = frozenset(line.split()[2:])
      photos.append(Photo(orientation,tags))

# print(photos[2].tags)
# print(interest(photos[1], photos[2]))

solution = [0]
# used = [False for _ in range(len(photos))]
unused = set(list(range(len(photos)))) - {0}
count_verts = len(list(filter(lambda p: p.orientation == 'V', photos)))
previous = photos[0]

while len(unused) > 0:
  best_score = -1
  best_pos = [-1]

  for p in unused:
    cur_score = -1
    cur_pos = [-1]
    
    if photos[p].orientation == 'H':
      cur_score = interest(previous, photos[p])
      cur_pos = [p]
      
      if cur_score > best_score:
        best_score = cur_score
        best_pos = cur_pos
    else:
      if count_verts < 2:
        count_verts = 0
        unused = unused - {p}
        continue
      for q in unused - {p}:
        if photos[q].orientation == 'V':
          slide = photosum(photos[p], photos[q])
          cur_score = interest(previous, slide)
          cur_pos = [p, q]

          if cur_score > best_score:
            best_score = cur_score
            best_pos = cur_pos

  for x in best_pos:
    unused = unused - {x}

  if len(best_pos) > 1:
    count_verts -= 2
    solution.append(best_pos)
    previous = photosum(photos[best_pos[0]], photos[best_pos[1]])
  else:
    solution.append(best_pos[0])
    previous = photos[best_pos[0]]

print(len(solution))
for x in solution:
  if type(x) == list:
    print(" ".join([str(y) for y in x]))
  else:
    print(str(x))
    


# M = len(list(filter(lambda p: p.orientation == 'H', photos))) + len(list(filter(lambda p: p.orientation == 'V', photos)))//2

# print(M)

# verts = []

# for p in range(len(photos)):
#   if photos[p].orientation == 'H':
#     print(p)
#   else:
#     verts.append(p)

# for p in range(0, len(verts)-1, 2):
#   print(verts[p], verts[p+1])
