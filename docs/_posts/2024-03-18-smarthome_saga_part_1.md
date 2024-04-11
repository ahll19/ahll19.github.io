---
layout: post
title: 'Smarthome Saga Part 1 - Getting Started'
author: "Anders Lauridsen"
categories: journal
tags: [python]
image: royalty_free/pexels-jakub-zerdzicki-17536106.jpg
---

Since I first got my own place I've wanted to get a "smarthome". My journey started out with buying an Ikea Trådfri bulb and hub, so that I could have cool RGB lights in my one-bedroom apartment. That was also around the time I first got into Linux and Python. My first foray into interacting with my smarthome outside the scope of the Ikea smarthome app, was using [pytradfri](https://github.com/home-assistant-libs/pytradfri) on my Linux laptop to control my lights. This was immensely fun, and lasted about 30 minutes before I borked my lights, and had to do a reset on them.

Over the years since I have bought more lights, some Google smart speakers, and a smart TV (which is just a TV these days...). But I never really got into self-hosting smart solutions since then, until 2023 when I received a Raspberry Pi 5 for my birthday.

This blog-post details my first dive into self-hosting my smarthome, and my hope is that it will be one of many posts talking about setting up cool features, only really allowed by self-hosting. In this post I will talk about how I set up conditional reminders, and turned my VERY old speaker system into a "smart" speaker system by using the Spotify connect protocol.

**Table of Contents**

---
- [1. Hardware](#1-hardware)
  - [Raspberry Pi 5](#raspberry-pi-5)
  - [Ikea TRÅDFRI](#ikea-trådfri)
  - [Google Nest Mini](#google-nest-mini)
  - [Old Speaker System](#old-speaker-system)
- [2. Software](#2-software)
  - [Docker and Home Assistant](#docker-and-home-assistant)
  - [Raspotify](#raspotify)
- [3. Conclusion](#3-conclusion)

---

# 1. Hardware
## Raspberry Pi 5
As mentioned before, I got a [Raspberry Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) my birthday in 2023, which has since served as the brains of my smarthome operations. The only additional hardware I have for the Pi is [the Raspberry pi 5 case](https://www.raspberrypi.com/products/raspberry-pi-5/), [the power supply](https://www.raspberrypi.com/products/27w-power-supply/), an SD card, and a USB-to-Aux cable.

In the future I would like to add the NVME hat which Jeff Geerling has an excellent [blog post](https://www.jeffgeerling.com/blog/2023/nvme-ssd-boot-raspberry-pi-5) about, and a Z-wave USB controller. The Z-wave controller would be needed in order to not rely on the IKEA Tradfri hub, and other hubs from Z-wave device manufactures like Phillips.


## Ikea TRÅDFRI
I have a few bulbs from the TRÅDFRI lineup from Ikea. All of them are hooked up to an Ikea TRÅDFRI Hub, using one of their remotes. My plan is to use the Z-wave controller in order to get rid of this hub, and these controllers, since they only really clutter my home.

If I wanted to add more Z-wave controlled devices in the future I would also like to not have 5 different hubs hooked up to ethernet and power all of the time.

Only one of these lights have died on me since I bought them. It was slightly over 3 years old, and the others (between 2 and 4 years old at this point) are still going strong.

## Google Nest Mini
I have two of these small smart speakers, one of them I bought second hand, and the other I bought new. Their sound is decent, but my hope is that I would have these replaced with proper speakers in the future. I also find that the Google "smart" assistant is often the worst way to get anything accomplished.

I only really use it for conversions between imperial and real units when cooking, or perhaps setting alarms (which could just as well be done from my phone).

## Old Speaker System
I don't know which speakers I have right now, or which amp they are connected to. I do have plans for maybe opening up the amp to make it turn on when I connect to the Raspberry Pi. If I ever do that I will of course write down some details on what I'm using.

These old speakers really do sound great when a device is hooked up to the amplifier via Aux. I personally got them from a family member who did not have the space for them anymore, but similar speakers can be had on Facebook Marketplace for cheap.

# 2. Software
The software deployed so far has been rather plug and play, with only some slight configuration needing to be done. How my software is set up as of now will most likely change, maybe I will add [Google Cast](https://developers.google.com/cast/docs/overview), maybe not.

## Docker and Home Assistant
Docker is being used to host the [Home Assistant](https://hub.docker.com/r/homeassistant/home-assistant/), since native support for the Raspberry Pi 5 was added [a few months](https://www.home-assistant.io/blog/2024/02/26/home-assistant-os-12-support-for-raspberry-pi-5/) after I set up my system...

Using Docker is not the worst thing every, since it does make porting easier, though I would like to experiment with installing it on the Pi directly, once I have another micro PC as the Pi Zero 2 W running Raspotify on the speaker system.

I used Docker-Compose to run the container, the guide I took inspiration from can be found [here](https://www.thetechnerd.org/articles/installing-home-assistant-using-docker-a-step-by-step-guide).

Here is my `docker-compose.yaml`{:#id}{:.class}

~~~yaml
version: '3'
services:
  homeassistant:
    container_name: homeassistant
    image: "ghcr.io/home-assistant/home-assistant:stable"
    volumes:
      - /opt/homeassistant/config:/config
      - /etc/localtime:/etc/localtime:ro
    restart: unless-stopped
    privileged: true
    network_mode: host
    ports:
      - "8123:8123"
    environment:
      - DISABLE_JEMALLOC=1
~~~

I might move to installing the new native Home Assistant software on the Pi, but that would necessitate a new single board computer for running Raspotify. I have not been able to get Bluetooth working in the Docker container, so installing the OS is appealing.

So far the only automation I have set up is my Google Nest speakers reminding to air out the apartment a couple of times each day, if I am home. Though, I do intend to add more automations once I am working full time and have a more fixed daily schedule.

## Raspotify
[Raspotify](https://dtcooper.github.io/raspotify/) is a wrapper around a Rust library, which allows it to function as a Spotify Connect receiver. It is technically for Debian 11, and Raspberry Pi OS is based on Debian 12, but the install script worked perfectly fine for me. If the script turned out to not work I don't believe it would be too hard to Dockerize the application.

Setting up the software once it is installed was not all that difficult. The workflow consists mostly of

~~~shell
sudo nano /etc/raspotify/conf
systemctl restart raspotify
~~~

Knowing what needs to be changed can be gathered by looking at 
~~~shell
journalctl -u raspotify.service -b
~~~

I didn't write my steps down, and this is not a detailed guide, so I won't provide the exact steps to reproduce this setup in this post, but my configuration can be found in [the GitHub repo](https://github.com/ahll19/ahll19.github.io/tree/master/docs/assets/etc_confs).

I also used the `alsamixer`{:#id}{:.class} CLI tool to turn up the volume on the Pi, in hopes that I would be able to go over a larger volume range once connected over Spotify. I don't know how this is handled by Raspotify, and therefore I don't know if it is worth replicating. But it is there as a troubleshooting step.

# 3. Conclusion
Running Home Assistant in Docker on a machine that is also connected to my old speaker setup over AUX seems like a "proof of concept" state of my smarthome. Given this I would like to invest in some more hardware, such as a Z-wave USB controller, and some Z-wave devices which aren't just smart lights, such as blinds or electricity meters.

I am pretty happy with what my smarthome is so far. I am able to play music on my nice speaker system, without hassle, or spending a fortune on new smart speakers. I am also a fan of being able to create automations without relying on [Google keeping functionality available for many years](https://killedbygoogle.com/), since it would be a shame if they killed off Google Home after I spend several hours setting up automations in that framework.

I am looking forward to adding more devices to my ecosystem, and playing around with Home Assistant some more.