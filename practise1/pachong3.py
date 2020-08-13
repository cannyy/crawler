import requests
import bs4
r=requests.get("http://zrzy.jiangsu.gov.cn/nt/gtzx/gzdt/")
html_doc=r.content.decode('utf-8')
soup = bs4.BeautifulSoup(html_doc,'lxml')
dingwei=soup.select('a[target="_blank"]')[0]['href']
print(dingwei)
r2=requests.get("http://zrzy.jiangsu.gov.cn/nt/gtzx/gzdt/"+dingwei)
html_doc=r2.content.decode('utf-8')
soup = bs4.BeautifulSoup(html_doc,'lxml')
c=soup.find_all("p")
for i in c:
    print(i.text)
print("test")
