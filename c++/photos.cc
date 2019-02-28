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
  vector<Photo> photos;

  Slide(Photo horizontal) {
    photos.push_back(horizontal);
  }

  Slide(Photo v1, Photo v2) {
    photos.push_back(v1);
    photos.push_back(v2);
  }

  void print() {
    if (photos.size() < 2)
      cout << photos.front().index << endl;
    else
      cout << photos.front().index << " " << photos.back().index << endl;    
  }  
};

int score(Slide &current, Slide &next) {
  Photo& _current = current.photos.front();
  Photo& _next = next.photos.front();
  
  int current_size = _current.tags.size();
  int next_size = _next.tags.size();
  
  if (current_size < next_size) {
    int intersection = 0;

    for (auto tag : _current.tags) {
      if (_next.tags.count(tag) > 0) {
        ++intersection;
      }
    }

    return min( min(current_size - intersection, intersection),
                (next_size - intersection) );
  } else {
    return score(next, current);
  }
}

int main() {
  long num_photos;
  int num_tags;
  char horizontal_flag;
  string current_tag;
  cin >> num_photos;
  
  list<Photo> photos;
  list<Slide> slides;
  vector<Slide> solution;
  
  for (int i = 0; i < num_photos; ++i) {
    cin >> horizontal_flag;
    cin >> num_tags;

    unordered_set<Tag> tags;

    for (int j = 0; j < num_tags; ++j) {
      cin >> current_tag;
      tags.insert(current_tag);
    }

    photos.push_back({horizontal_flag == 'H', i, tags});

    if (photos.back().horizontal) {
      slides.push_back(Slide(photos.back()));
    }
  }


  // Greedy aproach for horizontal photos only
  auto current = slides.begin();
  solution.push_back(*current);
  slides.erase(current);
  
  while (!slides.empty()) {
    auto it = slides.begin();
    list<Slide>::iterator best;
    int max_score = -1;
    
    while(it != slides.end()) {
      int current_score = score(*current, *it);
      
      if (current_score > max_score) {
        best = it;
        max_score = current_score;
      }
      
      ++it;
    }
    
    current = best;
    solution.push_back(*current);
    slides.erase(current);
  }

  cout << solution.size() << endl;
  
  for (auto slide : solution) {
    slide.print();
  }
  
}
