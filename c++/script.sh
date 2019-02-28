#!/bin/bash

g++ photos.cc -o photos
(./photos < ../examples/a_example.txt) > ./a_example.out
(./photos < ../examples/b_lovely_landscapes.txt) > ./b_lovely_landscapes.out
(./photos < ../examples/c_memorable_moments.txt) > ./c_memorable_moments.out
(./photos < ../examples/d_pet_pictures.txt) > ./d_pet_pictures.out
(./photos < ../examples/e_shiny_selfies.txt) > ./e_shiny_selfies.out
