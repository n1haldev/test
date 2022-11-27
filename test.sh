echo "Enter the name of your package manager:"
read pacman

echo "We will need tar to unpack and donwload system binaries"
sudo $pacman tar

echo "We will be downloading following software related to the subject DDCO(Digital Design and Computer Organisation):"
echo "1. Iverilog"
echo "2. Gtkwave"

echo "We are installing iverilog and gtkwave"
sudo $pacman install iverilog gtkwave

clear

echo "We are installing the following software for AFLL (Automata Formal Languages and Logic):"
echo "1. JFLAP"
echo "2. ply"

cd /usr/java
wget https://javadl.oracle.com/webapps/download/AutoDL?BundleId=247125_10e8cce67c7843478f41411b7003171c
tar xvf jre-8u351-linux-i586.tar.gz
cd ../..
wget https://www.jflap.org/jflaptmp/july27-18/JFLAP7.1.jar
pip3 install ply

clear

echo "We will be installing the following software for WT (Web Technologies):"
echo "1. NodeJS v18.12.1"
echo "2. MongoDB Server"
echo "3. Mongo Shell"
echo "4. MongoDB Compass"

echo "Installing NodeJS"
wget https://nodejs.org/dist/v18.12.1/node-v18.12.1.tar.gz
tar xvf node-v18.12.1.tar.gz
sudo cp -r ./{lib,share,include,bin} /usr

echo "Installing MongoDB Server"
echo "Warning:Installation on Ubuntu 22.04 LTS is bound to fail as MongoDB doesn't support this latest version"
echo "Enter the distro you are using to download MongoDB Server in all lower case"
read distro

case "$distro" in
    "ubuntu") echo "Installing MongoDB on Ubuntu"
    sudo apt-get install libcurl4 openssl liblzma5
    tar -zxvf mongodb-linux-*-6.0.3.tgz
    sudo cp mongodb-linux-*-6.0.3.tgz/bin/* /usr/local/bin/
    