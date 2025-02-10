import pyshorteners
import re, sys, socket

def validate_url(url):
    newurl = url.lower()
    if "http" in newurl and "://" in url:
        return newurl
    else:
        return ""

def validate_domain(domain):
    pattern = re.compile(r'^[A-Za-z0-9.]+$')

    if pattern.match(domain):
        return True
    else:
        return False


def internet_connection():
    try:
        socket.gethostbyname("www.google.com")
        return True
    except socket.gaierror:
        return False


def home_logo():
    print("""
        ####   ##     ##      ###        #####      #######     #######
         ##    ##     ##     ## ##      ##   ##    ##     ##   ##     ##
         ##    ##     ##    ##   ##    ##     ##   ##     ##   ##     ##
         ##    #########   ##     ##   ##     ##    #######     ########
         ##    ##     ##   #########   ##     ##   ##     ##          ##
         ##    ##     ##   ##     ##    ##   ##    ##     ##   ##     ##
        ####   ##     ##   ##     ##     #####      #######     #######

IHA089: Navigating the Digital Realm with Code and Security - Where Programming Insights Meet Cyber Vigilance.
    """)

def about():
    print("""Welcome to IHA089, your premier source for cutting-edge cybersecurity solutions. At IHA089, we specialize in developing tools designed to enhance the security and integrity of your digital environment. 

We understand the importance of reliable and efficient cybersecurity solutions, which is why we focus on creating tools that are not only powerful but also user-friendly. Our tools are designed to streamline security processes, making it easier for organizations to protect their assets and maintain a secure operational framework.
    """)
    print("Website    :::   https://iha089.org.in")
    print("Github     :::   https://github.com/IHA089")
    print("Instagram  :::   https://www.instagram.com/IHA089")
    print("Telegram   :::   https://t.me/IHATron")
    print("youtube    :::   https://youtube.com/@iha089")
    print("Twiter     :::   https://twitter.com/iha089")


def validate_phishing_keyword(keyword):
    pattern = re.compile(r'^[a-zA-Z0-9-_]+$')

    if pattern.match(keyword):
        return True
    else:
        return False

def shorting_url(short_obj, url):
    try:
        short_url =  short_obj.short(url)
        return short_url
    except:
        print("An error occur when short url")
        return "error"

def shortener_service(url):
    print("1\ttinyurl\n2\tdagd\n3\tclckru")
    try:
        select = int(input("select : "))
        shortner = pyshorteners.Shortener()
        if select == 1:
            shorter = shortner.tinyurl
            return shorting_url(shorter, url)
        elif select == 2:
            shorter = shortner.dagd
            return shorting_url(shorter, url)
        elif select == 3:
            shorter = shortner.clckru
            return shorting_url(shorter, url)
        else:
            print("please select between 1-3")
            return "error"
    except ValueError:
        print("please select between 1-3")
        return "error"

def combiner(masked_url, domain_name, phishing_keyword):
    mskd = masked_url.split("://")
    url_header = mskd[0]
    url_tail = mskd[1]
    if phishing_keyword == "":
        result = url_header+"://"+domain_name+"@"+url_tail
    else:
        result = url_header+"://"+domain_name+"-"+phishing_keyword+"@"+url_tail

    return result

def urlmask():
    try:
        aa = sys.argv[1]
        if aa == "about":
            home_logo()
            about()
            return 0
    except:
        pass

    home_logo()

    try:
        original_url = input("Enter original url[Ex. https://google.com]:")
    except KeyboardInterrupt:
        print("\nExit by user")
        return 0
    if original_url == "":
        print("Please enter an url")
        return 0

    check_url_valid = validate_url(original_url)
    if check_url_valid == "":
        print("URL is not valid, please enter correct url[Ex:https://google.com]")
        return 0

    masked_url = shortener_service(original_url)
    if masked_url == "error":
        return 0

    try:
        domain_nam = input("Enter what domain you want to set[Ex. google.com, facebook.com]:")
    except KeyboardInterrupt:
        print("\nExit by user")
        return 0

    domain_name = domain_nam.lower()
    if domain_name == "":
        print("Please enter an domain name")
        return 0
    if not validate_domain(domain_name):
        print("please enter corrct domain name[Ex: google.com, facebook.com etc]")
        return 0

    try:
        phishing_key = input("Do you want to enter phising keyword[yes/no]:")
    except KeyboardInterrupt:
        print("\nExit by user")
        return 0

    if phishing_key == "yes" or phishing_key == "YES":
        try:
            phishing_keyword = input("Enter phishing keyworkd[Ex: free, login]:")
        except KeyboardInterrupt:
            print("\nExit by user")
            return 0
        phishing_keyword = phishing_keyword.lower()
        if not validate_phishing_keyword(phishing_keyword):
            print("please enter valid phishing keyword that include alphbats, number, '-' and '_'symbol")
            return 0
    else:
        phishing_keyword = ""
    
    result = combiner(masked_url, domain_name, phishing_keyword)
    print("Masked URL:::{}".format(result))
    
if __name__ == "__main__":
    urlmask()