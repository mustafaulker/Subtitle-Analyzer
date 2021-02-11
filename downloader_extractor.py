import time
import zipfile

import requests
from bs4 import BeautifulSoup


# Download subtitles for the movies in the input list.
def sub_download(subs_to_download):
    try:
        # Go to subtitle site and search for movies in the input list.
        # Find get all anchors from this link.
        resp = requests.get("http://subscene.com/subtitles/release?q=" + subs_to_download)
        bsoup4 = BeautifulSoup(resp.content, "html.parser")
        anchors = bsoup4.find_all("a")
        href = ""

        # Find spans for every anchor, filter specific spans.
        for i in range(0, len(anchors)):
            a_spans = anchors[i].find_all("span")
            if len(a_spans) == 2 and a_spans[0].get_text().strip() == "English":
                href = anchors[i].get("href").strip()

        # Go to found subtitle & get download button's link & get content
        if len(href) > 0:
            print("Downloading & Extracting: ", subs_to_download)
            resp = requests.get("http://subscene.com" + href)
            bsoup4 = BeautifulSoup(resp.content, "html.parser")
            lin = bsoup4.find_all('a', attrs={'id': 'downloadButton'})[0].get("href")
            resp = requests.get("http://subscene.com" + lin)

            # Writing content to a temporary zip file
            temp_zip = open(f'./subs/temp.zip', 'wb')
            for chunk in resp.iter_content(chunk_size=100000):
                temp_zip.write(chunk)
                temp_zip.close()
            time.sleep(1)

            # Unzip the temp file to subs folder
            with zipfile.ZipFile('./subs/temp.zip') as temp_zip:
                [temp_zip.extract(files_in_zip, './subs/')
                 for files_in_zip in temp_zip.namelist() if files_in_zip.endswith(".srt")]
    except:
        print("An error occurred while downloading subtitles.")
