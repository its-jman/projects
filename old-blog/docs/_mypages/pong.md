---
title: Pong
author: Josh
date: 2018-2-18
time: 06:15 CST
published: false
edits:
  -
    date:
    time: 
    details: 
---
## Beginnings
This idea's foundation is entirely created from a [Meth Meth Method](https://www.youtube.com/watch?v=ju09womACpQ) video. While I have no desire to learn game design, or ever be a game designer, I felt this would be a good way to ease into building projects again. This project would be the game of pong build in Javascript. 

## Requirements
I initially thought it would be unnecessary to host the project, but it should be entirely possible to have it hosted for free on Github Pages. My ideas for this project initially encompass the following:
  * Two player game -> Websockets/User auth
  * Advanced mechanics -> Multiple balls, powerups, etc.
  * Precise collision detection -> Segment/Sweep algorithms

In contrast with an entirely simplistic approach, I am not ruling out any of those advanced features. However, I realize that it is much more important to get the game working before spending huge amounts of time implementing advanced features. The feature list I will start with is as follows:
  * One user and one computer -> Follows single ball
  * Ball bounces accurately along walls
  * Score/Reset ball when it hits side walls
  * Bounce off paddle using simple collision checkX, checkY