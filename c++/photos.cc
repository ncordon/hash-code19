#include <bits/stdc++.h>
using namespace std;

typedef string Tag;

struct Photo {
  // If it is not horizontal, it is vertical
  bool horizontal;
  int index;
  unordered_set<Tag> tags;
};


struct Slide {
  unordered_set<Tag> tags;
  vector<int> indexes;

  Slide(Photo horizontal) {
    tags = horizontal.tags;
    indexes.push_back(horizontal.index);
  }

  Slide(Photo v1, Photo v2) {
    indexes.push_back(v1.index);
    indexes.push_back(v2.index);
    tags = v1.tags;

    for (auto tag: v2.tags) {
      tags.insert(tag);
    }
  }

  void print() {
    for (auto index: indexes)
      cout << index << " ";

    cout << endl;
  }  
};

int score(Slide& _current, Slide& _next) {
  int current_size = _current.tags.size();
  int next_size = _next.tags.size();

  if (current_size <= next_size) {
    int intersection = 0;

    for (auto tag : _current.tags) {
      if (_next.tags.count(tag) > 0) {
        ++intersection;
      }
    }

    return min( min(current_size - intersection, intersection),
                (next_size - intersection) );
  } else {
    return score(_next, _current);
  }
}

bool slideCompare(Slide& one, Slide& two) {
  return one.tags.size() <  two.tags.size();
}

int main() {
  long num_photos;
  int num_tags;
  char horizontal_flag;
  string current_tag;
  cin >> num_photos;
  
  vector<Photo> verticals;
  vector<Slide> ordered_slides;
  vector<Slide> solution;
  
  for (int i = 0; i < num_photos; ++i) {
    cin >> horizontal_flag;
    cin >> num_tags;

    unordered_set<Tag> tags;

    for (int j = 0; j < num_tags; ++j) {
      cin >> current_tag;
      tags.insert(current_tag);
    }

    if (horizontal_flag == 'H')
      ordered_slides.push_back(Slide(Photo({true, i, tags})));
    else
      verticals.push_back(Photo({false, i, tags}));
  }

  // Tie each vertical to the following one
  for (int i = 0; i < verticals.size(); i += 2) {
    if (i + 1 < verticals.size())
      ordered_slides.push_back(Slide(verticals[i], verticals[i + 1]));
  }

  sort(ordered_slides.begin(), ordered_slides.end(), slideCompare);
  list<Slide> slides(ordered_slides.begin(), ordered_slides.end());
  
  // Greedy aproach
  auto first = slides.begin();
  solution.push_back(*first);
  slides.erase(first);
  
  while (!slides.empty()) {
    Slide current = solution.back();
    auto it = slides.begin();
    auto end = slides.begin();
    int num_slides = slides.size();
    advance(end, min(num_slides, 1000));
    
    list<Slide>::iterator best = it;
    int max_score = -1;
    
    while(it != end) {
      int current_score = score(current, *it);
      if (current_score > max_score) {
        best = it;
        max_score = current_score;
      }
      
      ++it;
    }
    
    solution.push_back(*best);
    slides.erase(best);
  }

  cout << solution.size() << endl;
  
  for (auto slide : solution) {
    slide.print();
  }
  
}
