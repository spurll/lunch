Overview
========

A web.py-based voting system that makes use of a basic scoring method to select a game to play or a lunch to order among people in an office (for example).

Formerly: A PHP-based web program that allows users to select a game to play using the popular "instant runoff" voting system. It's fairly ugly.

Bugs and Feature Requests
=========================

Feature Requests
----------------

* Button should move to next type of vote (instead of toggle between the only two types)
* Don't hard-code "game" and "lunch"; define it by the JSON
* Navigating to / should go to /{first type}
* Auto-create data/{type} directories if they don't exist
* Display X runners-up (not just the winner)
* Write an actual log-in page (and a sign-up page, I guess?)

Known Bugs
----------

* The favicon doesn't work
* Passwords are stored in plaintext
* There's no way to "sign out"

License Information
===================

Written by Gem Newman.
http://www.startleddisbelief.com

This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
