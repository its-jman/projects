---
title: Journal
author: Josh
date: 2018-2-18
time: 06:15 CST
edits:
  -
    date: 2018-2-19
    time: 16:12 CST
    details: Added Resources and fixed typos
---
## Beginnings
Initially this project had a sole goal of keeping track of my coding projects. As I both configured the program and wrote the first piece that would be on there, I realized there were two separate things that I wanted to achieve. A blog, and a single-page wiki of sorts. Both would look the same, but there needed to be a separate place to display the list of each of them (Still TBD).

## Requirements
When I started creating this project I had a myriad of ideas swirling around. If I was to make the "perfect" project here, I would want the following features:
  * Single page application
  * User authentication
  * Upload/WYSIWYG/Markdown editor on site
  * Commenting

I was definitely invested in creating this project, but I knew there was no reason for me to use any paid host. That dropped a lot of the ideas off of the board, and also forced me into accepting a simpler solution. Looking back, that was a great restriction to set for myself. Getting the project configured and off of the ground was significantly more important that adding unnecessary features. My final needs came down to the following few:
  * Free hosting
  * Static pages -> Fast load time, no complex backend.
  * Homepage that lists all articles

With those simple requirements, there were a few options still. The most obvious idea that I had started with was to use Github Pages. Free, simple, automated, and plenty of support from community. In my trekking I stumbled across this [post](https://news.ycombinator.com/item?id=16346187) on HN. It gave me hesitation to continue with Github Pages since it offered a free opportunity (Netlify) to do many of the complex ideas I initially had. I even proceeded to attempt to move the site entirely to the service. Thankfully, in this process I realized how much I was overcomplicating the simple task that was already automated within Github Pages.

## Creation
With my choices finalized, I moved my focus on to configuring Github Pages. It is initially setup using the [username].github.io domain, with subpages based on project (eg. /my-project/). This comes with built in HTTPS and is simple to setup, however, I wanted to use my own domain. It was a simple config change to move the domain, though this did not come with HTTPS. This is still a bit of a stumbling point, since the hosting provided by Github Pages to an external domain is not secured. I am unsure if there is a way to give Github a certificate to secure by default, so a workaround was needed.

Cloudflare, to the rescue... Before finding recommendations to use their service, I thought it was simply DOS protection. However, they also provide DNS, SSL, caching, and other features to personal websites for free. Since they are a DNS service that provides SSL at the top layer, my custom domain was now able to be provided on HTTPS. I moved my DNS hosting from Route 53 to their service to gain this functionality. This possibly comes as false security though. Since this is only SSL on the DNS layer (?), the connection from the DNS to the Github Pages ip is still an unsecured connection (if I understand correctly.) Worth worrying about eventually, but not worth holding up development and completion of the project.

The next major hurdle to overcome was Jekyll's build in blog-handling. They push you into using a format that specifies the date and slug in the filename. This wasn't a feature that I wanted to deal with, and it seemed to be locked in to not be able to be turned off. Looking back, I might be able to configure the posts folder to use custom processing (like I am doing for my own folder anyway.) I decided to completely avoid any built in handling done by Jekyll by creating a "collection" with custom rules for processing. With the processing/templating finalized, I was then able to figure out how I wanted the site to be stylized. I had created a blog styling in an earlier class, so I decided to simply copy that over.

## Final Thoughts
There are several items that I could certainly take another look at to improve some aspects of the site.
  * Improve the homepage
    * Blog posts (with an excerpt)
    * Project pages (with just the name)
  * SSL situation
  * Add SEO/META tags to improve accessibility.

As a whole though, I am very happy with how quickly I turned this project around. No over-complication, no unnecessary libraries, I just wrote what needed to be done and did it.


## Resources
  * [GitHub Help](https://help.github.com/categories/customizing-github-pages/)
  * [Build a Blog](https://www.smashingmagazine.com/2014/08/build-blog-jekyll-github-pages/)
  * [Guide to Creating Site on Github](http://jmcglone.com/guides/github-pages/)
  * [Jekyll Docs](https://jekyllrb.com/docs/home/)
