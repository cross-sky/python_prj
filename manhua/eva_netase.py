from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException, MoveTargetOutOfBoundsException,WebDriverException
import time
import requests
import os

#profile_directory = r'C:\Users\apple\AppData\Roaming\Mozilla\Firefox\Profiles\kuzq39zz.default'
#profile = webdriver.FirefoxProfile(profile_directory)
#profile = webdriver.FirefoxProfile()
#driver = webdriver.Firefox(firefox_profile=profile)

url = 'https://manhua.163.com/source/5119732667930155653'


profile = webdriver.FirefoxProfile()
drivers = webdriver.Firefox(firefox_profile=profile)
#drivers.get(url)
#time.sleep(5)

'''
    profile = webdriver.FirefoxProfile()
    drivers = webdriver.Firefox(firefox_profile=profile)
    drivers.get(url)
'''
def get_urls(url):
    '''

    :param url:
    :return:
    '''
    drivers.get(url)
    time.sleep(5)
    l1 = drivers.find_element_by_class_name('sr-catalog__bd')
    l2 = l1.find_elements_by_class_name('m-chapter-item')
    result = []
    for c in l2:
        r = []
        d = c.find_element_by_class_name('f-toe')
        title = d.get_attribute('title')
        href = d.get_attribute('href')
        r.append(title)
        r.append(href)
        result.append(r)
    return result

cur_path = os.getcwd()
def make_dir(path):
    target_path = cur_path + r'\\result\\' + path
    if not os.path.exists(target_path):
        os.makedirs(target_path)

    return target_path

def write_img(path, name, url):
    r = requests.get(url)
    p = path + '\\' +name+'.jpeg'

    if not os.path.exists(p):
        with open(p, 'wb') as f:
            f.write(r.content)


def get_page(url, title):
    drivers.get(url)
    #time.sleep(5)
    drivers.implicitly_wait(5)
    #imgbox = drivers.find_element_by_class_name('img-box-wrapper')
    #imgs = imgbox.find_elements_by_class_name('img-box')

    #cur_index = drivers.find_element_by_class_name('js-currentIndex').text
    total_index = drivers.find_element_by_class_name('js-totalIndex').text
    print('total_page:', total_index)
    r_dic = {}

    path = make_dir(title)

    try:
        tucao = drivers.find_element_by_class_name('js-switchTucao-mini')
        ActionChains(drivers).context_click(tucao).perform()
    except ElementNotInteractableException as e:
        print(e)
    except MoveTargetOutOfBoundsException as e:
        print(e)
    except WebDriverException as e:
        print(e)

    cur_count = 0
    last_cur = 0
    for index in range(100):    #int(total_index)
        url1 = url + '#imgIndex=' + str(index)
        drivers.get(url1)
        #time.sleep(1)
        drivers.implicitly_wait(2)

        #drivers.find_element_by_xpath(r'//*[@id="auto-id-1550936401856"]')


        imgbox = drivers.find_element_by_class_name('img-box-wrapper')
        imgs = imgbox.find_elements_by_class_name('img-box')
        cur_index = drivers.find_element_by_class_name('js-currentIndex').text
        print('cur_page:', cur_index)

        if cur_index == last_cur:
            cur_count += 1
            if cur_count >= 4:
                break
            elif cur_count == 1:
                continue
        else:
            last_cur = cur_index
            cur_count = 0

        end = drivers.find_elements_by_class_name('end-text')
        if len(end) > 0:
            break

        for i in imgs:
            if 'right' in i.get_attribute('class'):
                value = str(cur_index) + 'a'
            else:
                value = str(cur_index) + 'b'
            img_elem = i.find_element_by_tag_name('img')
            key = img_elem.get_attribute('src')
            if key not in r_dic.keys():
                r_dic[key] = value
                write_img(path=path, name=value, url=key)

    return r_dic

def readtxt_urls(path):
    with open(path, 'r') as f:
        urls = f.readlines()[0] # type:str

    lines = urls.strip('[[')
    lines = lines.strip(']]')
    line_ls = lines.split('], [')
    return line_ls



#url2 = 'https://manhua.163.com/reader/5119732667930155653/5119647669120517969#imgIndex=0'
#r_urls = get_page(url2, '2_part')

if __name__ == '__main__':
    list_urls = readtxt_urls('urls.txt')
    for l in list_urls:
        l = l.replace("'", '')
        l = l.replace('\\', '')
        title, url = l.split(', ')
        print(title, url)
        get_page(url, title)
        #break

    drivers.close()


