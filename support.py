def save(number, line):
    with open("%s#%s.txt" % (get_current_notebook_name(), number), "w+") as f:
        f.write(line)
        return line

def get_current_notebook_path():
    import json
    import os
    import urllib2
    import IPython
    from IPython.lib import kernel
    connection_file_path = kernel.get_connection_file()
    connection_file = os.path.basename(connection_file_path)
    kernel_id = connection_file.split('-', 1)[1].split('.')[0]

    # Updated answer with semi-solutions for both IPython 2.x and IPython < 2.x
    if IPython.version_info[0] < 2:
        ## Not sure if it's even possible to get the port for the
        ## notebook app; so just using the default...
        notebooks = json.load(urllib2.urlopen('http://127.0.0.1:8888/notebooks'))
        for nb in notebooks:
            if nb['kernel_id'] == kernel_id:
                path = nb.get('name')
                break
    else:
        sessions = json.load(urllib2.urlopen('http://127.0.0.1:8888/api/sessions'))
        for sess in sessions:
            if sess['kernel']['id'] == kernel_id:
                path = sess.get('notebook').get('path')
                break
    return path

def get_current_notebook_name():
    import os
    path = get_current_notebook_path()
    return os.path.splitext(os.path.basename(path))[0]