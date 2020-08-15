import requests
import bs4
import xlwings as xw
import time

# 打开Excel程序，默认设置：程序可见，只打开不新建工作薄
app = xw.App(visible=True,add_book=False)
# 新建工作簿 (如果不接下一条代码的话，Excel只会一闪而过，卖个萌就走了）
wb = app.books.add()

# 打开已有工作簿（支持绝对路径和相对路径）
# wb = app.books.open('example.xlsx')

wb = xw.Book('test1.xlsx')

r = requests.get("http://zrzy.jiangsu.gov.cn/nt/gtzx/gzdt/")
html_doc = r.content.decode('utf-8')
soup = bs4.BeautifulSoup(html_doc, 'lxml')
a = len(soup.select('a[target="_blank"]'))
zong = soup.select('a[target="_blank"]')
n = 1
for cishu in range(0, a - 1, 1):
    fen = zong[cishu].attrs["href"]

    dingwei = fen

    r2 = requests.get("http://zrzy.jiangsu.gov.cn/nt/gtzx/gzdt/" + dingwei)
    html_doc = r2.content.decode('utf-8')
    soup = bs4.BeautifulSoup(html_doc, 'lxml')
    c = soup.find_all("p")

    for i in c:
        wb.sheets['sheet1'].range('A' + str(n)).value = str(i.text)
        n = n + 1

wb.save()
wb.close()
app.quit()
