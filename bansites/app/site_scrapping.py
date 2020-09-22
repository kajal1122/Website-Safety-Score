from bs4 import BeautifulSoup
import urllib.request , urllib.parse, urllib.error
bad_words = {"sex":3,
"fuck":3,
"intensifier":3,
"kill":3,
"murder":3,

"bastard":3,
"illegitimate":3,
"penis":3,
"ass":3,
"butt":3,
"vagina":3,
"cunt":3,
"testicles":3,
"dumbass":3,
"fucker":3,
"witch":2,
"dickhead":3,
"hell":3,
"whore":3,
"bullshit":2,
"bitch":3,
"cock":2,
"prick":2,
"balls":3,
"dick":3,
"tits":3,
"asshole":3,
"cocksucker":3,
"shithead":3,
"slut":3,
"die":3,
"porn":3,
"erotic":3,
"drugs":3,
}


def site_scrapping(url):
    html = urllib.request.urlopen(url,timeout=5).read()
    soup = BeautifulSoup(html, "html.parser")
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())

    li=[]
    for line in lines:
        p = line.split(" ")
        for words in p:
            if words != "":
                li.append(words)
    bad_words_in_site = {}
    for i in li:
        if(i.lower() in bad_words):
            bad_words_in_site[i.lower()] += 1
    result = 0
    if len(bad_words_in_site) == 0:
        result=0
    else:
        result=90

    return result
