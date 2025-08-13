import random
import string
all_short_urls = {}

def get_shorturl(Longurl,myshorturl = None):

    """given a long url it returns the short url """
    # to coustomize our shorturl
    if myshorturl :
        if myshorturl in all_short_urls :
            return ("Short url already exist")
        else:
            all_short_urls[myshorturl] = Longurl
            result = ("myurlshortener//" + myshorturl)


    # here len is the length of our short url 
    len = random.randint(3,7)
    # it is a variable that store our shorturl
    shorturl = ""
    # chars we get all letter using strin
    chars = string.ascii_letters
    for i in range(len):
        shorturl+=random.choice(chars) # enables us to get a char of our choice
    if shorturl in all_short_urls:
        return get_shorturl(Longurl)
    else:
        all_short_urls[shorturl]= Longurl
    end_result= "myurlshortener//"+ shorturl
    return end_result
def get_longurl(Shorturl):
    """given a sort url it returns us a long url"""
    # for eg: if our short url is https/www/fm/in/Kegbs in order to get last part we split and collect it
    key = Shorturl.split("/")[-1]
    if key in all_short_urls:
        return all_short_urls[key]
    else :
        return ("your short doesn't exist")
def update_longurl(shorturl , newlongurl):
    if shorturl in all_short_urls:
        shorturl = shorturl.split[-1]
        all_short_urls[shorturl] = newlongurl
        result = "myurlshortener//"+shorturl
        return result
    else :
        return("short url doesn't exist")

