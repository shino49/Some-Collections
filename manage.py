import os
import sys,getopt
curdir = os.getcwd()
#print(curdir)
def argGain(argv):
    #appname = ''
    try:
        opts,args = getopt.getopt(argv[1:],"hi:n:")
    except getopt.GetoptError:
        print ('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt,arg in opts:
        if opt == '-h':
            print('manage.py -n yourappname')
        elif opt =='-n':
            appname = arg
            print("waiting initing...")
            return appname
        else:
            raise Exception
         
appname = argGain(sys.argv)
if appname not in os.listdir(curdir):
    os.mkdir(appname)
    appdir = os.path.join(curdir,appname)
    with open(appdir+"\\views.py",'w') as f1:
        f1.write(f"from {appname} import app\n@app.route('/')\ndef index():\n\treturn 'Hello World'")
    with open(appdir+"\\__init__.py",'w') as f2:
        f2.write(f"from flask import Flask\napp=Flask(__name__)\napp.config.from_object('config')\n\nfrom {appname} import views,models")
    with open(appdir+"\\models.py",'w') as f3:
        f3.write("#This is the models")
    os.mkdir(appdir+"\\templates")
    f4 = open(appdir+"\\templates\\index.html","w")
    f4.close()
    os.mkdir(appdir+"\\static")
    os.mkdir(appdir+"\\static\\css")
    os.mkdir(appdir+"\\static\\javascript")
    os.mkdir(appdir+"\\static\\img")
    os.mkdir(appdir+"\\static\\audio")



