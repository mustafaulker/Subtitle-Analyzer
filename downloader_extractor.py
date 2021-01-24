import time
import zipfile

import requests
from bs4 import BeautifulSoup


def sub_download(subs_to_download):
    try:
        resp = requests.get("http://subscene.com/subtitles/release?q=" + subs_to_download)
        bsoup4 = BeautifulSoup(resp.content, "html.parser")
        a_tags = bsoup4.find_all("a")
        href = ""
        for i in range(0, len(a_tags)):
            a_spans = a_tags[i].find_all("span")
            print(a_spans)
            if len(a_spans) == 2 and a_spans[0].get_text().strip() == "English":
                href = a_tags[i].get("href").strip()
        if len(href) > 0:
            print("Downloading & Extracting: ", subs_to_download)
            resp = requests.get("http://subscene.com" + href)
            bsoup4 = BeautifulSoup(resp.content, "html.parser")
            lin = bsoup4.find_all('a', attrs={'id': 'downloadButton'})[0].get("href")
            resp = requests.get("http://subscene.com" + lin)
            temp_zip = open(f'./subs/temp.zip', 'wb')
            for chunk in resp.iter_content(chunk_size=100000):
                temp_zip.write(chunk)
                temp_zip.close()
            time.sleep(1)
            with zipfile.ZipFile('./subs/temp.zip') as zip_ext:
                [zip_ext.extract(filex, './subs/') for filex in zip_ext.namelist() if filex.endswith(".srt")]
    except:
        pass
