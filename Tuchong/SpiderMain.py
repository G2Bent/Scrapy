from Tuchong import HtmlDownload,HtmlParser,HtmlOutput,UrlManage

class SpiderMain(object):
    def __init__(self):
        self.urls = UrlManage.UrlManager()
        self.downloader = HtmlDownload.HtmlDownloader()
        self.parser = HtmlParser.HtmlParser()
        self.output = HtmlOutput.HtmlOutputer()

    def craw(self,root_url,user_nick):
        html_cont = self.downloader.download(root_url)
        new_urls = self.parser.parse_albums_urls(root_url,user_nick,html_cont)

        count = 1
        for link in new_urls:
            self.urls.add_new_url(link)
            while self.urls.has_new_url():
                try:
                    new_url = self.urls.get_new_url()
                    html_cont = self.downloader.download(new_url)
                    print("craw %d : %s "%(count,new_url))
                    new_data = self.parser.pars_image(new_url,html_cont)
                    self.output.collect_data(new_data)

                    count += 1
                except :
                    print("craw fail")

            self.output.output_html(user_nick)

if __name__=="__main__":
    print("开始")
    user_nick = "G"
    root_url = "https://gyeonlee.tuchong.com/albums/"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url,user_nick)

    print("结束")