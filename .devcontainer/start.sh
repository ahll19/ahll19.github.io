#!/bin/bash
set -e

# SSHkey

# Jekyll setup
cd /workspace/docs
export GEM_HOME=/workspace/.gem
export GEM_PATH=/workspace/.gem
bundle config set path 'vendor/bundle'
bundle install

# Run the server
bundle exec jekyll serve --host 0.0.0.0 --livereload