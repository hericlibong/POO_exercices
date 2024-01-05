import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re


class PlaceSpider(CrawlSpider):
    name = "place"
    allowed_domains = ["placedeslibraires.fr"]
    start_urls = ["https://www.placedeslibraires.fr/list-136855/9e-fete-du-livre-de-quiberon/"]

    rules = (Rule(LinkExtractor(restrict_xpaths="//ul[@class='resultsList  liste_palmares col-xs-12']/li//p[@class='zone_image']/a"), callback="parse_item", follow=True),
             Rule(LinkExtractor(restrict_xpaths="//a[@class='nav-next']")))

    def parse_item(self, response):
        titre = response.xpath("//h1/text()").get().strip()
        #titre = titre.strip() if titre else None
        auteur = response.xpath("//h2[@class='auteurs mb-01']//span/text()").get()
        ISBN = response.xpath("//li[@class='col-xs-12 no-padding EAN']/p[2]/text()").get()
        prix = response.xpath("//div[@class='portail-infoFormatPrix col-xs-12 no-padding']/span/strong/text()").get().replace('€', '')
        prix = prix.strip() if prix else None
        prix = float(prix) if prix else None
        genre = response.xpath("//a[@class='gtl'][2]/text()").get().strip()
        pub_year = response.xpath("//div[@class='autresInformations-content col-md-6 col-xs-12'][1]//li[4]/p[@class='info']/text()").get()
        pub_year = re.search(r'\d{4}', pub_year).group() if pub_year else None
        pub_year = int(pub_year) if pub_year else None
        results = {

            'titre':titre,
            'auteur':auteur,
            'ISBN':ISBN, 
            'genre':genre,
            'prix':prix,
            'pub_year':pub_year

        }
        yield results
