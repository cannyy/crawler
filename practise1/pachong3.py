import requests
import bs4


import xlwings as xw
app=xw.App(visible=True,add_book=False)
app.display_alerts=False
app.screen_updating=False
# 文件位置：filepath，打开test文档，然后保存，关闭，结束程序
filepath=r'test1.xlsx'
wb=app.books.open(filepath)

r=requests.get("http://zrzy.jiangsu.gov.cn/nt/gtzx/gzdt/")
html_doc=r.content.decode('utf-8')
soup = bs4.BeautifulSoup(html_doc,'lxml')
a=len(soup.select('a[target="_blank"]'))
zong=[]
for cishu in range(0,a-1,1):
    zong=zong.append(soup.select('a[target="_blank"]')[cishu]['href'])

n=1
for cishu in range(0,a-1,1):
    print(cishu)
    dingwei=zong[cishu]

    r2=requests.get("http://zrzy.jiangsu.gov.cn/nt/gtzx/gzdt/"+dingwei)
    html_doc=r2.content.decode('utf-8')
    soup = bs4.BeautifulSoup(html_doc,'lxml')
    c=soup.find_all("p")

    for i in c:
        wb.sheets['sheet1'].range('A'+str(n)).value=str(i.text)
        n=n+1



wb.save()
wb.close()
app.quit()

