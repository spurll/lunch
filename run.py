#!/usr/bin/env python
from app import app, views
views.clear_vogts()				# In case options have changed.
print "Reset vogts!"
app.run(app.config.get('HOST'), app.config.get('PORT'), debug=app.config.get('DEBUG'))
