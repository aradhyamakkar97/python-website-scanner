import os

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_file(path,data):  # data is results of "scan" and path is where to write the file
    f=open(path,'w')
    f.write(data)
    f.close()
