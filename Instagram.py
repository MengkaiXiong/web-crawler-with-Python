#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
from lxml import html
from urllib.request import Request, urlopen
import urllib.request
from selenium import webdriver
import os


# In[2]:


url = "https://www.instagram.com"


options = webdriver.ChromeOptions()
options.add_argument('--headless')

# browser = webdriver.Chrome(executable_path="/Users/zili/Documents/projects/webscraping/chromedriver",options=options)
browser = webdriver.Chrome(executable_path="/Users/zili/Documents/projects/webscraping/chromedriver")

browser.get(url)
innerHTML = browser.page_source #returns the inner HTML as a string

soup = BeautifulSoup(innerHTML,'lxml')


# # Find login button

# In[3]:


soup.select(".izU2O")


# In[5]:


loginUrl = soup.select(".izU2O")[0].find('a').attrs.get('href')
loginUrl


# In[6]:


url + loginUrl


# In[3]:


loginP = browser.find_element_by_css_selector('.izU2O')


# In[4]:


loginP.find_element_by_tag_name('a').click()


# In[5]:


username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")


# In[6]:


username.send_keys("lizishuo19940328@gmail.com")
password.send_keys("***")


# In[73]:


loginButton = browser.find_elements_by_tag_name('button')


# In[74]:


len(loginButton)


# In[7]:


browser.find_element_by_xpath('//button[text()="Log in"]').click()


# In[8]:


try:
    browser.find_element_by_xpath('//button[text()="Not Now"]').click()
except:
    pass


# In[9]:


innerHtml = browser.page_source


# In[10]:


soup = BeautifulSoup(innerHtml,'lxml')


# In[11]:


soup.select(".C4VMK")


# In[ ]:




