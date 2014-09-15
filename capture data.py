# 导入BeautifulSoup模块和re模块，re是python中正则表达式的模块
import BeautifulSoup
import re
# 生成一个soup对象，doc就是步骤二中提到的
soup = BeautifulSoup.BeautifulSoup(doc)
# 抓取论文标题，作者，简短描述，引用次数，版本数，引用它的文章列表的超链接
# 这里还用了一些正则表达式，不熟悉的先无知它好了。至于'class' : 'gs_rt'中
# 'gs_rt'是怎么来的，这个是分析html文件肉眼看出来的。上面提到的firebug插件
# 让这个变的很简单，只要一点网页，就可以知道对应的html 标签的位置和属性，
# 相当好用。
paper_name = soup.html.body.find('h3', {'class' : 'gs_rt'}).text.鏈枃鍘熷垱鑷�1point3acres璁哄潧
paper_name = re.sub(r'\[.*\]', '', paper_name) # eliminate '[]' tags like '[PDF]'. 涓€浜�-涓夊垎-鍦帮紝鐙鍙戝竷
paper_author = soup.html.body.find('div', {'class' : 'gs_a'}).text
paper_desc = soup.html.body.find('div', {'class' : 'gs_rs'}).text
temp_str = soup.html.body.find('div', {'class' : 'gs_fl'}).text
temp_re = re.match(r'[A-Za-z\s]+(\d*)[A-Za-z\s]+(\d*)', temp_str)
citeTimes = temp_re.group(1)
versionNum = temp_re.group(2)
if citeTimes == '':
  citeTimes = '0'
if versionNum == '':
  versionNum = '0'
citedPaper_href = soup.html.body.find('div', {'class' : 'gs_fl'}).a.attrs[0][1]
