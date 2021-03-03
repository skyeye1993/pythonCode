from selenium import webdriver
import sys
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import pyexcel

if __name__ == '__main__':
    keyword = 'iphone'
    if len(sys.argv) > 1:
        keyword = sys.argv[1]

    option = Options()
    option.add_argument('--headless')
    driver = webdriver.Chrome(options=option)
    driver.get('https://www.jd.com/')

    kw = driver.find_element_by_id('key')
    kw.send_keys(keyword)
    kw.send_keys(Keys.RETURN)

    time.sleep(3)

    # 点击销量排序
    sort_btn = driver.find_element_by_xpath('.//div[@class="f-sort"]/a[2]')
    sort_btn.click()

    rows = []
    has_next = True
    while has_next:
        time.sleep(3)
        next_page = driver.find_element_by_css_selector('a.pn-next')
        print(next_page.location)
        driver.execute_script('window.scrollTo({x},{y})'.format(**next_page.location))
        driver.execute_script('window.scrollBy(0,-500)')
        time.sleep(3)

        products = driver.find_elements_by_class_name('gl-item')
        for p in products:
            row = {}
            sku = p.get_attribute('data-sku')
            row['price'] = p.find_element_by_css_selector('strong.J_%s' % sku).text
            row['name'] = p.find_element_by_css_selector('div.p-name>a>em').text
            row['comments'] = p.find_element_by_id('J_comment_%s' % sku).text
            try:
                row['shop'] = p.find_element_by_css_selector('div.p-shop>span>a').text
            except Exception:
                row['shop'] = '无'
            print(row)
            rows.append(row)
        next_page = driver.find_element_by_css_selector('a.pn-next')
        if 'disabled' in next_page.get_attribute('class'):
            has_next = False
        else:
            next_page.click()
    pyexcel.save_as(records=rows, dest_file_name='high_speed_rail.csv')
    # driver.back()
    driver.quit()
