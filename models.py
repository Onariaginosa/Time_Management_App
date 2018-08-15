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
    owner = ndb.KeyProperty(Character)

class Path(ndb.Model):
    p_1a = ndb.StringProperty(repeated = True)
    p_1b = ndb.StringProperty(repeated = True)
    p_2a = ndb.StringProperty(repeated = True)
    p_2b = ndb.StringProperty(repeated = True)
    p_3a = ndb.StringProperty(repeated = True)
    p_3b = ndb.StringProperty(repeated = True)
    owner = ndb.KeyProperty(Character)

class Looper(ndb.Model):
    loop_1 = ndb.StringProperty(required = True)
    loop_2 = ndb.StringProperty(required = True)
    loop_3 = ndb.StringProperty(required = True)
    run = ndb.StringProperty(required = True)
    owner = ndb.KeyProperty(Character)

class KPath(ndb.Model):
    p_2a = ndb.StringProperty(required = True)
    p_2b = ndb.StringProperty(required = True)
    p_3a = ndb.StringProperty(required = True)
    p_3b = ndb.StringProperty(required = True)
    owner = ndb.KeyProperty(Character)
