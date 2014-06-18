#!/usr/bin/python

from wlokalu.logging import getLogger, message
logger = getLogger('wlokalu.presence')

from models import Person, Sensor, ListSensor

#-----------------------------------------------------------------------------

def log(*args, **kwargs):
  context = kwargs.get('context')
  if context is not None:
    del kwargs['context']
    kwargs.update(context)
  return message(*args, **kwargs)

#-----------------------------------------------------------------------------

def person_entered(nick, context = None):
  if Person.objects.filter(nick = nick).count() == 0:
    Person(nick).save() # add if not exists
    logger.info(log('person entered premises', nick = nick, context = context))

def person_left(nick, context = None):
  people = Person.objects.filter(nick = nick)
  if people.count() > 0:
    people.delete()
    logger.info(log('person left premises', nick = nick, context = context))

def person(nick):
  people = Person.objects.filter(nick = nick)
  if people.count() == 0:
    return None
  else:
    return people[0]

def list_people():
  return Person.objects.all().order_by('nick')

#-----------------------------------------------------------------------------

def sensor_state(sensor_id, state, context = None):
  if isinstance(state, (list, tuple)):
    return sensor_sync_states(sensor_id, state, context)
  else:
    return sensor_update_state(sensor_id, state, context)

def list_sensors():
  return [] # TODO

#-----------------------------------------------------------------------------

def sensor_sync_states(sensor_id, states, context = None):
  pass # TODO

def sensor_update_state(sensor_id, state, context = None):
  pass # TODO

#-----------------------------------------------------------------------------
# vim:ft=python:foldmethod=marker
