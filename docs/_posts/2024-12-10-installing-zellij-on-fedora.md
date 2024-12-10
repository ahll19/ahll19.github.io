---
layout: post
title: 'Installing Zellij on Fedora'
author: "Anders Lauridsen"
categories: journal
tags: [Fedora, Rust, Zellij, Unix]
image: posts/2024-12-10/image.png
---

This guide outlines the process of installing [Zellij](https://zellij.dev/),
a Rust-based terminal workspace and multiplexer, on [Fedora Linux](https://fedoraproject.org/). While Zellij
can typically be installed using Cargo, the Rust package manager, I encountered
compilation issues on a fresh Fedora installation. Finding limited documentation
for resolving this, I’ve compiled this step-by-step guide to help others.

**Table of Contents**

---

- [Installing Rustup](#installing-rustup)
- [Dependencies](#dependencies)
- [Compiling Zellij](#compiling-zellij)

---

# Installing Rustup
The recommended way of installing Rust on Linux is using Rustup.
I ran the following command from the [Rust install site].

The recommended way to install Rust on Linux is via Rustup. You can use the following
command from the [official Rust installation site](https://www.rust-lang.org/tools/install):

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```
Choose the recommended settings during the installation process.
This will set up Rust quickly and easily.

# Dependencies
Trying to install Zellij without installing additional dependencies will result
in errors. These are the dependencies I installed before Zellij would compile,
- `gcc`
- `openssl`
- `rust-openssl-sys-devel`
- `perl`
which can all be installed with `dnf`.

The step which fails without these dependencies is when the Rust compiler tries to build
openssl. In order to build openssl Perl is needed, so I suspect that you only need to run

```sh
sudo dnf install perl
```

However, if this does not work, you might want to try and install all the other
dependencies. With that in place, you should be able to install Zellij.

# Compiling Zellij
With Rust and the necessary dependencies installed, you can compile Zellij using Cargo.
Follow the instructions from the [official Zellij documentation](https://zellij.dev/documentation/installation.html):
```sh
cargo install --locked zellij
```

If you’ve installed the dependencies mentioned earlier, this command should execute without any errors.