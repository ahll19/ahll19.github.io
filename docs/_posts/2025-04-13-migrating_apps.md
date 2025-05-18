---
layout: post
title: 'Migrating Services from my old to my new Server'
author: "Anders Lauridsen"
categories: journal
tags: [home server, nextcloud, tandoor mealie, migration, truenas]
image: posts/2025-04-13/migration-3020862114.jpg
---

some intro

- [Why Migrate](#why-migrate)
  - [Home Assistant](#home-assistant)
    - [Installation on TrueNAS](#installation-on-truenas)
    - [Migration](#migration)
    - [Troubleshooting](#troubleshooting)
  - [Tandoor](#tandoor)
    - [Easy migration, and PWA instead of 3rd party app](#easy-migration-and-pwa-instead-of-3rd-party-app)
  - [Nextcloud](#nextcloud)

# Why Migrate
I described my old server setup briefly in [this](creating-a-landing-page-and-why-llms-wont-take-our-jobs) post but here's a brief excerpt from that post:

>My dad had an old Acer Aspire XC-886 desktop lying around with a 9th-gen i3 CPU, which I ended up using for the server. I bought two 1TB SSDs and installed Ubuntu Server 22.04 on the desktop. I used [mdadm](https://linux.die.net/man/8/mdadm) to create a RAID 1 array over the two SSDs for redundancy. <br> <br> I installed [Nextcloud](https://nextcloud.com/) to back up all of the videos and photos from the hard drive. I chose Nextcloud because it did what I needed (and more), seemed easy to install, and offered Office-like capabilities I thought I might use later. Eventually, I bought a domain, got a static IP from my ISP, and made the service available to my family. <br> <br>As time went on, I wanted to run more software on the Acer server. I tried running [Pi-hole](https://pi-hole.net/) (but DNS is a pain, so I ditched that) and ended up running [Home Assistant](https://www.home-assistant.io/) instead. [This](smarthome_saga_part_1) is my latest post on that journey at the time of writing. <br> <br> So that was my setup before building the new server: an old Acer desktop running Home Assistant and Nextcloud, with ports forwarded for remote access.

I wanted to have everything "under one roof", more or less. While I am ok running extra infrastructure, such as a proxy manager or geofencing, on other hardware, I wanted all of my services running on one server, preferably using the same technology (namely Docker in the form of TrueNAS Apps). This would, in theory, make backups easier, and general system administration.

I had 3 services running on my old server: Home Assistant, Tandoor, and Nextcloud. I will be covering each migration in increasing difficulty.

## Home Assistant

My old Home Assistant setup consisted of a Docker Compose file along with a mounted volume in `/opt/homeassistant/`. a setup copied from a blog I unfortunately don't remember the name of. 

```yaml
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
```

This install has been relatively unproblematic, and when I plugged in my Zigbee dongle it 'just worked'. I specifically used the *ZBDongle-E* model from Sonoff.

Given that this 'just works' setup was based on Docker, and I wanted to move it to a Docker container in TrueNAS it should be easy right? To my surprise it actually was.

### Installation on TrueNAS

I created the following datasets in TrueNAS using the App preset in the dataset creation wizard. 
![Overview of datasets](../assets/img/posts/2025-04-13/datasets.png)
In the Home Assistant configuration wizard I set all storage options to use a host path, and pointed each host path to the corresponding dataset. The only extra option which had to be set was the "Automatic Permissions" option.
![config of postgres host path](../assets/img/posts/2025-04-13/pg_permissions.png)
Other than that, my Home Assistant instance was up and running without too much hassle.

### Migration

I created a backup on my original Home Assistant instance, downloaded it to my PC, and in the new instance I chose the "restore" option on the welcome page. It was *almost* that easy...

### Troubleshooting

My ZigBee integration simply would not work. All configuration was imported correctly, but it seemed that Home Assistant could not connect to the device.

My first troubleshooting step was to check that the container could actually see the device, which was confirmed with `lsusb`.
![output from lsusb](../assets/img/posts/2025-04-13/lsusb.png)

After digging around in the terminal for a while I went back into the Home Assistant config, and found the "device" section of the config page. It turns out that I needed to map my device to the container, in order for it to use it. This was something I had not considered since `lsusb` showed the device from a shell in the container.

## Tandoor

I had installed Tandoor using Docker Compose on the old server.
TrueNAS doesn't directly support Tandoor,
and for now I don't want to install community supported apps.

Researching self-hosted recipe software can be bewildering,
but I ended up using [Mealie](https://mealie.io/) instead.

### Easy migration, and PWA instead of 3rd party app

Migrating from Tandoor to Mealie is rather easy and intuitive,
and installing the PWA is just as easy.
Good thing [Apple reversed their decision about PWAs in the EU](https://techcrunch.com/2024/03/01/apple-reverses-decision-about-blocking-web-apps-on-iphones-in-the-eu/).

## Nextcloud
...

I haven't migrated Nextcloud yet.
