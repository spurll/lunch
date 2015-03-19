Lunch Voter
===========

A Python 3/Flask voting system that makes use of a basic scoring (voting) method to select a restaurant to order lunch from or a game to play (or any number of other things). Can also send reminders and results via Slack messages. Authentication is done via LDAP (so you'll need access to an LDAP server), and votes are stored in an SQLite DB.

Usage
=====

Requirements
------------

* flask
* flask-login
* flask-wtf
* flask-sqlalchemy
* sqlalchemy
* ldap3
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

* The "Remember Me" option on the login page doesn't seem to work anymore.
* The "Reset" button on the voting page doesn't update the numeric label fields and causes strange behaviour with the JavaScript that does category-wide updates.

Special Thanks
==============

The web.py version was ported to Flask with the help of [Miguel Grinberg's excellent mega-tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

License Information
===================

Written by Gem Newman. [GitHub](https://github.com/spurll/) | [Blog](http://www.startleddisbelief.com) | [Twitter](https://twitter.com/spurll)

This work is licensed under Creative Commons [BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/).

Fork-and-knife icon by [Freepik](http://www.freepik.com) from [Flaticon](http://www.flaticon.com), licensed under Creative Commons [BY 3.0](https://creativecommons.org/licenses/by/3.0/).
