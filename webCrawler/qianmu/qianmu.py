import requests
from lxml import etree

start_url = 'http://www.qianmu.org/ranking/1528.htm'


def fetch(url):
    r = requests.get(url)
    if r.status_code != 200:
        r.raise_for_status()
    return r.text.replace('\t', '')


def parse_university(url):
    selector = etree.HTML(fetch(url))
    data = {}
    data['name'] = selector.xpath('//div[@id="wikiContent"]/h1/text()')[0]
    table = selector.xpath('//div[@id="wikiContent"]/div[@class="infobox"]/table')
    if len(table) == 0:
        return None
    keys = table[0].xpath('.//td[1]/p/text()')
    cols = table[0].xpath('.//td[2]')
    values = [' '.join(col.xpath('.//text()')) for col in cols]
    if len(keys) != len(values):
        return None
    data.update(zip(keys, values))
    return data


def process_data(data):
    if data:
        print(data)


if __name__ == '__main__':
    selector = etree.HTML(fetch(start_url))
    links = selector.xpath('//div[@class="rankItem"]/table//tr[position()>1]/td[2]/a/@href')
    for link in links:
        data = parse_university(link)
        process_data(data)
