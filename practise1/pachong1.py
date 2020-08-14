import requests
import bs4
r=requests.get("http://zrzy.jiangsu.gov.cn/nt/gtzx/gzdt/202008/t20200811_956795.htm")
html_doc=r.content.decode('utf-8')
soup = bs4.BeautifulSoup(html_doc,'lxml')
c=soup.find_all("p")
for i in c:
    print(i.text)
print("2")
print("3")