import os
import platform
import distro
import time

def check(checker):
    if("Y" in checker or "y" in checker):
        return 1
    return 0

def find_pacman(dis):
    if("Ubuntu" in dis or "Debian" in dis):
        return "apt"
    elif("Fedora" in dis or "CentOS" in dis or "RedHat" in dis):
        return "dnf"

system=platform.uname()
if("Linux" in platform.platform()):
    dis=distro.name()
    pacman=find_pacman(dis)
    print(f"Architecture:{system.machine}")
    os.system("sudo %s update -y" % pacman)
    os.system("sudo %s upgrade -y" % pacman)
    os.system("clear")

    # Digital Design and Computer Organisation
    print("\n\nWe will start installing required software for DDCO\n\n")
    print("DDCO-wanna download iverilog?")
    vl=input("Enter Yes/No:")
    if(check(vl)):
        os.system("sudo %s install iverilog" % pacman)
        print("You will likely need gtkwave too")
        gtkwave=input("Enter Yes/no[Y/n]?:")
        if(check(gtkwave)):
            os.system("sudo %s install gtkwave" % pacman)
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
        os.system("cd")
        os.system("cd /usr/java")
        os.system("wget https://javadl.oracle.com/webapps/download/AutoDL?BundleId=247125_10e8cce67c7843478f41411b7003171c")
        os.system("tar xvf jre-8u351-linux-i586.tar.gz")
        os.system("cd ../..")
        os.system("wget https://www.jflap.org/jflaptmp/july27-18/JFLAP7.1.jar")
    os.system("clear")

    # Web Tech
    print("Now we will be downloading MongoDB:")
    mongo=input("Enter Yes/No[Y/n]?:")
    if(check(mongo)):
        os.system("wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -")
        os.system('echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntubionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list')
        os.system("sudo at update")
        os.system("sudo apt-get install mongodb-org -y")
        os.system("sudo systemctl enable mongod.service")
        os.system("sudo systemctl start mongod.service")

    print("Now we will be downloading node:")
    node=input("Enter Yes/No[Y/n]?:")
    if(check(node)):
        print("Do you want to download node")
        ch=input("Enter Yes/No[Y/n]?:")
        if(check(ch)):
            os.system("wget https://nodejs.org/dist/v18.12.1/node-v18.12.1.tar.gz")
            os.system("tar xvf node-v18.12.1.tar.gz")
            os.system("sudo cp -r ./{lib,share,include,bin} /usr")
        
        print("Do you want to download expressjs")
        ch=input("Enter Yes/No[Y/n]?:")
        if(check(ch)):
            os.system("npm install -g express")

        print("\n\nWanna download create-react-app(a tool that allows you to automatically build a basic react-app fro you)?:")
        react=input("Enter Yes/No[Y/n]?:")
        if(check(react)):
            os.system("npm install create-react-app")
        os.system("clear")


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
        os.system("start chrome https://www.jflap.org/jflaptmp/july27-18/JFLAP7.1.jar")
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