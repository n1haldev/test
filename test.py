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

    # Digital Design and Computer Organisation
    print("\n\nWe will start installing required software for DDCO\n\n")
    print("DDCO-wanna download iverilog?")
    vl=input("Enter Yes/No:")
    if(check(vl)):
        os.system("sudo apt install iverilog")
        print("You will likely need gtkwave too")
        gtkwave=input("Enter Yes/no[Y/n]?:")
        if(check(gtkwave)):
            os.system("sudo apt install gtkwave")
    os.system("clear")

    # Statistics for Data Science
    print("SDS-wanna download all the required python libraries?")
    sds=input("Enter Yes/No:")
    if(check(sds)):
        print("Installing Jupyter Notebook and other required python packages from pip:\n\n")
        if(check(sds)):
            os.system("pip3 install -r sds.txt")
        print("Do you want to install machine learning tools:")
        ml=input("Enter Yes/No[Y/n]?:")
        if(check(ml)):
            os.system("pip3 install -r ml.txt")
        os.system("clear")

    # Automata Formal Languages and Logic
    print("Let us download all required software for AFLL")
    afll=input("Enter Yes/No[Y/n]?:")
    if(check(afll)):
        os.system("java --version")
        os.system("firefox https://www.jflap.org/jflaptmp/july27-18/JFLAP7.1.jar"|"chrome https://www.jflap.org/jflaptmp/july27-18/JFLAP7.1.jar"|"brave-browser https://www.jflap.org/jflaptmp/july27-18/JFLAP7.1.jar")

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
            os.system("nvm install v18.12.1")
            os.system("sudo apt-get install nodejs")
        # else:
            os.system("nvm ls-remote")
            version=input("Enter the version(v18.12.1) or something like that:")
            os.system("nvm install v%s" % version)
        print("\n\nWanna download create-react-app(a tool that allows you to automatically build a basic react-app fro you)?:")
        react=input("Enter Yes/No[Y/n]?:")
        if(check(react)):
            os.system("npm install create-react-app")


elif("Windows" in platform.platform()):
    print(f"Architecture:{system.machine}")

    # Digital Design and Computer Organisation
    print("We will download iverilog and gtkwave")
    ddco=input("Enter Yes/No[Y/n]?")
    if(check(ddco)):
        os.system("start chrome https://bleyer.org/icarus/iverilog-0.9.7_setup.exe"|"start brave https://bleyer.org/icarus/iverilog-0.9.7_setup.exe"|"start firefox https://bleyer.org/icarus/iverilog-0.9.7_setup.exe")
    os.system("cls")

    # Statistics for Data Science
    print("SDS-wanna download all the required python libraries?")
    sds=input("Enter Yes/No:")
    if(check(sds)):
        print("Installing Jupyter Notebook and other required python packages from pip:\n\n")
        if(check(sds)):
            os.system("pip3 install -r sds.txt")
        print("Do you want to install machine learning tools:")
        ml=input("Enter Yes/No[Y/n]?:")
        if(check(ml)):
            os.system("pip3 install -r ml.txt")
        os.system("cls")

    # Automata Formal Languages and Logic
    print("We will download JFLAP")
    afll=input("Enter Yes/No[Y/n]?:")
    if(check(afll)):
        os.system("java --version")
        os.system("start chrome https://www.jflap.org/jflaptmp/july27-18/JFLAP7.1.jar"|"start firefox https://www.jflap.org/jflaptmp/july27-18/JFLAP7.1.jar"|"start brave https://www.jflap.org/jflaptmp/july27-18/JFLAP7.1.jar")
        os.system("cls")

    # Web Tech
    print("We will download required software for Web Tech:")
    wt=input("Enter Yes/No[Y/n]?:")
    if(check(wt)):
        print("Would you like to download NodeJS?")
        node=input("Enter Yes/No[Y/n]?:")
        # Node JS
        if(check(node)):
            os.system("winget install -e --id OpenJS.NodeJS")
        # MongoDB
        print("Would you like to download MongoDB?")
        mongo=input("Enter Yes/No[Y/n]?:")
        if(check(mongo)):
            print("We will be downloading MongoDB Server now")
            mongoserver=input("Enter Yes/No[Y/n]?:")
            # Server
            if(check(mongoserver)):
                os.system("winget install -e --id MongoDB.Server")
            # Compass
            print("Would you like to download MongoDB Compass(A GUI representation of NoSQL data)?")
            mongocomp=input("Enter Yes/No[Y/n]?")
            if(check(mongocomp)):
                os.system("winget install -e --id MongoDB.Compass.Community")
            # Shell
            print("You will most likely need a Mongo Shell to run CRUD operations")
            print("Would you like to download Mongo Shell?")
            mongosh=input("Enter Yes/No[Y/n]?:")
            os.system("winget install -e --id MongoDB.Shell")
        # create-react-app
        print("Would you like to download create-react-app(a tool to automatically build a basic react-app for you)?:")
        react=input("Enter Yes/No[Y/n]?:")
        if(check(react)):
            os.system("npm install create-react-app")
            print("Would you like to create a react app?")
            createapp=input("Enter Yes/No[Y/n]?:")
            if(check(createapp)):
                appname=input("Enter the name of the project:")
                os.system("npx create-react-app %s" % appname)