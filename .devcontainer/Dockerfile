FROM ubuntu:jammy

# Avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y ruby-full build-essential zlib1g-dev git && \
    rm -rf /var/lib/apt/lists/*

# Install Ruby gems
RUN gem install jekyll bundler

ARG USERNAME=anders
RUN adduser --disabled-password --gecos "" $USERNAME \
    && mkdir -p /home/$USERNAME \
    && chown -R $USERNAME:$USERNAME /home/$USERNAME
