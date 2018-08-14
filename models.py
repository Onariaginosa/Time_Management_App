from google.appengine.ext import ndb

class Character(ndb.Model):
    species = ndb.StringProperty(required = True)

class Born(ndb.Model):
    born_1 = ndb.StringProperty(required = True)
    born_2 = ndb.StringProperty(required = True)
    born_3 = ndb.StringProperty(required = True)
    owner = ndb.KeyProperty(Character)
