''' 

Please install requirement.txt 

Real-World Example: Multithreading for I/O bound Tasks
Scenario: Web Scraping

Web Scraping often involves making numerous network requests to
fetch webpages. These task are I/O bound because they spend a lot of time
waiting for the network to respond from servers.

Multithreading can significantly improve the performance by allowing
multiple webpages requests to fetch concurrently.

'''

import threading
import requests
from bs4 import BeautifulSoup

urls=[
'https://python.langchain.com/docs/introduction/',

'https://python.langchain.com/docs/concepts/',

'https://python.langchain.com/docs/tutorials/agents/'

]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')

threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)  
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
print(threads)
print("All web pages are fetched")