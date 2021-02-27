import requests
import threading
import time
from queue import Queue
from lxml import etree

start_url = 'http://www.qianmu.org/ranking/1528.htm'
link_queue = Queue()
threads = []
threads_num = 10

def fetch(url):
    r = requests.get(url)
    if r.status_code != 200:
        r.raise_for_status()
    return r.text.replace('\t','')


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

def download():
    while True:
        link = link_queue.get()
        if link is None:
            break
        data = parse_university(link)
        process_data(data)
        link_queue.task_done()

if __name__ == '__main__':
    start_time = time.time()
    selector = etree.HTML(fetch(start_url))
    links = selector.xpath('//div[@class="rankItem"]/table//tr[position()>1]/td[2]/a/@href')
    for link in links:
        link_queue.put(link)

    for i in range(threads_num):
        t = threading.Thread(target=download)
        t.start()
        threads.append(t)

    link_queue.join()

    for i in range(threads_num):
        link_queue.put(None)

    for t in threads:
        t.join()

    print('finished time: %.2f', (time.time() - start_time))