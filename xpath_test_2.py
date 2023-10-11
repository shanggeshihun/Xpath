# _*_coding:utf-8 _*_
# @Time　　 : 2019/8/26   23:01
# @Author　 : zimo
#@ File　   :xpath_test_2.py
#@Software  :PyCharm

"""
python开发使用XPath条件：
由于XPath属于lxml库模块，所以首先要安装库lxml，具体的安装过程可以查看博客，包括easy_install 和 pip 的安装方法。

XPath的简单调用方法：

from lxml import etree

selector=etree.HTML(源码) #将源码转化为能被XPath匹配的格式

selector.xpath(表达式) #返回为一列表

XPath的使用方法：
首先讲一下XPath的基本语法知识：
四种标签的使用方法
1) // 双斜杠 定位根节点，会对全文进行扫描，在文档中选取所有符合条件的内容，以列表的形式返回。
2) / 单斜杠 寻找当前标签路径的下一层路径标签或者对当前路标签内容进行操作
3) /text() 获取当前路径下的文本内容
4) /@xxxx 提取当前路径下标签的属性值
5) | 可选符 使用|可选取若干个路径 如//p | //div 即在当前路径下选取所有符合条件的p标签和div标签。
6) . 点 用来选取当前节点
7) .. 双点 选取当前节点的父节点
另外还有starts-with(@属性名称,属性字符相同部分)，string(.)两种重要的特殊方法后面将重点讲。
"""
from lxml import etree
html="""
<!DOCTYPE html>
<html>
<head lang="en">
<title>测试</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
<div id="content">
<ul id="ul">
<li>NO.1</li>
<li>NO.2</li>
<li>NO.3</li>
</ul>
<ul id="ul2">
<li>one</li>
<li>two</li>
</ul>
</div>
<div id="url">
<a href="http:www.58.com" title="58">58</a>
<a href="http:www.csdn.net" title="CSDN">CSDN</a>
</div>
</body>
</html>
"""
selector=etree.HTML(html)
# 这里使用id属性来定位哪个div和ul被匹配 使用text()获取文本内容
content=selector.xpath('//div[@id="content"]/ul[@id="ul"]/li/text()')
for i in content:
    print(i)

# 这里使用//从全文中定位符合条件的a标签，使用“@标签属性”获取a便签的href属性值
con=selector.xpath('//a/@href')
for each in con:
    print(each)

# 使用相对路径定位 两者效果是一样的
con=selector.xpath('/html/body/div/a/@title')
print(len(con))
print(con[0])

"""介绍XPath的特殊用法： """
# 1) starts-with 解决标签属性值以相同字符串开头的情况
from lxml import etree
html="""
 <body>
        <div id="aa">aa</div>
        <div id="ab">ab</div>
        <div id="ac">ac</div>
    </body>
"""
selector=etree.HTML(html
# 这里使用starts-with方法提取div的id标签属性值开头为a的div标签
content=selector.xpath('//div[start-with(@id,"a")]/text()')
for each in content:
    print(each)

# 2） string(.) 标签套标签
html="""
<div id="a">
    left
        <span id="b">
        right
            <ul>
            up
                <li>down</li>
            </ul>
        east
        </span>
        west
    </div>
"""
sel=etree.HTML(html)
con=sel.xpath('//div[@id="a"]/text()')
for i in con:
    print(i)

data=sel.xpath('//div[@id="a"]')[0]
info=data.xpath('string(.)')
content=info.replace('\n','').replace(' ','')
for i in content:
    print(i)


# XPath提供的几个特殊的方法：
# XPath中需要取的标签如果没有属性，可以使用text()，posision()来识别标签。


from lxml import etree
html="""
    <div>hello
        <p>H</p>
</div>
<div>hehe</div>
"""
sel=etree.HTML(html)
con=sel.xpath('//div[text()="hello"]/p/text()')
print(con[0])


from lxml import etree
html="""
    <div>hello
        <p>H</p>
        <p>J</p>
        <p>I</p>
</div>
<div>hehe</div>
"""
sel=etree.HTML(html)
con=sel.xpath('//div[text()="hello"]/p[posision()=2]/text()')
print(con)