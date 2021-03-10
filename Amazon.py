#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
from lxml import html
from urllib.request import Request, urlopen
import urllib.request
from selenium import webdriver


# In[3]:


url = "https://www.amazon.com/Black-Friday/b/?ie=UTF8&node=384082011&ref=nav_cs_gb"

options = webdriver.ChromeOptions()
options.add_argument('--headless')

browser = webdriver.Chrome(executable_path="/Users/zili/Documents/projects/webscraping/chromedriver",options=options)
browser.get(url)
innerHTML = browser.page_source #returns the inner HTML as a string

soup = BeautifulSoup(innerHTML,'lxml')


# In[5]:


soup.select("div.a-row.dealContainer.dealTile")


# # Login

# In[24]:


loginUrl = "https://www.amazon.com/ap/signin?_encoding=UTF8&accountStatusPolicy=P1&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcss%2Forder-history%3Fie%3DUTF8%26ref_%3Dnav_youraccount_orders&pageId=webcs-yourorder&showRmrMe=1"


# In[25]:


options = webdriver.ChromeOptions()
options.add_argument('--headless')

browser = webdriver.Chrome(executable_path="/Users/zili/Documents/projects/webscraping/chromedriver")
browser.get(loginUrl)
innerHTML = browser.page_source #returns the inner HTML as a string

soup2 = BeautifulSoup(innerHTML,'lxml')


# In[26]:


soup2.findAll('input')


# In[27]:


soup2.find("input",{'id':'ap_email'})


# In[21]:


soup2.find("input",{'id':'ap_password'})


# In[29]:


username = browser.find_element_by_id("ap_email") #username form field
password = browser.find_element_by_id("ap_password") #password form field

username.send_keys("zl2528@columbia.edu")
password.send_keys("****")

submitButton = browser.find_element_by_id("signInSubmit") 
submitButton.click() 


# In[ ]:




