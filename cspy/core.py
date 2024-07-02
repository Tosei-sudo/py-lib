import subprocess
import tempfile

BIN_PATH = 'C:/Users/tosei/work/py-lib/cspy/bin/'

def MessageBox(message, title='Message', buttons='YesNoCancel', icon='info'):
    exe_path = BIN_PATH + 'MessageBox.exe'
    return subprocess.call([exe_path, message, title, buttons, icon])

def FileDialog(filter_str='All files (*.*)|*.*', multi_select=False):
    exe_path = BIN_PATH + 'FileDialog.exe'
    
    selected_file = subprocess.check_output([exe_path, filter_str, str(multi_select)]).strip().split('\r\n')
    
    return selected_file

print(FileDialog())