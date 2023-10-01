---
layout: post
title: "Creating my Website"
author: "Anders Lauridsen"
categories: journal
tags: [website, meta]
image: royalty_free/web-design.jpg
---

- [1. My old website](#1-my-old-website)
- [2. My new website](#2-my-new-website)
  - [2.1. Idea for the new site](#21-idea-for-the-new-site)
  - [2.2. Technology behind the site](#22-technology-behind-the-site)

# 1. My old website

This is not the first iteration of my personal website. Back in December 2020 I decided to create my own personal website. My idea was to have a place to showcase whatever projects I had worked on, and perhaps for general blogging (I later realized that a 2nd semester project about [Eigenfaces](https://en.wikipedia.org/wiki/Eigenface) wouldn't exactly be the most appealing project on my site...). <br>
Even so I decided to continue to work on my site, by finding and buying a template that I liked, in order to get up and running quickly. I created a somewhat decent website if I do say so myself. If you're interested you can check out the history of commits on the [repository](https://github.com/ahll19/ahll19.github.io), though the naming of the earlier commits aren't always the most useful. Though, some idea of what the website looked like can be gleamed from the images below.

![Header of my old website](/assets/img/posts/2023-09-30/header.png "Header of my old website")

While I was, and am still, happy with how the website looked, it was difficult to change the look of the website. Since I understood none of the tools that went in to creating the first website, I had trouble changing the contents of the site (specifically adding a blog-post functionality). Instead, I was stuck with this look on the site
![Content of my old website](/assets/img/posts/2023-09-30/body.png "Content of my old website")
which does not lend itself to the blogging format.

My contact page also used a third party service, and was not really practical, so I wanted to scrap that as well.
![Old contact form](/assets/img/posts/2023-09-30/contact.png "Old contact form")

# 2. My new website
As you can see the new website is drastically different from the old one. The old website functioned as a sort of online resume, more than anything else. I generally dislike having to write resumes, so having to write two when applying for a job, or when they need updating, seemed excessively meaningless.

## 2.1. Idea for the new site
I want to work on smaller projects, as I have done for the last couple of years, but in a more structured manner. I wanted somewhere to showcase these projects, and a personal blog seemed like the perfect way to do it.

My hope is that this blog will grow with interesting subjects over time, regarding mathematics, data-analysis, home-automation, and more.

## 2.2. Technology behind the site
I host the page on GitHub Pages, since I don't need anything dynamic, and it's free to host a site there.

I searched the internet and [Jekyll](https://github.com/jekyll/jekyll) Seemed like a good choice to build the website in, so I decided to go with that, since it can build static HTML sites from Markdown, which makes my life easier.

I started out by following this [guide](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll), which worked fine in the beginning. I did have some trouble getting a TeX engine (used for creating equations like this $E=mc^2$) working both locally and on the GitHub's build system. After scouring the internet for solutions that worked either on GitHub or locally, I decided to find a template that had [Mathjax](https://www.mathjax.org/) properly configured from the get-go. And so I ended up going with [Lagrange](https://github.com/LeNPaul/Lagrange), a beautiful and easy to set up template.

Both the guide on GitHub and the guide included in the Lagrange repository are great to get started, and I highly recommend those guides if you want to build you own GitHub Pages site.
