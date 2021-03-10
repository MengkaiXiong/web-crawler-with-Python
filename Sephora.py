#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
from lxml import html
from urllib.request import Request, urlopen
import urllib.request
from selenium import webdriver


# # Normal process for webscraping

# In[2]:


url = "https://www.sephora.com/new-beauty-products"

page = requests.get(url)


# In[3]:


"""
r.text is the content of the response in unicode, and r.content is the content of the response in bytes.
"""

soup = BeautifulSoup(page.text,'html5lib')
# soup1 = BeautifulSoup(page.text,'html.parser')
# soup2 = BeautifulSoup(page.text,'lxml')


# In[5]:


"""Take one class as an example"""
egClass = "u-size1of4 SkuItem SkuItem--135 SkuItem SkuItem--135"

soup.find_all('a',attrs={'class': egClass})

egClassCss = egClass.replace(" ",'')
soup.select(".u-size1of4.SkuItem--135.SkuItem.SkuItem--135")


# # selenium part 

# In[ ]:


from selenium import webdriver

browser = webdriver.Chrome(executable_path="/Users/zili/Documents/projects/webscraping/chromedriver")
browser.get(url)
innerHTML = browser.page_source


# In[7]:


soupNew = BeautifulSoup(innerHTML,'lxml')

soupNew.select(".u-size1of4.SkuItem--135.SkuItem.SkuItem--135")


# # Optimize

# In[8]:


options = webdriver.ChromeOptions()
options.add_argument('--headless')


# In[12]:


browser = webdriver.Chrome(executable_path="/Users/zili/Documents/projects/webscraping/chromedriver",options=options)
browser.get(url)
innerHTML = browser.page_source


# In[10]:


soupNew1 = BeautifulSoup(innerHTML,'lxml')

soupNew1.select(".u-size1of4.SkuItem--135.SkuItem.SkuItem--135")


# In[ ]:




