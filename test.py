import os
import platform
import distro
import time

def check(checker):
    if("Y" in checker or "y" in checker):
        return 1
    return 0

system=platform.uname()
if("Linux" in platform.platform()):
    print(distro.name())
    print(f"Architecture:{system.machine}")
    os.system("sudo apt update -y")
    os.system("sudo apt upgrade -y")
    a=input("Enter C to clear:")
    if(a=="C" or a=='c'):
        os.system("clear")
    else:
        print("You like it dirty huh?")
    print("DDCO-wanna download iverilog?")
    vl=input("Enter Yes/No:")
    if(check(vl)):
        os.system("sudo apt install iverilog")
    print("SDS-wanna download all the required python libraries?")
    sds=input("Enter Yes/No:")
    if(check(sds)):
        os.system("pip3 install -r sds.txt")

    # Web Tech
    print("Now we will be downloading node:")
    node=input("Enter Yes/No[Y/n]?:")
    if(check(node)):
        print("Installing Node Version Manager")
        time.sleep(2)
        os.system("curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.26.1/install.sh | sudo -E bash")
        os.system("source ~/.nvm/nvm.sh")
        print("Do you want to download node")
        ch=input("Enter Yes/No[Y/n]?:")
        if(check(ch)):
            # os.system("nvm install v18.12.1")
            os.system("sudo apt-get install nodejs")
        # else:
        #     os.system("nvm ls-remote")
        #     version=input("Enter the version(v18.12.1) or something like that:")
        #     os.system("nvm install v%s" % version)
        print("\n\nWanna download create-react-app(a tool that allows you to automatically build a basic react-app fro you)?:")
        react=input("Enter Yes/No[Y/n]?:")
        if(check(react)):
            os.system("npm install create-react-app")


elif("Windows" in platform.platform()):
    print(f"Architecture:{system.machine}")
    os.system("start chrome https://bleyer.org/icarus/iverilog-10.0-x86_setup.exe")
    print("Would you like to download NodeJS?")
    node=input("Enter Yes/No[Y/n]?:")
    if(check(node)):
        os.system("winget install -e --id OpenJS.NodeJS")
    print("Would you like to download MongoDB?")
    mongo=input("Enter Yes/No[Y/n]?:")
    if(check(mongo)):
        print("We will be downloading MongoDB Server now")
        mongoserver=input("Enter Yes/No[Y/n]?:")
        if(check(mongoserver)):
            os.system("winget install -e --id MongoDB.Server")
        print("Would you like to download MongoDB Compass(A GUI representation of NoSQL data)?")
        mongocomp=input("Enter Yes/No[Y/n]?")
        if(check(mongocomp)):
            os.system("winget install -e --id MongoDB.Compass.Community")
        print("You will most likely need a Mongo Shell to run CRUD operations")
        print("Would you like to download Mongo Shell?")
        mongosh=input("Enter Yes/No[Y/n]?:")
        os.system("winget install -e --id MongoDB.Shell")
    print("Would you like to download create-react-app(a tool to automatically build a basic react-app for you)?:")
    react=input("Enter Yes/No[Y/n]?:")
    if(check(react)):
        os.system("npm install create-react-app")
        print("Would you like to create a react app?")
        createapp=input("Enter Yes/No[Y/n]?:")
        if(check(createapp)):
            appname=input("Enter the name of the project:")
            os.system("npx create-react-app %s" % appname)
    
            