from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')
print(driver.title)
print(driver.current_url)
a = driver.find_element_by_xpath('//div[@id="s-top-left"]/a[1]')
print(a.text)
print(a.get_attribute('name'))
print(a.get_property('name'))
print(a.value_of_css_property('color'))
# a.click()
# driver.back()
# driver.forward()
kw = driver.find_element_by_id('kw')
kw.send_keys('python')
su = driver.find_element_by_id('su')
su.click()
h3_list = driver.find_elements_by_tag_name('h3')
for h3 in h3_list:
    print(h3.text)

# driver.execute_script('alert(1234)')
driver.execute_script('window.scrollTo(0,window.bodyHeight)')
driver.execute_script('window.scrollTo(0,document.body.Height)')
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

next_page = driver.find_element_by_class_name('n')
next_page.click()
driver.quit()