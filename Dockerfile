FROM ubuntu:jammy

WORKDIR /root/
RUN apt-get update && apt-get upgrade -y

# Following guide from Jekyll
RUN apt-get install ruby-full build-essential zlib1g-dev git glibc-source -y
# RUN echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
# RUN echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
# RUN echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
# RUN source ~/.bashrc
RUN gem install jekyll bundler
RUN mkdir -p ahll19.github.io
WORKDIR /root/ahll19.github.io