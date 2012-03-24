import dbus

bus = dbus.SessionBus()
remote = bus.get_object('org.trayicond', '/daemon')
trayicon = dbus.Interface(remote, 'org.trayicond')
trayicon.set_icon('/home/rubens/.weechat/rec/chat.png')

trayicon.set_blinking(True)
trayicon.play_sound('~/.weechat/rec/type.wav')


