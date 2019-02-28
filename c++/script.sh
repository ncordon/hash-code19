#!/bin/bash

g++ photos.cc -o photos
gnome-terminal -x bash -c -- "(./photos < ../examples/a_example.txt) > ./a_example.out"
gnome-terminal -x bash -c -- "(./photos < ../examples/b_lovely_landscapes.txt) > ./b_lovely_landscapes.out"
gnome-terminal -x bash -c -- "(./photos < ../examples/c_memorable_moments.txt) > ./c_memorable_moments.out"
gnome-terminal -x bash -c -- "(./photos < ../examples/d_pet_pictures.txt) > ./d_pet_pictures.out"
gnome-terminal -x bash -c -- "(./photos < ../examples/e_shiny_selfies.txt) > ./e_shiny_selfies.out"
