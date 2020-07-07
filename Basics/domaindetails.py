import whois

def getDomainInfo():
    domain=input("Enter your domain name :")
    find=whois.whois(domain)
    print(find)

getDomainInfo()