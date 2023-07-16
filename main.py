import requests
from bs4 import BeautifulSoup, NavigableString, TemplateString
import json
def go(bs_label: BeautifulSoup) -> str:
    return bs_label.get_text(types=(NavigableString, TemplateString)).strip()

header = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

mew = requests.get("https://zh.moegirl.org.cn/MARETU", headers=header)
soup = BeautifulSoup(mew.text, 'html.parser')

div = soup.find("div", attrs=
    {"style": "position:relative; max-width:auto; max-height:300px; overflow:auto; margin-bottom:3px; padding-left:0.5em; border:solid medium lightblue; -moz-border-radius-topleft:0.5em; -webkit-border-top-left-radius:0.5em; border-top-left-radius:0.5em;"}
)

song_dict = {}
for x in div.find_all('table', attrs={"style": "width:100%; vertical-align:top;"}):
    song_name = go(x.find_previous())
    song_info_soup = x.tbody.tr.find("td", attrs={"style": "vertical-align:top;"}).table.tbody
    trs = song_info_soup.find_all("tr")
    date = go(trs[0].find_all("td")[1])
    vocal = go(trs[0].find_all("td")[3])
    composer = go(trs[1].find_all("td")[1])
    lyric = go(trs[2].find_all("td")[1])
    video = go(trs[3].find_all("td")[1])
    link = trs[4].td.a["href"].strip()
    song_dict[song_name] = {
        "date": date,
        "vocal": vocal,
        "composer": composer,
        "lyric": lyric,
        "video": video,
        "link": link,
    }

with open("maretu.json", 'w') as f:
    f.write(json.dumps(song_dict,indent=4,ensure_ascii=False))
