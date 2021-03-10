#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


url = "https://www.themoviedb.org/movie?language=en-US"


# In[11]:


response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
# soup = BeautifulSoup(response.content, 'html.parser')


# # Movie Poster Url Scrape

# In[25]:


#### Eg: nested structure

posterUrl = soup.select(".item.poster.card.image_content.result")
posterUrl


# In[22]:


ImgList = soup.select("div.image_content")


# In[17]:


ImgList[0].find("img").attrs.get("data-src")


# In[9]:


poster fade lazyautosizes lazyloaded
soup.select(".poster.fade.lazyautosizes.lazyloaded")


# In[10]:


"""Get the url """
rawPosterUrl = soup.select('.poster.lazyload.fade')
PosterUrl = list(map(lambda x:x.attrs.get('data-src'),rawPosterUrl))

"""Download the poster to local"""
#urllib.request.urlretrieve(url, path)


# In[5]:


PosterUrl

