Overview
========

A Python/Flask voting system that makes use of a basic scoring method to select a game to play or a lunch to order among people in an office (for example). Can also send reminders and results via Slack messages.

Authentication is done via LDAP (so you'll need access to an LDAP server), and votes are stored in an SQLite DB.

Installation
============

Instructions
------------

Before running for the first time, run db_create.py. Then simply execute run.py.

Bugs and Feature Requests
=========================

Feature Requests
----------------

* Display number of ballots cast

Known Bugs
----------

None

Requirements
============

* flask (0.10)
* flask-login
* flask-wtf (0.8.4)
* flask-sqlalchemy (0.16)
* sqlalchemy (0.7.9)
* python-ldap

Special Thanks
==============

The web.py version was ported to Flask with the help of Miguel Grinberg's excellent mega-tutorial.
http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

License Information
===================

Written by Gem Newman.
http://www.startleddisbelief.com

This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
