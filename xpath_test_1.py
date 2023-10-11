# _*_coding:utf-8 _*_
# @Time　　 : 2019/8/26   12:43
# @Author　 : zimo
#@ File　   :xpath_text_1.py
#@Software  :PyCharm

# 1、导入
from  lxml import etree
wb_data = """
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html" id="places_neighbours__row">9,596,960first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html" id="places_neighbours__row">fourth item</a></li>
                 <li class="item-0"><a>fifth item</a></li>
                 <li class="bectter"><a>fifth item</a></li>
             </ul>
             <book>
                    <title lang="eng">Harry Potter</title>
                    <price>29.99</price>
            </book>
            <book>
                <title lang="zh" id="places_neighbours__row">Learning XML</title>
                <price>38</price>
            </book>
            <book>
                <title>Python</title>
                <price>55.55</price>
            </book>
         </div>
        """
# 2、基本使用
html=etree.HTML(wb_data)
# etree.tostring(html)则是不全里html的基本写法，补全了缺胳膊少腿的标签。
result=etree.tostring(html)
# 3、获取某个标签的内容(基本使用)，注意，获取a标签的所有内容，a后面就不用再加正斜杠，否则报错。获取某个标签的内容(基本使用)，注意，获取a标签的所有内容，a后面就不用再加正斜杠
# 写法一
html_data = html.xpath('/html/body/div/ul/li/a')
print(html)
for i in html_data:
    print(i.text)
# 写法二
html = etree.HTML(wb_data)
html_data = html.xpath('/html/body/div/ul/li/a/text()')
print(html)
for i in html_data:
    print(i)

# 4、打开读取html文件
#使用parse打开html的文件
html = etree.parse('fang.html')
html_data = html.xpath('//*') #打印是一个列表，需要遍历
print(html_data)
for i in html_data:
    print(i.text)

html = etree.parse('fang.html')
html_data = etree.tostring(html,pretty_print=True)
res = html_data.decode('utf-8')
print(res)



html = etree.parse('fang.html')
html_data = etree.tostring(html,pretty_print=True)
res = html_data.decode('utf-8')
print(res)


# 5、打印指定路径下a标签的属性（可以通过遍历拿到某个属性的值，查找标签的内容）
html = etree.HTML(wb_data)
html_data = html.xpath('/html/body/div/ul/li/a/@href')
for i in html_data:
    print(i)

# 6、我们知道我们使用xpath拿到得都是一个个的ElementTree对象，所以如果需要查找内容的话，还需要遍历拿到数据的列表。
# 　　查到绝对路径下a标签属性等于link2.html的内容。
html = etree.HTML(wb_data)
html_data = html.xpath('/html/body/div/ul/li/a[@href="link2.html"]/text()')
print(html_data)
for i in html_data:
    print(i)

# 7、上面我们找到全部都是绝对路径（每一个都是从根开始查找），下面我们查找相对路径，例如，查找所有li标签下的a标签内容。
html = etree.HTML(wb_data)
html_data = html.xpath('//li/a/text()')
print(html_data)
for i in html_data:
    print(i)

html = etree.HTML(wb_data)
html_data = html.xpath('//li/a[@href="link2.html"]/text()')
print(html_data)
for i in html_data:
    print(i)

# 8、上面我们使用绝对路径，查找了所有a标签的属性等于href属性值，利用的是/---绝对路径，下面我们使用相对路径，查找一下l相对路径下li标签下的a标签下的href属性的值，注意，a标签后面需要双//。
html = etree.HTML(wb_data)
html_data = html.xpath('//li/a//@href')
print(html_data)
for i in html_data:
    print(i)

# 9、相对路径下跟绝对路径下查特定属性的方法类似，也可以说相同。
html = etree.HTML(wb_data)
html_data = html.xpath('//li/a[@href="link2.html"]')
print(html_data)
for i in html_data:
    print(i.text)

html = etree.HTML(wb_data)
html_data = html.xpath('//li/a[@href="link2.html"]/@href')
print(html_data)
for i in html_data:
    print(i)

# 10、查找最后一个li标签里的a标签的href属性
html = etree.HTML(wb_data)
html_data = html.xpath('//li[last()]/a/text()')
print(html_data)
for i in html_data:
    print(i)

# 11、查找倒数第二个li标签里的a标签的href属性
html = etree.HTML(wb_data)
html_data = html.xpath('//li[last()-1]/a/text()')
print(html_data)
for i in html_data:
    print(i)
