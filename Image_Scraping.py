import bs4, requests, os
url = "https://xkcd.com/"
while not url.endswith('#'):
    res = requests.get(url)
    beau = bs4.BeautifulSoup(res.text, features="lxml")
    comicEle = beau.select('#comic img')
    #print(comicEle)
    if comicEle == []:
        print("Comic element not found!")
    else:
        comicUrl = "http:" + comicEle[0].get('src')
        print("Downloading image %s" %(comicUrl))
        res = requests.get(comicUrl)
        image = open(os.path.join('xkcd', os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(10000000):
            image.write(chunk)
        image.close()
    prevlink = beau.select('a[rel="prev"]')[0]
    url = "https://xkcd.com/" + prevlink.get('href')