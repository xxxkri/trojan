import os

dirname="."
has_args=0
def run(**args):
    print "[*] In dirlister module."
    global has_args
    global dirname
    for a in args:
        has_args=1
        if args[a] is not None:
            dirname=args[a]
        files = os.listdir(dirname)
        return str(files)
    
    if has_args == 0:
        return str(os.listdir(dirname))

# run like this:
#print run(**{'dirname': "/tmp"})
#print run()
