from curses import echo
from sys import api_version
from urllib.parse import urlparse
from random import randint
from time import sleep
import csv
import requests
import bs4
import random
from googlesearch import search
import people_also_ask


# Performing google search using Python code
class Gsearch_python:
   def __init__(self,name_search):
      self.name = name_search
   def Gsearch(self):
      try :
         from googlesearch import search,lucky
      except ImportError:
         print("No Module named 'google' Found")
      text= "Inner thigh workout"
      links = []
      url = 'https://google.com/search?q=' + self.name+'&hl=en'
  
      # Fetch the URL data using requests.get(url),
      # store it in a variable, request_result.
      A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
       )
 
      Agent = A[random.randrange(len(A))]
 
      headers = {'user-agent': Agent}

      request_result=requests.get( url, headers=headers)
      
      # Creating soup from the fetched request
      soup = bs4.BeautifulSoup(request_result.text,
                              "html.parser")
      tag = soup.body
      ask_result = soup(text=lambda t: "People also ask" in t.text)
      ask_search_stringsTmp=[]
      people_also_ask_data=[];
      if(len(ask_result)>0):
         # print (self.name + " Found!")
         skip=0 
         for string in tag.strings:
               #   print(self.name + "->>" +string.strip() + ", ")
               if(string.strip()=='People also ask'):
                  skip=1
               if(string.strip()=='Next >'):
                  skip=0  
               if(skip<1 or string.strip()==''):
                  continue
               ask_search_stringsTmp.append(string.strip())
         loop=0
         for paask in ask_search_stringsTmp:
              if(loop>4 or loop==0):
                  loop=loop+1 
                  continue
              else:
                    loop=loop+1 
                    people_also_ask_data.append(paask)
                   
      else:
         people_also_ask_data=people_also_ask.get_related_questions(self.name,4)

      print(people_also_ask_data)
      # skip=0
      # if search('People also ask', tag.strings):
      #     print (self.name + " Found!")
      # else:
      #    print (self.name + " Not found!")
      # if tag.find('People also ask') != -1:
      #    # print(self.name + " Found!")
      #    for string in tag.strings:
      #       # print(string + ", ")
      #       if(string.strip()=='People also ask' or string.strip()=='people also ask'):
      #          # skip=1
      #          print(self.name)
      #       else:
      #          print(self.name)
      #          search_strings.append(string)
      #          # print(string)   
      #       # if(string.strip()=='Next >'):
      #       #    skip=0  
      #       # if(skip<1 or string.strip()==''):
      #       #    continue
      #    print(search_strings)
      # else:
      #    print(self.name + " Not found!")
      # for string in tag.strings:
         # if(string.strip()=='Related searches'):
         #    skip=1
         # if(string.strip()=='Next >'):
         #    skip=0  
         # if(skip<1 or string.strip()==''):
         #    continue
      #   list.reverse() 
         # search_strings.append(string.strip())
      # del search_strings[0:len(search_strings)-8]
      # print(search_strings)





      
      # search_strings=[]
      # skip=0
      # for string in tag.strings:
      #    if(string.strip()=='Related searches'):
      #       skip=1
      #    if(string.strip()=='Next >'):
      #       skip=0  
      #    if(skip<1 or string.strip()==''):
      #       continue
      # #   list.reverse() 
      #    search_strings.append(string.strip())
      # del search_strings[0:len(search_strings)-8]
      # print(search_strings[0]) OK






      # skip=0
      # for item in search_strings:
      #    if(item=='Related searches'):
      #       skip=1
      #       print('IN')
      #       print(item)
      #    if(skip<1):
      #       continue
      #       print('OUT')
      #    print(item)
         
      # p = soup.select(".y6Uyqe .AB4Wff")
      # result = soup(text=lambda t: "More results from " in t.text)
      # people_also_ask_data=people_also_ask.get_related_questions(self.name)
      # print(temp)
      # people_also_ask_data=[]
      # temp = soup.find( "div" , class_='BNeawe')
      # # print(temp)
      # related_search=[]
      # for rls in  temp.findAll('li'):
      #    related_search.append(rls.find('div',class_="BNeawe").text)
      #    # print(rls.find('div',class_="BNeawe").text)
      # if(len(related_search)<1):
      #    for rls1 in  soup.find( "div" , class_='BNeawe'):
      #       related_search.append(rls1.text)
            # related_search1 = soup.find( "div" , class_='BNeawe')
      # print(related_search[6])

      # print(related_search[0])
      # print(temp.findAll('li'))
      # data={}
      # if(len(result)>0):
      #    if(len(result)>1):
      #       # domain = result[0].split(' ', -1)[3]
      #       data['success']=True
      #       # data['domain']=domain
      #       data['type']='more searches'
      #       data['result']=result
      #       data['related_search']=related_search
      #       data['people_also_ask']=people_also_ask_data
      #       return data
      #    else:   
      #       # domain = result[0].split(' ', -1)[3]
      #       data['success']=True
      #       # data['domain']=domain
      #       data['type']='more searches'
      #       data['result']=result
      #       data['related_search']=related_search
      #       data['people_also_ask']=people_also_ask_data
      #       return data
      # else:
      #    links = []
      #    # for link in soup.find_all('a', href=True):
      #    #    if(urlparse(link['href']).netloc !=''):
      #    #       links.append(urlparse(link['href']).netloc) 
      #    for j in search(query=self.name, tld="com", num=10, stop=10, pause=5): 
      #       links.append(urlparse(j).netloc)  

      #    data['success']=False
      #    data['domain']='NULL'
      #    data['type']='NULL' 
      #    data['links']=links
      #    data['related_search']=related_search
      #    data['people_also_ask']=people_also_ask_data
      #    return data 
       
if __name__=='__main__':
    line=1
    with open('searches.txt', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
   #  gs = Gsearch_python('python tutorial digitalocean')
   #  searchResult=gs.Gsearch();  
   #  print(searchResult)
        for row in csv_reader:
                  sleep(randint(1,5))
                  
                  gs = Gsearch_python(row['search_terms'])
                  searchResult=gs.Gsearch();
            