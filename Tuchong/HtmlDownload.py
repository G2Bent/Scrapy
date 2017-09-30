import urllib

class HtmlDownloader():
    def download(self,url):
        if url is None:
            return None

        responese = urllib.request.urlopen(url,timeout = 10)

        if responese.getcode() != 200:
            return None
        return responese.read()
		
		
		