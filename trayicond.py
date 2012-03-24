#!/usr/bin/python2

import gtk
import os
import dbus
import dbus.service
import dbus.mainloop.glib
import gobject
import threading


#trayicon = gtk.StatusIcon()
#trayicon.set_tooltip('test')
#trayicon.set_from_file('/home/rubens/.weechat/rec/chat.png')

def play_sound(sound):
   os.system('aplay %s -q' % sound)

class trayicond(dbus.service.Object):

   @dbus.service.method('org.trayicond', in_signature='s', out_signature='')
   def play_sound(self, sound):
      threading.Thread(target=play_sound, args=(sound,)).start()
         
   @dbus.service.method('org.trayicond', in_signature='s', out_signature='')
   def set_icon(self, icon):
      self.trayicon = gtk.StatusIcon()
      self.trayicon.set_from_file(icon)
      self.trayicon.connect('activate', self.stop_blinking)

   @dbus.service.method('org.trayicond', in_signature='b', out_signature='')
   def set_blinking(self, state):
      self.trayicon.set_blinking(state)

   def __del__(self):
      self.trayicon.set_visible(False)

   def stop_blinking(self, array):
      self.trayicon.set_blinking(False)


dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

session_bus = dbus.SessionBus()
name = dbus.service.BusName("org.trayicond", session_bus)
obj = trayicond(session_bus, '/daemon')

t = threading.Thread(target=gtk.main)
t.start()

mainloop = gobject.MainLoop()
mainloop.run
