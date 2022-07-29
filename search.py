from unicodedata import category
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
      
      result = soup(text=lambda t: "More results from " in t.text)
      
      tag = soup.body
      ask_result = soup(text=lambda t: "People also ask" in t.text)
      ask_search_stringsTmp=[]
      people_also_ask_data=[];
      if(len(ask_result)>0):
         skip=0 
         for string in tag.strings:
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
         people_also_ask_data=people_also_ask.get_related_questions(self.name)
      tag = soup.body
      search_strings=[]
      skip=0
      for string in tag.strings:
         if(string.strip()=='Related searches'):
            skip=1
         if(string.strip()=='Next >'):
            skip=0  
         if(skip<1 or string.strip()==''):
            continue
      #   list.reverse() 
         search_strings.append(string.strip())
      del search_strings[0:len(search_strings)-8]

      
      data={}
      if(len(result)>0):
         if(len(result)>1):
            # domain = result[0].split(' ', -1)[3]
            data['success']=True
            # data['domain']=domain
            data['type']='more searches'
            data['result']=result
            data['related_search']=search_strings
            data['people_also_ask']=people_also_ask_data
            return data
         else:   
            # domain = result[0].split(' ', -1)[3]
            data['success']=True
            # data['domain']=domain
            data['type']='more searches'
            data['result']=result
            data['related_search']=search_strings
            data['people_also_ask']=people_also_ask_data
            return data
      else:
         links = []
         # for link in soup.find_all('a', href=True):
         #    if(urlparse(link['href']).netloc !=''):
         #       links.append(urlparse(link['href']).netloc) 
         for j in search(query=self.name, tld="com", num=10, stop=10, pause=5): 
            links.append(urlparse(j).netloc)  

         data['success']=False
         data['domain']='NULL'
         data['type']='NULL' 
         data['links']=links
         data['related_search']=search_strings
         data['people_also_ask']=people_also_ask_data
         return data 
       
if __name__=='__main__':
    line=1
    with open('searches.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        csv_writer=csv.writer(open('output.csv','w'),delimiter=',');
        csv_writer.writerow(['Keyword','Category','Domain Matched','Match Type','PAA 1','PAA 2','PAA 3','PAA 4','RS 1','RS 2','RS 3','RS 4','RS 5','RS 6','RS 7','RS 8'])

      #   Keyword	Domain Matched	Match Type
        matchDomainList=[]
        for row in csv_reader:
            sleep(randint(20,60))
            gs = Gsearch_python(row['search_terms'])
            searchResult=gs.Gsearch();
            
            try:
               paa1=searchResult['people_also_ask'][0]
            except IndexError:
               paa1='-'
            try:
               paa2=searchResult['people_also_ask'][1]
            except IndexError:
               paa2='-'
            try:
               paa3=searchResult['people_also_ask'][2]
            except IndexError:
               paa3='-'
            try:
               paa4=searchResult['people_also_ask'][3]
            except IndexError:
               paa4='-'
                       
            try:
               rs1=searchResult['related_search'][0]
            except IndexError:
               rs1='-'   
            
            try:
               rs2=searchResult['related_search'][1]
            except IndexError:
               rs2='-' 
            try:
               rs3=searchResult['related_search'][2]
            except IndexError:
               rs3='-' 

            try:
               rs4=searchResult['related_search'][3]
            except IndexError:
               rs4='-'    
            try:
               rs5=searchResult['related_search'][4]
            except IndexError:
               rs5='-'   
            
            try:
               rs6=searchResult['related_search'][5]
            except IndexError:
               rs6='-' 
                 
            try:
               rs7=searchResult['related_search'][6]
            except IndexError:
               rs7='-'   

            try:
               rs8=searchResult['related_search'][7]
            except IndexError:
               rs8='-'
            
            if(searchResult['success']):
               #  domain_writer=csv.writer(open('domain-matches.txt','a'),delimiter=',');
               #  people_also_ask=searchResult['people_also_ask']
                domainList=[]
               
                for item in searchResult['result']:
                   if(line==1):
                     csv.writer(open('domain-matches.txt','w'),delimiter=',').writerow(['matched_domain'])
                     line=line+1
                   domain = item.split(' ', -1)[3]
                   domainList.append(domain)
                   csv.writer(open('domain-matches.txt','a'),delimiter=',').writerow([domain])
                appendableArray= [row['search_terms'],row['category'],domainList[0], searchResult['type'],paa1,paa2,paa3,paa4,rs1,rs2,rs3,rs4,rs5,rs6,rs7,rs8] 
               #  for pasd in searchResult['people_also_ask']:
               #      appendableArray.append(pasd)
                csv_writer.writerow(appendableArray)    
            else:
                if(line==1):
                     csv.writer(open('domain-matches.txt','w'),delimiter=',').writerow(['matched_domain'])
                     # csv.writer(open('domain-matches.txt','a'),delimiter=',').writerow(['policies.google.com'])
                     line=line+1
                with open('domain-matches.txt', mode='r') as txt_matches_file:
                     text_reader = csv.DictReader(txt_matches_file) 
                 
                     for item in text_reader: 
                        matchDomainList.append(item['matched_domain']) 
               #  people_also_ask=searchResult['people_also_ask'] 
               #  print(searchResult['links'])  
                a_set = set(matchDomainList)
                b_set = set(searchResult['links'])
               
                if (a_set & b_set):
                     commonDomain=list(a_set & b_set)
                     appendableArray= [row['search_terms'],row['category'],commonDomain[0],'single occurance',paa1,paa2,paa3,paa4,rs1,rs2,rs3,rs4,rs5,rs6,rs7,rs8] 
                     # for pasd in searchResult['people_also_ask']:
                     #    appendableArray.append(pasd)
                     searchItem=appendableArray
                else:
                  searchItem=[row['search_terms'],row['category'],'NULL','NULL',paa1,paa2,paa3,paa4,rs1,rs2,rs3,rs4,rs5,rs6,rs7,rs8]       
               #  print(np.intersect1d(matchDomainList, searchResult['links']))
               #  if(np.intersect1d(matchDomainList, searchResult['links'])):
               #    searchItem=[row['search_terms'],'NULL','NULL']
               #  else:
               #      searchItem=[row['search_terms'],'NULL','NULL']            
                csv_writer.writerow(searchItem)    
            