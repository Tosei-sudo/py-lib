import subprocess

BIN_PATH = 'C:/Users/**/work/py-lib/cspy/bin/'

def MessageBox(message, title='Message', buttons='YesNoCancel', icon='info'):
    exe_path = BIN_PATH + 'MessageBox.exe'
    return subprocess.call([exe_path, message, title, buttons, icon])

print(MessageBox('Hello, World!'))