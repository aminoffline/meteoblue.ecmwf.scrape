from bs4 import BeautifulSoup
from selenium.webdriver import Chrome , Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import ChromeOptions ,  FirefoxOptions
import requests
import time
import datetime
#import urllib
import re, os
import csv


head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

proxies = {'http': '127.0.0.1:10809','https': '127.0.0.1:10809'}

"""
city_names = {'Kerman':'kerman_iran_128234?','Arzū’īyeh':'arz%c5%ab%e2%80%99%c4%abyeh_iran_142902?','Anār':'an%c4%81r_iran_143499?',
              'Bāft':'b%c4%81ft_iran_142247?','Bardsīr':'bards%C4%ABr_iran_124647?','Bam':'bam_iran_141736?',
              'Jiroft': 'j%c4%abroft_iran_6925362?', 'Rabor': 'r%c4%81bor_iran_119010?', 'Ravar': 'r%c4%81var_iran_118704?',
              'Rafsanjan': 'rafsanj%c4%81n_iran_118994?','Rudbar':'esl%c4%81m%c4%81b%c4%81d_iran_6928551?','Rigan':'r%c4%abg%c4%81n_iran_118509?',
              'Zarand': 'zarand_iran_111421?',
              'Sirjan': 's%c4%abrj%c4%81n_iran_114259?', 'Shahdad': 'shahd%c4%81d_iran_115960?', 'Shahr-eBabak': 'shahr-e-b%c4%81bak_iran_115781?',
              'Anbarabad': '%e2%80%98anbar%c4%81b%c4%81d_iran_143471?','Faryab':'f%c4%81ry%c4%81b_iran_134735?', 'Fahraj': 'fahraj_iran_134962?',
              'Qaleh Ganj':'qal%e2%80%98eh-ganj_iran_120323?','Kahnuj':'kahn%c5%abj_iran_6961608?','Kuhebanan': 'k%c5%abhban%c4%81n_iran_126411?',
              'Golbaf': 'golb%c4%81f_iran_403529?', 'Lalehzar': 'l%c4%81lehz%c4%81r_iran_125945?','Mahan': 'm%c4%81h%c4%81n_iran_125427?',
              'Manujan': 'man%c5%abj%c4%81n_iran_124914?', 'Narmashir': 'narm%c4%81sh%c4%abr_iran_118323?'
              }


date_ = datetime.datetime.now().strftime("%y.%m.%d ")
time_ = datetime.datetime.now().strftime("%H")

try:
    os.mkdir(f'{date_}')
except Exception as err:
    pass
dir_date_ = re.sub(r"'","",date_)
dir_date_ = re.sub(r" ","",dir_date_)
try:
    dir_time = os.mkdir(f'{dir_date_}/{time_}')
except Exception as err:
    pass

count=0
for i,j in zip(city_names.values(),city_names):
    my_url = f'https://www.meteoblue.com/en/weather/forecast/multimodel/{i}fcstlength=168&params%5B%5D=&params%5B%5D=NEMSGLOBAL&params%5B%5D=&params%5B%5D=IFS04&params%5B%5D=UMGLOBAL10&params%5B%5D=ICON&params%5B%5D=GFS05'
    #my_url = f'https://www.meteoblue.com/en/weather/forecast/multimodel/{i}fcstlength=144&params%5B%5D=&params%5B%5D=NEMSGLOBAL&params%5B%5D=&params%5B%5D=IFS04&params%5B%5D=UMGLOBAL10&params%5B%5D=ICON&params%5B%5D=GFS05'
    response = requests.get(my_url,headers=head, timeout=60, verify=True, proxies=proxies)
    #response = requests.get(my_url,headers=head, timeout=45 , verify=True )

    if response.ok == True:
        print(response.url)
        soup = BeautifulSoup(response.text, 'lxml')
        for post in soup.find_all('main', class_="main"):
            time.sleep(1)
            try:
                body = post.find('a', id="chart_download")
                img_url = body.get('href')
                img = re.sub(r'//','https://',img_url)
                r = requests.get(img, headers=head, allow_redirects=True, verify=True)
                with open(f'{dir_date_}/{time_}/MetB-{time_}.H-{count}-{j}.jpg', "wb") as f:
                    f.write(r.content)
                count += 1
                time.sleep(1)
            except Exception as err:
                print(err)
    else:
        time.sleep(60)



"""
"""
c_path = "C:\Program Files\chromedriver108.exe "

for i in city_code:
    my_url = f'https://www.meteoblue.com/en/weather/forecast/multimodel/{i}fcstlength=168&params%5B%5D=&params%5B%5D=NEMSGLOBAL&params%5B%5D=&params%5B%5D=IFS04&params%5B%5D=UMGLOBAL10&params%5B%5D=ICON&params%5B%5D=GFS05'
    driver = webdriver.Chrome(c_path)
    driver.get(my_url)
    #driver.file_detector
    chart = driver.find_element_by_id('chart_download')
    image = chart.get_attribute('href')
    print(image)
    r = requests.get(image,headers=head ,allow_redirects=True , verify=True)
    open(f'{city_code.index(i)}.png', 'wb').write(r.content)


    print(chart.text)
    #main = driver.find_elements_by_id('blooimage') #("image-lazyload loaded")
    #img = main.find_element('img',cla)
    #print(main.__getitem__('src'))
    #driver.save_screenshot(f"{city_code.index(i)}-.png")
    driver.close()
"""
"""

"""
runtime = input('which Run is it ? 00 or 12 :')

today = datetime.datetime.now() - datetime.timedelta(days=1)
today = today.strftime("%Y%m%d")
todayy = datetime.datetime.now() - datetime.timedelta(days=1)
todayy = todayy.strftime(f"%a %d %b %Y {runtime} UTC")

c_path = "C:\Program Files\chromedriver108.exe "
f_path = "S:\geckodriver.exe"
options = ChromeOptions()
options.headless = True
driver = Chrome(c_path , options=options)
#f_options = FirefoxOptions()
#f_options.headless = True
#driver = Firefox(Service(f_path),firefox_options=f_options)


city_n_coor = []
with open('coordinates.v2.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        city_n_coor.append(row)

city_n_coor = [list(i) for i in city_n_coor]


print(todayy)

for i in city_n_coor:
    time.sleep(5)
    ecmwf_url = f'https://charts.ecmwf.int/products/opencharts_meteogram?base_time={today}{runtime}00&epsgram=classical_10d&lat={i[1]}&lon={i[2]}&station_name={i[0]}'
    print(ecmwf_url)

    driver.get(ecmwf_url)
    soup = BeautifulSoup(driver.page_source,'lxml')
    post = soup.find('div' , class_="jss14")
    print(soup)
    imag = soup.find_all(attrs={"alt": f"{todayy}"})
    #img_url = imag.get('src')
    #print(imag)
    #r = requests.get(imag, headers=head, allow_redirects=True, verify=True)
   # with open(f'{i[0]}.jpg', "wb") as f:
     #   f.write(r.content)
    driver.quit()
#<img class="jss200 jss47 jss204 jss50" alt="Fri 16 Dec 2022 00 UTC" src="https://charts.ecmwf.int/streaming/20221216-1650/6d/render-worker-commands-5d9fc45c7d-f9t4q-6fe5cac1a363ec1525f54343b6cc9fd8-bUCqlJ.png">












