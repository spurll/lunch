Lunch Voter
===========

A Python/Flask voting system that makes use of a basic scoring (voting) method to select a restaurant to order lunch from or a game to play (or any number of other things). Can also send reminders and results via Slack messages. Authentication is done via LDAP (so you'll need access to an LDAP server), and votes are stored in an SQLite DB.

Usage
=====

Requirements
------------

* flask (0.10)
* flask-login
* flask-wtf (0.8.4)
* flask-sqlalchemy (0.16)
* sqlalchemy (0.7.9)
* python-ldap
* [slackutils](https://github.com/spurll/slackutils/)

Configuration
-------------

Before starting the server for the first time, run `db_create.py`.

Starting the Server
-------------------

Start the server with `run.py`. By default it will be accessible at `localhost:9999`. To make the server world-accessible or for other options, see `run.py -h`.

Bugs and Feature Requests
=========================

Feature Requests
----------------

None

Known Bugs
----------

* The "Ballots Cast" list includes ballots cast *for any type of voting*. It should be restricted to the current type (lunch, game, etc.).

Special Thanks
==============

The web.py version was ported to Flask with the help of [Miguel Grinberg's excellent mega-tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

LDAP authentication was achieved with the help of [BCJ](https://github.com/bcj).

License Information
===================

Written by Gem Newman. [GitHub](https://github.com/spurll/) | [Blog](http://www.startleddisbelief.com) | [Twitter](https://twitter.com/spurll)

This work is licensed under Creative Commons [BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/).

Fork-and-knife icon by [Freepik](http://www.freepik.com) from [Flaticon](http://www.flaticon.com), licensed under Creative Commons [BY 3.0](https://creativecommons.org/licenses/by/3.0/).
