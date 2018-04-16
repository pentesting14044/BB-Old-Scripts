import argparse, os, requests, time, csv, datetime, glob
from signal import signal, alarm, SIGALRM

today = datetime.date.today()

__author__ = 'Caleb Kinney'

global url, secure


def get_args():
    parser = argparse.ArgumentParser(
        description='PyBrute')
    parser.add_argument(
        '-d', '--domain', type=str, help='Domain', required=False, default=False)
    parser.add_argument(
        '-s', '--secure', help='Secure', nargs='?', required=False, default=False)
    parser.add_argument(
        '-b', '--bruteforce', help='Bruceforce', nargs='?', default=False)
    parser.add_argument(
        '--upgrade', help='Upgrade', nargs='?', default=False)
    parser.add_argument(
        '--install', help='Install', nargs='?', default=False)
    parser.add_argument(
        '--vpn', help='VPN Check', nargs='?', default=False)
    parser.add_argument(
        '-p', '--ports', help='Ports', nargs='?', default=False)
    parser.add_argument(
        '-q', '--quick', help='Quick', nargs='?', default=False)
    parser.add_argument(
        '--bruteall', help='Bruteforce JHaddix All', nargs='?', default=False)

    return parser.parse_args()


newpath = r'Output/PyBrute'
if not os.path.exists(newpath):
    os.makedirs(newpath)


def banner():
    print("\033[1;31m__________        __________                __     ")
    print("\033[1;31m\______   \___.__.\______   \_______ __ ___/  |_  ____")
    print("\033[1;31m |     ___<   |  | |    |  _/\_  __ \  |  \   __\/ __ \ ")
    print("\033[1;31m |    |    \___  | |    |   \ |  | \/  |  /|  | \  ___/")
    print("\033[1;31m |____|    / ____| |______  / |__|  |____/ |__|  \___  >")
    print("\033[1;31m           \/             \/                         \/ ")
    print("\033[1;34m                             OrOneEqualsOne.com\033[1;m")
    globpath = ("*.csv")
    globpath2 = ("*.lst")
    if (next(glob.iglob(globpath), None)) or (next(glob.iglob(globpath2), None)):
        print("\nThe following files may be left over from failed PyBrute attempts:")
        for file in glob.glob(globpath):
            print("  - " + file)
        for file in glob.glob(globpath2):
            print("  - " + file)
        signal(SIGALRM, lambda x: 1 / 0)
        try:
            alarm(25)
            RemoveQ = raw_input("\nWould you like to remove the files? [y/n]: ")
            if RemoveQ.lower() == "y":
                os.system("rm *.csv")
                os.system("rm *.lst")
                print("Files removed\nStarting PyBrute...")
            else:
                print("Files not removed\nStarting PyBrute...")
        except:
            print("Error or No User Input\nFiles not removed\nStarting PyBrute...")
        time.sleep(2)


def sublist3r():
    if vpn is not False:
        vpncheck()
    sublist3rFileName = ("Output/PyBrute/" + domain + "_sublist3r.txt")
    Subcmd = (("python bin/Sublist3r/sublist3r.py -v -t 15 -d %s -o " + sublist3rFileName) % (domain))
    print("\n\033[1;31mRunning Command: \033[1;37m" + Subcmd)
    os.system(Subcmd)
    print("\n\033[1;31mSublis3r Complete\033[1;37m")
    time.sleep(1)


def sublist3rBrute():
    if vpn is not False:
        vpncheck()
    sublist3rFileName = ("Output/PyBrute/" + domain + "_sublist3r.txt")
    Subcmd = (("python bin/Sublist3r/sublist3r.py -v -b -t 15 -d %s -o " + sublist3rFileName) % (domain))
    print("\n\033[1;31mRunning Command: \033[1;37m" + Subcmd)
    os.system(Subcmd)
    print("\n\033[1;31mSublis3r Complete\033[1;37m")
    time.sleep(1)
    eyewitness(sublist3rFileName)


def enumall():
    if vpn is not False:
        vpncheck()
    enumallCMD = "python bin/domain/enumall.py %s" % (domain)
    print("\n\033[1;31mRunning Command: \033[1;37m" + enumallCMD)
    os.system(enumallCMD)
    print("\n\033[1;31menumall Complete\033[1;37m")
    time.sleep(1)


def massdns():
    if vpn is not False:
        vpncheck()
    if bruteall is not False:
        massdnsCMD = (
            "./bin/subbrute/subbrute.py -s ./bin/sublst/all.txt " + domain + " | ./bin/massdns/bin/massdns -r resolvers.txt -t A -a -o -w ./Output/PyBrute/" + domain + "-massdns.txt -")
        print("\n\033[1;31mRunning Command: \033[1;37m" + massdnsCMD)
        os.system(massdnsCMD)
        print("\n\033[1;31mMasscan Complete\033[1;37m")
    else:
        massdnsCMD = (
            "./bin/subbrute/subbrute.py -s ./bin/sublst/sl-domains.txt " + domain + " | ./bin/massdns/bin/massdns -r resolvers.txt -t A -a -o -w ./Output/PyBrute/" + domain + "-massdns.txt -")
        print("\n\033[1;31mRunning Command: \033[1;37m" + massdnsCMD)
        os.system(massdnsCMD)
        print("\n\033[1;31mMasscan Complete\033[1;37m")
    time.sleep(1)


def knockpy():
    rootdomainStrip = domain.replace(".", "_")
    os.system("rm " + rootdomainStrip + "*")
    if vpn is not False:
        vpncheck()
    knockpyCmd = ("python bin/knockpy/knockpy/knockpy.py -c " + domain)
    print("\n\033[1;31mRunning Command: \033[1;37m" + knockpyCmd)
    os.system(knockpyCmd)
    try:
        filenameKnock = (rootdomainStrip + "*")
        knockpyFilenameInit = ("Output/PyBrute/" + domain + "_knock.csv")
        time.sleep(1)
        knockpySubs = []
        with open(knockpyFilenameInit, 'rb') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                knockpySubs.append(row[3])
        filenameKnocktxt = (knockpyFilenameInit + ".txt")
        f1 = open(filenameKnocktxt, "w")
        for hosts in knockpySubs:
            hosts = "".join(hosts)
            f1.writelines("\n" + hosts)
        f1.close()
        time.sleep(1)
    except:
        pass
    try:
        os.system("rm " + knockpyFilenameInit)
        os.system("rm " + filenameKnock + ".csv")
    except:
        pass


def eyewitness(filename):
    rootdomain = domain
    EWHTTPScriptIPS = (
        "python bin/EyeWitness/EyeWitness.py -f " + filename + " --active-scan --no-prompt --headless  -d " + "Output/PyBrute/" + rootdomain + "-" + time.strftime(
            '%m-%d-%y-%H-%M') + "-Sublist3r-EW ")
    if vpn is not False:
        print(
            "\n\033[1;31mIf not connected to VPN manually run the following command on reconnect:\n\033[1;37m" + EWHTTPScriptIPS)
        vpncheck()
        print("\n\033[1;31mRunning Command: \033[1;37m" + EWHTTPScriptIPS)
        os.system(EWHTTPScriptIPS)
    print("\a")


def upgradeFiles():
    binpath = r'bin'
    if not os.path.exists(binpath):
        os.makedirs(binpath)
    else:
        os.system("rm -r bin")
        os.makedirs(binpath)
    sublist3rUpgrade = ("git clone https://github.com/aboul3la/Sublist3r.git ./bin/Sublist3r")
    print("\n\033[1;31mRunning Command: \033[1;37m" + sublist3rUpgrade)
    os.system(sublist3rUpgrade)
    subInstallReq = ("sudo pip install -r bin/Sublist3r/requirements.txt")
    print("\n\033[1;31mRunning Command: \033[1;37m" + subInstallReq)
    os.system(subInstallReq)
    print("Sublis3r Installed")
    eyeWitnessUpgrade = ("git clone https://github.com/ChrisTruncer/EyeWitness.git ./bin/EyeWitness")
    print("\n\033[1;31mRunning Command: \033[1;37m" + eyeWitnessUpgrade)
    os.system(eyeWitnessUpgrade)
    eyeInstallReq = ("sudo bash bin/EyeWitness/setup/setup.sh")
    print("\n\033[1;31mRunning Command: \033[1;37m" + eyeInstallReq)
    os.system(eyeInstallReq)
    cpphantomjs = ("cp phantomjs bin/EyeWitness/bin/")
    print("\n\033[1;31mRunning Command: \033[1;37m" + cpphantomjs)
    os.system(cpphantomjs)
    movephantomjs = ("mv phantomjs bin/")
    print("\n\033[1;31mRunning Command: \033[1;37m" + movephantomjs)
    os.system(movephantomjs)
    print("EyeWitness Installed")
    enumallUpgrade = ("git clone https://github.com/jhaddix/domain.git ./bin/domain")
    print("\n\033[1;31mRunning Command: \033[1;37m" + enumallUpgrade)
    print("enumall Installed")
    os.system(enumallUpgrade)
    knockpyUpgrade = ("git clone https://github.com/guelfoweb/knock.git ./bin/knockpy")
    print("\n\033[1;31mRunning Command: \033[1;37m" + knockpyUpgrade)
    os.system(knockpyUpgrade)
    print("Knockpy Installed")
    sublstUpgrade = ("git clone https://gist.github.com/jhaddix/86a06c5dc309d08580a018c66354a056 ./bin/sublst")
    print("\n\033[1;31mRunning Command: \033[1;37m" + sublstUpgrade)
    print("JHaddix All Domain List Installed")
    os.system(sublstUpgrade)
    SLsublstUpgrade = (
        "wget -O ./bin/sublst/sl-domains.txt https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/sorted_knock_dnsrecon_fierce_recon-ng.txt")
    print("\n\033[1;31mRunning Command: \033[1;37m" + sublstUpgrade)
    print("SecList Domain List Installed")
    os.system(SLsublstUpgrade)
    subbruteUpgrade = ("git clone https://github.com/TheRook/subbrute.git ./bin/subbrute")
    print("\n\033[1;31mRunning Command: \033[1;37m" + subbruteUpgrade)
    os.system(subbruteUpgrade)
    print("Subbrute Installed")
    massdnsUpgrade = ("git clone https://github.com/blechschmidt/massdns ./bin/massdns")
    print("\n\033[1;31mRunning Command: \033[1;37m" + massdnsUpgrade)
    os.system(massdnsUpgrade)
    massdnsMake = ("make -C ./bin/massdns")
    os.system("apt-get install libldns-dev -y")
    os.system(massdnsMake)
    print("Massdns Installed")
    os.system("cp ./bin/subbrute/resolvers.txt ./")


def subdomainfile():
    sublist3rFileName = ("Output/PyBrute/" + domain + "_sublist3r.txt")
    enumallFileName = (domain + ".lst")
    subdomainAllFile = ("Output/PyBrute/" + domain + "-all.txt")
    knockpyFileName = ("Output/PyBrute/" + domain + "_knock.csv.txt")
    massdnsFileName = ("Output/PyBrute/" + domain + "-massdns.txt")
    try:
        with open(sublist3rFileName) as f:
            SubHosts = f.read().splitlines()
        f.close()
        time.sleep(2)
        f1 = open(subdomainAllFile, "w")
        for hosts in SubHosts:
            hosts = "".join(hosts)
            f1.writelines("\n" + hosts)
        f1.close()
    except:
        pass
    try:
        with open(enumallFileName) as f:
            SubHosts = f.read().splitlines()
        f.close()
        time.sleep(2)
        f1 = open(subdomainAllFile, "a")
        for hosts in SubHosts:
            hosts = "".join(hosts)
            f1.writelines("\n" + hosts)
        f1.close()
    except:
        pass
    try:
        with open(knockpyFileName) as f:
            SubHosts = f.read().splitlines()
        f.close()
        time.sleep(2)
        f1 = open(subdomainAllFile, "a")
        for hosts in SubHosts:
            hosts = "".join(hosts)
            f1.writelines("\n" + hosts)
        f1.close()
    except:
        pass
    try:
        with open(massdnsFileName) as f:
            SubHosts = f.read().splitlines()
        f.close()
        time.sleep(2)
        f1 = open(subdomainAllFile, "a")
        for hosts in SubHosts:
            hosts = hosts.split(".	")[0]
            if domain in hosts:
                hosts = "".join(hosts)
                f1.writelines("\n" + hosts)
        f1.close()
    except:
        pass
    domainList = open(subdomainAllFile, 'r')
    uniqueDomains = set(domainList)
    domainList.close()
    subdomainUniqueFile = ("Output/PyBrute/" + domain + "-unique.txt")
    uniqueDomainsOut = open(subdomainUniqueFile, 'w')
    for domains in uniqueDomains:
        domains = domains.replace('\n', '')
        if domains.endswith(domain):
            uniqueDomainsOut.writelines("https://%s" % domains + "\n")
            if ports is not False:
                uniqueDomainsOut.writelines("https://%s" % domains + ":8443" + "\n")
            if secure is False:
                uniqueDomainsOut.writelines("http://%s" % domains + "\n")
                if ports is not False:
                    uniqueDomainsOut.writelines("http://%s" % domains + ":8080" + "\n")
    uniqueDomainsOut.close()
    time.sleep(5)
    enumallFileNamecsv = (domain + ".csv")
    try:
        os.remove(sublist3rFileName)
        os.remove(enumallFileName)
        os.remove(enumallFileNamecsv)
        os.remove(knockpyFileName)
        os.remove(massdnsFileName)
    except:
        pass
    eyewitness(subdomainUniqueFile)


def vpncheck():
    vpnck = requests.get('http://ipinfo.io')
    # Change "Comcast" to your provider or City")
    if "Comcast" in vpnck.content:
        print("\n\033[1;31mNot connected via VPN \033[1;37m")
        print("\n" + vpnck.content)
        quit()
    else:
        print("\n\033[1;31mConnected via VPN \033[1;37m")
        print("\n" + vpnck.content)
        time.sleep(5)


if __name__ == "__main__":
    banner()
    args = get_args()
    domain = args.domain
    secure = args.secure
    bruteforce = args.bruteforce
    upgrade = args.upgrade
    install = args.install
    ports = args.ports
    vpn = args.vpn
    quick = args.quick
    bruteall = args.bruteall
    if install is not False:
        upgradeFiles()
    elif upgrade is not False:
        upgradeFiles()
    else:
        if domain is not False:
            if quick is not False:
                sublist3rBrute()
            elif bruteforce is not False:
                massdns()
                sublist3r()
                enumall()
                subdomainfile()
            else:
                sublist3r()
                enumall()
                knockpy()
                subdomainfile()
        else:
            print("Please provide a domain. Ex. -d example.com")
    print("PyBute Out")
