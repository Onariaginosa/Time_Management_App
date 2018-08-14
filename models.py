from google.appengine.ext import ndb

class Character(ndb.Model):
    species = ndb.StringProperty(required = True)

class Born(ndb.Model):
    born_1 = ndb.StringProperty(required = True)
    born_2 = ndb.StringProperty(required = True)
    born_3 = ndb.StringProperty(required = True)
    owner = ndb.KeyProperty(Character)

class PB2(ndb.Model):
    pb_1 = ndb.StringProperty(required = True)
    pb_2 = ndb.StringProperty(required = True)
    pb_3 = ndb.StringProperty(required = True)
    owner = ndb.KeyProperty(Character)

class PPath(ndb.Model):
    PP_1 = ndb.StringProperty(required = True)
    PP_2 = ndb.StringProperty(required = True)

class Path(ndb.Model):
    p_1a = ndb.ListProperty(required = True)
    p_1b = ndb.ListProperty(required = True)
    p_2a = ndb.ListProperty(required = True)
    p_2b = ndb.ListProperty(required = True)
    p_3a = ndb.ListProperty(required = True)
    p_3b = ndb.ListProperty(required = True)
    owner = ndb.KeyProperty(Character)
