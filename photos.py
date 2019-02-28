#! /usr/bin/python3
import sys
import itertools

O = dict(h = 'H', v = 'V')

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

class Photo:
  def __init__(self, pos, orientation, tags):
    self.pos = pos
    self.orientation = orientation
    self.tags = tags

def interest(i, j):
  return min(len(i.tags & j.tags), len(i.tags - j.tags), len(j.tags - i.tags))

def photosum(i, j):
  return Photo("{} {}".format(i.pos, j.pos), 'H', i.tags | j.tags)

def difference(i, j):
  return len(i.tags) + len(j.tags) - len(i.tags | j.tags)


def read_photos(filename):
  photos = []
  first_line = True

  with open(filename) as f:
    for pos, line in enumerate(f):
      if first_line:
        N = int(line)
        first_line = False
      else:
        orientation = line[0]
        tags = frozenset(line.split()[2:])
        photos.append(Photo(pos - 1, orientation, tags))

  return photos

def david():
  photos = read_photos(sys.argv[1])
  
  # used = [False for _ in range(len(photos))]
  unused_h = set([i for i in range(len(photos)) if photos[i].orientation == 'H'])
  unused_v = set([i for i in range(len(photos)) if photos[i].orientation == 'V'])
  solution = []

  if len(unused_h) > 0:
    solution.append(unused_h.pop())
  else:
    solution.append([unused_v.pop(), unused_v.pop()])
    
  previous = photos[0]

  while len(unused_h) > 0 or len(unused_v) > 1:
    best_score = -1
    best_pos = [-1]

    next_h = set(itertools.islice(unused_h, min(10, len(unused_h))))
    next_v = set(itertools.islice(unused_v, min(10, len(unused_v))))

    for p in next_h:
      cur_score = interest(previous, photos[p])

      if cur_score > best_score:
        best_score = cur_score
        best_pos = [p]

    if len(next_v) >= 2:
      for p in next_v:
        for q in next_v - {p}:
          slide = photosum(photos[p], photos[q])
          cur_score = interest(previous, slide)

          if cur_score > best_score:
            best_score = cur_score
            best_pos = [p, q]
    else:
      unused_v = {}

    if len(best_pos) > 1:
      unused_v = unused_v - {best_pos[0], best_pos[1]}
      solution.append(best_pos)
      previous = photosum(photos[best_pos[0]], photos[best_pos[1]])
      #eprint("{} {}".format(best_pos[0], best_pos[1]))
    else:
      unused_h = unused_h - {best_pos[0]}
      solution.append(best_pos[0])
      previous = photos[best_pos[0]]
      #eprint(best_pos[0])

  print(len(solution))
  for x in solution:
    if type(x) == list:
      assert(photos[x[0]].orientation == 'V' and photos[x[1]].orientation == 'V')
      print("{} {}".format(photos[x[0]].pos, photos[x[1]].pos))
    else:
      assert(photos[x].orientation == 'H')
      print(str(x))


if __name__ == '__main__':
  david()
  # photos = read_photos(sys.argv[1])

  # print(len(list(filter(lambda p: p.orientation == 'H', photos))) +
  #       len(list(filter(lambda p: p.orientation == 'V', photos)))//2)

  # verts = []

  # for p in photos:
  #   if p.orientation == 'H':
  #     print(p.pos)
  #   else:
  #     verts.append(p)
  # photos.sort(key=lambda x: len(x.tags))

  # for p in photos:
  #   if p.orientation == 'H':
  #     print(p.pos)
  #   else:
  #     verts.append(p)

  # for i in range(0, len(verts)-1, 2):
  #   print(verts[i].pos, verts[i+1].pos)
