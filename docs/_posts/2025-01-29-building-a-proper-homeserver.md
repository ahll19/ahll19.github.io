---
layout: post
title: 'Building a Proper Home Server'
author: "Anders Lauridsen"
categories: journal
tags: [HexOS, TrueNAS, Hardware, Server, Selfhosted, Unix, DIY]
image: royalty_free/server.jpeg
---

Ever since I was a teenager, I've wanted a home server. Not because I needed to host specific software or had concrete plans for it, but mainly because I saw people on YouTube who had them, and I thought it looked cool.

Flash forward a couple of years, and I'm visiting my parents. They pull out an old hard drive enclosure so we can watch some old pictures and home videos from vacations and such. It's a great time. When we're done, I ask how old the enclosure is and whether they keep any backups. The hard drive in the enclosure is from 2006, and no, they do not keep any backups. So that's 40GB of childhood memories stored in an enclosure that could fail at any moment. That was when I decided I needed to back it up somehow. And that's why I built my first home server.

**Table of Contents**

---

- [The Old Setup](#the-old-setup)
- [The New Setup](#the-new-setup)
  - [Choice of Software](#choice-of-software)
  - [Hardware](#hardware)
  - [Putting it all Together](#putting-it-all-together)
- [Conclusion](#conclusion)

---

# The Old Setup

My dad had an old Acer Aspire XC-886 desktop lying around with a 9th-gen i3 CPU, which I ended up using for the server. I bought two 1TB SSDs and installed Ubuntu Server 22.04 on the desktop. I used [mdadm](https://linux.die.net/man/8/mdadm) to create a RAID 1 array over the two SSDs for redundancy.

I installed [Nextcloud](https://nextcloud.com/) to back up all of the videos and photos from the hard drive. I chose Nextcloud because it did what I needed (and more), seemed easy to install, and offered Office-like capabilities I thought I might use later. Eventually, I bought a domain, got a static IP from my ISP, and made the service available to my family.

As time went on, I wanted to run more software on the Acer server. I tried running [Pi-hole](https://pi-hole.net/) (but DNS is a pain, so I ditched that) and ended up running [Home Assistant](https://www.home-assistant.io/) instead. [This](https://anders-lauridsen.dk/smarthome_saga_part_1) is my latest post on that journey at the time of writing.

So that was my setup before building the new server: an old Acer desktop running Home Assistant and Nextcloud, with ports forwarded for remote access.

# The New Setup

I got a Raspberry Pi 5 for my birthday and started tinkering with homelabbing again. I knew I wanted to run more services locally, such as [Jellyfin](https://jellyfin.org/), and I wanted a "proper" server to do so—"proper" meaning a dedicated build. I also wanted an easier and more reliable way to back up my data remotely, which felt clunky given that I had installed Nextcloud using Snap and intended to run everything else through Docker Compose.

## Choice of Software

I created a list of the services I wanted to host:

* Home Assistant
* Nextcloud
* Jellyfin
* One or more SMB shares with plenty of space for my Canon camera photos

Around this time, I heard about [HexOS](https://hexos.com/), a paid software built on [TrueNAS Scale](https://www.truenas.com/truenas-scale/), which supposedly makes it easier to use TrueNAS. Even if I didn't end up using HexOS, I could always fall back to TrueNAS, and I liked the project, so I decided to support them by buying a license.

## Hardware

With the software plan in place, I needed hardware to match these requirements:

* Plenty of hard drive bays
* Enough CPU power for seamless movie streaming while running all my services
* Ample RAM for caching files (TrueNAS Scale uses ZFS, which benefits from extra RAM)
* A case that wouldn't make my living room look like a server room

Here’s what I bought:

| Part         | Model                                                                        |
| ------------ | ---------------------------------------------------------------------------- |
| CPU          | Intel i5-13400F                                                              |
| Motherboard  | GIGABYTE H610I                                                               |
| RAM          | Corsair Vengeance LPX DDR4-3200 64GB CL16                                    |
| Storage      | SK Hynix Platinum P41 SSD 500GB (boot), 2 x Seagate Exos 7E10 4TB HDD (mass) |
| Power Supply | Lian Li SP750 SFX Gold                                                       |
| Case         | Jonsbo N3 Mini-ITX                                                           |
| Fans         | 2 Noctua NF-A8                                                               |

I still need to buy some Noctua fans for the hard drive bay, as the included ones are quite loud.

## Putting it all Together

Building the system was great fun, though I wouldn't recommend assembling in the Jonsbo case without prior experience. I built the SSD, motherboard, CPU, and RAM outside the case, added a GPU for video output, and installed the OS. I later realized that using a laptop with a replaceable SSD would have made installation easier.

HexOS lived up to its branding—it was easy to install and set up an SMB share. However, many supported apps still require configuration through the TrueNAS dashboard. Despite that, I do recommend HexOS for quickly turning an old PC into a NAS.

Right now, my setup is a bit scattered, but I plan to consolidate everything onto the HexOS system. Currently, I have:

* **Raspberry Pi 5**: Runs [Nginx Proxy Manager](https://nginxproxymanager.com/) for handling SSL certificates and routing traffic.
* **Acer Server**: Runs Home Assistant, Nextcloud, and [Tandoor](https://tandoor.dev/). I plan to migrate these services to HexOS and repurpose the SSDs.
* **HexOS Server**: Runs [FreshRSS](https://www.freshrss.org/), [Flame](https://github.com/pawelmalak/flame), Jellyfin, [qBittorrent](https://www.qbittorrent.org/), [Unifi Controller](https://www.ui.com/), [MeTube](https://github.com/alexta69/metube), and SMB shares.

One limitation is that HexOS only allows expanding storage pools with three or more drives, meaning I'll need to buy three new HDDs before expanding storage.

# Conclusion

It might have been wiser to buy a motherboard with 2.5Gb Ethernet, and had I known about the storage pool expansion limitation, I would have bought another drive upfront. Otherwise, I’m very proud of the system.

My homelab setup is still somewhat janky, with three different installation methods (Snap, Docker in TrueNAS, and Docker Compose on Ubuntu) across three systems. However, it has the potential to become a solid setup.

There’s still a lot of work to do—migrating services, upgrading hardware, and setting up proper backups—but it's been reliable these past few weeks, and best of all, it requires NO subscription fees!

