#include <bits/stdc++.h>
using namespace std;

typedef string Tag;

struct Photo {
  // If it is not horizontal, it is vertical
  bool horizontal;
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
    for (auto photo: photos) {
      if (photo.horizontal)
        cout << "H" << " ";
      else
        cout << "V" << " ";
      
      cout << photo.tags.size() << " ";

      for (auto tag : photo.tags) {
        cout << tag << " ";
      }
      
      cout << endl;
    }
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
  int num_horizontals;
  int num_verticals;
  
  list<Photo> horizontals;
  list<Photo> verticals;
  vector<Slide> slides;
  
  for (int i = 0; i < num_photos; ++i) {
    cin >> horizontal_flag;
    cin >> num_tags;

    unordered_set<Tag> tags;

    for (int j = 0; j < num_tags; ++j) {
      cin >> current_tag;
      tags.insert(current_tag);
    }

    if (horizontal_flag == 'H') {
      horizontals.push_back({true, tags});
    } else {
      verticals.push_back({false, tags});
    }
  }

  num_horizontals = horizontals.size();
  num_verticals = verticals.size();

  // Greedy aproach for horizontal photos only
  auto current = horizontals.begin();
  slides.push_back(Slide(*current));
  horizontals.erase(current);
  
  while (!horizontals.empty()) {
    auto it = horizontals.begin();
    list<Photo>::iterator best;
    int max_score = -1;
    Slide current_slide = Slide(*current);
    
    while(it != horizontals.end()) {
      Slide next_slide = Slide(*it);
      int current_score = score(current_slide, next_slide);

      if (current_score > max_score) {
        best = it;
        max_score = current_score;
      }
      
      ++it;
    }

    current = best;
    slides.push_back(Slide(*current));
    horizontals.erase(current);
  }

  cout << slides.size() << endl;
  
  for (auto slide : slides) {
    slide.print();
  }
  
}
