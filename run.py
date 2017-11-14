#!/usr/bin/env python
import time
import json
import sys, os

def help():
    print "Input the config file name (absolute path)"
    print "For example: ./run.py /home/andy/run.py"
    print "If not argument, then it load current path config file which named config.json"

if __name__ == "__main__":
    print('hello world:begin')
    argc = len(sys.argv)
    configfile = 'config.json'
    if argc < 2:
        print("using the default config file: config.json")
        if os.path.isfile(configfile) == False:
            sys.exit("default file config.json not exist, program exit")
    else:
        configfile = sys.argv[1]
        print('using config file:', configfile)

    #os.system('./test.sh')
    #time.sleep(5)
    with open(configfile) as json_data:
        data = json.load(json_data)
        path = data["executablePath"]
        executive = data["executableName"]
        if os.path.exists(path) == False:
            sys.exit("executablePath in config file not exist")
        else:
            print "executablePath is:", path
        print os.getcwd()
        os.chdir(path)
        print os.getcwd()
        if os.path.isfile(executive) == False:
            sys.exit("executableName in config file not exist")
        else:
            print "executableName is:", executive
        command = "gnome-terminal -e 'bash -c \"" + executive + " ; exec bash\"'"
        print "the command is:", command
        os.system(command)
        #The format for open a terminal and make terminal not shut down
        #os.system("gnome-terminal -e 'bash -c \"sudo add-apt-repository ppa:x2go/ppa && sudo apt-get update ; exec bash\"'")
    print('hello world:end')
