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
  int_size = len(i.tags & j.tags)
  return min(int_size,
             len(i.tags) - int_size,
             len(j.tags) - int_size)

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

def mysort(x, photos):
    return sorted(x, key = lambda i: len(photos[i].tags))

def greedy():
  photos = read_photos(sys.argv[1])
  order_h = mysort([i for i in range(len(photos)) if photos[i].orientation == 'H'], photos)
  order_v = mysort([i for i in range(len(photos)) if photos[i].orientation == 'V'], photos)

  # used = [False for _ in range(len(photos))]
  unused_h = set(range(len(order_h)))
  unused_v = set(range(len(order_v)))
  solution = []

  if len(unused_h) > 0:
    solution.append(order_h[unused_h.pop()])
  else:
    solution.append([order_v[unused_v.pop()], order_v[unused_v.pop()]])

  previous = photos[0]
  if type(solution[0]) == list:
      previous = photosum(photos[solution[0][0]], photos[solution[0][1]])
  else:
      previous = photos[solution[0]]

  while len(unused_h) > 0 or len(unused_v) > 1:

    next_h = set(itertools.islice(unused_h, min(30, len(unused_h))))
    next_v = set(itertools.islice(unused_v, min(30, len(unused_v))))

    if len(next_h) > 0:
      best_pos = [max(next_h, key = lambda p: interest(previous, photos[order_h[p]]))]
      best_score = interest(previous, photos[order_h[best_pos[0]]])
    else:
      best_score = -1
      best_pos = [-1]

    if len(next_v) >= 2:
      for p in next_v:
        for q in next_v - {p}:
          slide = photosum(photos[order_v[p]], photos[order_v[q]])
          cur_score = interest(previous, slide)

          if cur_score > best_score:
            best_score = cur_score
            best_pos = [p, q]
    else:
      unused_v = {}

    if len(best_pos) > 1:
      unused_v = unused_v - {best_pos[0], best_pos[1]}
      solution.append([order_v[best_pos[0]], order_v[best_pos[1]]])
      previous = photosum(photos[order_v[best_pos[0]]], photos[order_v[best_pos[1]]])
      #eprint("{} {}".format(best_pos[0], best_pos[1]))
    else:
      unused_h = unused_h - {best_pos[0]}
      solution.append(order_h[best_pos[0]])
      previous = photos[order_h[best_pos[0]]]
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
  greedy()
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
