Overview
========

A Python/Flask voting system that makes use of a basic scoring method to select a game to play or a lunch to order among people in an office (for example).

Authentication is done using OpenID (it's not perfect), and votes are stored in an SQLite DB.

Former iterations used web.py and (worse still) PHP, and made use of the "instant runoff" (or "alternative") voting system.

Bugs and Feature Requests
=========================

Feature Requests
----------------

* Display X runners-up (not just the winner)

Known Bugs
----------

* There are occasional problems where the POST method doesn't seem to do aything, but this is difficult to reproduce

Requirements
============

* flask (0.10)
* flask-login
* flask-openid
* sqlalchemy (0.7.9)
* flask-sqlalchemy (0.16)
* sqlalchemy-migrate
* flask-wtf (0.8.4)

Special Thanks
==============

The web.py version was ported to Flask with the help of Miguel Grinberg's excellent megoa-tutorial.
http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

License Information
===================

Written by Gem Newman.
http://www.startleddisbelief.com

This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
