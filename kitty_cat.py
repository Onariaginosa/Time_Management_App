from google.appengine.ext import ndb

class Character(ndb.Model):
    species = ndb.StringProperty(required = True)
    
