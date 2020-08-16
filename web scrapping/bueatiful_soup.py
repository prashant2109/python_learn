from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml') 
for article in soup.find_all('article'):
    headline = article.h2.a.text

    ## grab summary information
    summary = article.find('div', class_='entry-content')
    summary = summary.p.text

    ## grap video source
    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
    except:continue
    vid_id = vid_src.split('/')[4]
    vid_id = vid_id.split('?')[0]

    yt_link = f'https://youtube.com/watch?v={vid_id}'
    print (yt_link)

