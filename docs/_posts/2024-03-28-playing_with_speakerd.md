---
layout: post
title: 'Playing with old speakers'
author: "Anders Lauridsen"
categories: journal
tags: [python, rust, speakers, diy, electronics]
image: posts/2024-03-17/placeholder.jpg
---

# Speaker Notes

**Todo**
1. Make schematic of speaker internals
   1. [Cement resistors](https://www.bennic.com.tw/catalogue/en/Resistors-en.pdf) (white boxy things) 
   2. [film capacitor](https://frequence.dk/hifi/424-bennic-capacitors/6728-bennic-mt-10-microf-100v-5/) (not this exact one but something close)
   3. Perhaps the copper coils are inductors? Check out my reddit post I guess.
2. Add link to speaker brochure, probably through internet archive or something

## Wiring
Extremely difficult to find information on caps and coils

# Software Notes
[Snapcast inspiration and guide](https://whynot.guide/posts/howtos/multiroom-media/)
- Pi5 running snapcast server 
- pi3a+ running snapcast client
- Dell workstation running Home Assistant in docker

## Snapcast
On the [GitHub Page](https://github.com/badaix/snapcast) of Snapcast they say that

>Snapcast is a multiroom client-server audio player, where all clients are time synchronized with the server to play perfectly synced audio. It's not a standalone player, but an extension that turns your existing audio player into a Sonos-like multiroom solution.

*something something fitting my needs*

### First Setup
Since Snapcast is distributed to Debian based systems, I could just download and install the packages from the [release page](https://github.com/badaix/snapcast/releases).

After installing the correct packages I went and tested the setup. I have my Pi 5 and Pi 3A+ hooked up to the same network, and my headphones plugged into the AUX port of the Pi 3A+ . After opening up a terminal on the Pi 3A+ I opened `alsamixer` to turn the volume, in order to not blow out the speakers of my headphones. I then ran the `snapclient` command to spawn the client, and logged into my Pi 5. On the Pi 5 I have tmux installed, and opened up a session. In the first window I started the server by running `snapserver`. I opened up a new window, and then ran `cat /dev/urandom > /tmp/snapfifo`. This should start playing white noise on the headphones plugged into the headphones.

The files `/dev/random` and `/dev/urandom` provide an interface to the random number generator in the Linux kernel, the difference between them being that the form the former will block reading if the system is not able to generate "random enough" numbers, and the latter will never be blocked. This is lifted from [this post](https://linuxhandbook.com/dev-random-urandom/) from the Linux Handbook.

When I first did this I ran into permission issues, since Snapcast creates a user and group for that user called `snapserver`, on the server. I had to change the ownership of the file using `chown` in order to test this in my case, but switched the owner back after testing.