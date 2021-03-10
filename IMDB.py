#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import re
import urllib
import json
# Download IMDB's Top 250 data
url = 'http://www.imdb.com/chart/top'
base = "http://www.imdb.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

### option 2
# soup = BeautifulSoup(response.content, 'html.parser')


# In[10]:


response.content[:1000]


# # Eg

# In[15]:


test = soup.findAll('img',{"width":45,'height':'67'})
len(test)


# In[2]:


egClass = "posterColumn"


# In[16]:


egList = soup.select("td.posterColumn")
egtd = egList[0]


# In[19]:


egtd


# In[20]:


egtd.find("img").attrs.get("src")


# # Get title Column and link to Child content (jump to child link)

# In[3]:


TitleColumn = soup.select(".titleColumn > a")

child = TitleColumn[0]

urlChild= child.attrs.get("href")
base + urlChild


# In[20]:


urlContent = requests.get(base + urlChild)

soupChild  = BeautifulSoup(urlContent.text,'lxml')

contentChild = soupChild.select('.flatland')


# # Get poster url list

# In[30]:


# posterList = soup.findAll('td', class_='posterColumn')
posterList = soup.select('.posterColumn img')
posterUrl = list(map(lambda x:x.attrs.get("src"),posterList))


# In[49]:


def downloadImage(url,path):
    try:
        urllib.request.urlretrieve(url, path)
    except:
        raise("download meet an issue")
downloadImage(posterUrl[0],'data/poster/eg.jpg')


# # Get movie title, author and others

# In[6]:


movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

imdb = []

# Store each item into dictionary (data), then put those into a list (imdb)
for index in range(0, len(movies)):
    # Seperate movie into: 'place', 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"movie_title": movie_title,
            "year": year,
            "place": place,
            "star_cast": crew[index],
            "rating": ratings[index],
            "vote": votes[index],
            "link": links[index]}
    imdb.append(data)

for item in imdb:
    print(item['place'], '-', item['movie_title'], '('+item['year']+') -', 'Starring:', item['star_cast'])
 


# In[ ]:




