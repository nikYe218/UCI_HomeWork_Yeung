import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from urllib.parse import urlparse
import cssutils

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)
    
#dictionary
mars_data = {}

def scrape_news():
    browser = init_browser()
    
    #---------------------------------------------------------------------------
    # Mars News
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Get the lastest news title
    news_title = soup.find('h3', attrs={'class': None}).get_text()

    # Get the lastest paragraph text
    news_p = soup.find("div", class_="article_teaser_body").get_text()
    
    # add to dictionary
    mars_data['news_title']= news_title
    mars_data['news_p']=news_p

    #print(mars_data)
    
    browser.quit()

    return  mars_data
    #---------------------------------------------------------------------------
def scrape_featureimg():
    browser = init_browser()
    # Mars Featured Space
    marUrl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(marUrl)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    parseUrl =urlparse(f'{marUrl}')
    main_url = (f'{parseUrl.scheme}://{parseUrl.netloc}')
    main_url=main_url.replace(' ', '')
    
    print(main_url)
    soup1 = BeautifulSoup(html, 'lxml')
    a_tag = soup1.find("article", {"class":"carousel_item"})
    
    print(a_tag)
    html = f'{a_tag}'
    soup = BeautifulSoup(html)
    div_style = soup.find('article')['style']
    style = cssutils.parseStyle(div_style)
    cur_url = style['background-image']
    cur_url=cur_url.replace('url(', '').replace(')', '')  
    print(f'{main_url}{cur_url}')
    
    featured_image_url = f'{main_url}{cur_url}'
    
    mars_data['featured_image_url']=featured_image_url

    print(mars_data)
    
    browser.quit()
    
    return mars_data
    
    #---------------------------------------------------------------------------
def scrape_facts():
    browser = init_browser()
    # Mars Facts
    factUrl = 'https://space-facts.com/mars/'
    tables = pd.read_html(factUrl)
    df = tables[0]
    df.columns=['Description', 'Mars']
    new_df = df.set_index('Description')
    html_table = new_df.to_html(header=True)
    print(html_table)

    # add to dicttionary
    mars_data['table']=html_table
    
    browser.quit()
    
    return mars_data
    #---------------------------------------------------------------------------
def scrape_hemisphere():
    browser = init_browser()
    #Mars Hemisphere
    
    hemUrl = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemUrl)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    hem_items = soup.find_all('div', class_='item')
    prsUrl =urlparse(f'{hemUrl}')
    mainHem_url = (f'{prsUrl.scheme}://{prsUrl.netloc}')
    mainHem_url=mainHem_url.replace(' ', '')
    print(mainHem_url)
    data=[]

    for h in hem_items :
        dicts = {}
        title = h.find('h3').text
        #print(title)
        browser.find_by_text(title).click()
        part_url = h.find('a', class_='itemLink product-item')['href']
        url = f'{mainHem_url}{part_url}'
        #print(url)
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        #print(len(soup.find_all('a',attrs={'target':'_blank'})))
        hem_url =soup.find_all('a',attrs={'target':'_blank'})[3]['href']
        #print(hem_url)
        
        
        #add title and image 
        dicts['title'] = title
        dicts['img_url']= hem_url
        
        #append dict to list
        data.append(dicts)
        time.sleep(2)
        browser.visit(hemUrl)
    #browser.quit()
    mars_data=data
    print(mars_data)
    return mars_data
