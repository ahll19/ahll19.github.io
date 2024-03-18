#!/bin/bash

docker run -p 4000:4000 -p 35729:35729 -v $(pwd):/root/ahll19.github.io -it jekyll:latest bash