import os

def run(**args):
    print "[*] In environment module."
    return str(os.environ)

# run like this
#print run()
