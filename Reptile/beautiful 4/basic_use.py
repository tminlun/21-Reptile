# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/8 0008 13:46'

from bs4 import BeautifulSoup

# 测试的文本
html = """
<li>
    <div class="info-primary">
        <h3 class="name">
            <div class="title-box">
                <div class="job-title">名称</div>
                <span class="red">薪资</span>
            </div>
            <div class="info-detail" style="top: 0px;"></div>
        </h3>
        <pid="name">城市<em class="vline"></em>工作年份<em class="vline"></em>学历</p>
    </div>
</li>

<li>
    <a href="/job_detail/faf746a4160291e603Z709-5GFY~.html" data-lid="1cc24d16-0c4e-4c6f-b271-b36e814420f6.brand_jod_list" data-jid="faf746a4160291e603Z709-5GFY~" ka="comp_joblist_1" target="_blank">
        <div class="job-primary">
            <div class="info-primary">
                <h3 class="name">
                    <div class="title-box">
                        <div class="job-title">和平精英-游戏服务器开发工程师</div>
                        <span class="red">21-40K</span>
                    </div>
                    <div class="info-detail" style="top: 0px;"></div>
                </h3>
                <p id="name">深圳<em class="vline"></em>1-3年<em class="vline"></em>本科</p>
            </div>
            <div class="info-publis">
                <h3 class="name">
                    <img src="https://img.bosszhipin.com/beijin/upload/avatar/20190816/ff8d72329e6a3c35670dda11f76f903bd87350801bcb7d5b4d76567f91a7e68f_s.png?x-oss-process=image/resize,w_40,limit_0">
                    王女士<em class="vline"></em>招聘HR
                </h3>
                <p></p>
            </div>
        </div>
    </a>
    <div class="startchat-box">
        <a ka="job-1-chat" href="javascript:;" data-url="/wapi/zpgeek/friend/add.json?jobId=faf746a4160291e603Z709-5GFY~&amp;lid=1cc24d16-0c4e-4c6f-b271-b36e814420f6.brand_jod_list" redirect-url="/web/geek/chat?id=a558589f7d4cc1c603By3tu5GVQ~&amp;lid=1cc24d16-0c4e-4c6f-b271-b36e814420f6.brand_jod_list" class="btn btn-startchat">立即沟通</a>
    </div>
</li>

<li>
    <a href="/job_detail/1d86ef7bc576500303J829-0GFE~.html" data-lid="1cc24d16-0c4e-4c6f-b271-b36e814420f6.brand_jod_list" data-jid="1d86ef7bc576500303J829-0GFE~" ka="comp_joblist_2" target="_blank">
    <div class="job-primary">
    <div class="info-primary">
        <h3 class="name">
            <div class="title-box">
                <div class="job-title">高级运营开发工程师</div>
                <span class="red">20-40K·15薪</span>
            </div>
            <div class="info-detail" style="top: 0px;"><div class="detail-bottom">
    <div class="detail-bottom-title">职位描述</div>
    <div class="detail-bottom-text">
    本科及以上学历，3年以上开发经验； <br>至少熟悉精通1种或多种服务端开发语言：PHP/Go/Python/Java，对于后端框架有理解和开发经验 ；<br>熟悉MYSQL,PG或其他大型数据库，能够快速根据需求完成高性能数据库表设计，有大数据套件经验者更优；<br>熟悉Linux下开发，优秀的编码规范，了解设计模式，熟悉微服务架构和开发，具备高并发服务的开发能力。<br>具有良好的学习能力、沟通能力、服务理念和合作精神，对于项目有owner意识，能够独立承担项目的架构，设计和开发。<br>有以下经验者更优：<br>具有大数据产品研发和数据服务经验者更优； <br>有大型分布式系统设计与开发经验者更优。
    </div>
    <div class="detail-bottom-title">技能要求</div>
    <div class="detail-bottom-labels">
    <span class="detail-bottom-label">PHP</span>
    <span class="detail-bottom-label">Golang</span>
    <span class="detail-bottom-label">Java</span>
    </div>
    </div>
    </div>
        </h3>
        <p>深圳<em class="vline"></em>5-10年<em class="vline"></em>本科</p>
    </div>
    <div class="info-publis">
        <h3 class="name" id="name">
            <img src="https://img.bosszhipin.com/boss/avatar/avatar_14.png?x-oss-process=image/resize,w_40,limit_0">
            金先生<em class="vline"></em>组长
        </h3>
        <p></p>
    </div>
    </div>
    </a>
    <div class="startchat-box">
    <a ka="job-2-chat" href="javascript:;" data-url="/wapi/zpgeek/friend/add.json?jobId=1d86ef7bc576500303J829-0GFE~&amp;lid=1cc24d16-0c4e-4c6f-b271-b36e814420f6.brand_jod_list" redirect-url="/web/geek/chat?id=b6d3f7bc5ff0738803J-2t2-FVQ~&amp;lid=1cc24d16-0c4e-4c6f-b271-b36e814420f6.brand_jod_list" class="btn btn-startchat">立即沟通</a>
    </div>
    </li>

"""

# lxml  解析器（底层由c语言编写，运行速度快）
soup = BeautifulSoup(html, "lxml")

# 打印html
# print(soup.prettify())

# # 1、获取所有h3标签（find_all（元素名，条件））
# h3s = soup.find_all("h3")  # h3s  类型为list
# for h3 in h3s:
#     # h3  类型为Tag：Tag会返回__repr__()，所以返回的是字符串
#     print(h3)
#     print('*'*30)


# # 2、获取第二个h3标签: 只能列表切片获取
# h3 = soup.find_all('h3', limit=2)[1]  # limit=2  获取2个h3标签，再切片拿第2个
# print(h3)


# # 3、所有class等于job-title的div标签（单个属性条件）   attrs
# titles = soup.find_all('div', attrs={'class': 'job-title'})
# for title in titles:
#     print(title)
#     print('*' * 30)

# # 4、所有class等于name，id也等于name的h3标签（多个属性条件）
# h3s = soup.find_all('h3', attrs={'class':'name', 'id':'name'})
# for h3 in h3s:
#     print(h3)
#     print('='*20)


# # 5、获取所有a标签的href属性（先获取a标签，在获取其href）
# aList = soup.find_all('a')
# for a in aList:
#     # 1、通过下标方式（推荐）
#     # href = a['href']
#     # 2、通过attrs获取
#     href = a.attrs['href']
#
#     print(href)


# 6、获取所有职位数据（纯文本）记住：find_all  返回的是list

'''
    步骤：通过stripped_strings（自动去空格）
            1、先变量父标签。再获取其（有用）标签中所有文本（非标签），
            2、放进列表。
            3、最后通过列表索引， 得到对应的数据
'''

# 存储数据
jops = []

lis = soup.find_all('li')[1:]  # 过滤第1个
for li in lis:
    jop = {}
    info_primary = li.find_all('div', attrs={'class': 'info-primary'})

    # 职位
    for info in info_primary:
        # 获取标题、月薪
        name = list(info.find_all('h3')[0].stripped_strings)
        title = name[0]
        job_pay = name[1]
        jop['职位'] = title
        jop['月薪'] = job_pay

        # 获取城市、工作历时、学历
        p = list(info.find_all('p')[0].stripped_strings)

        city = p[0]
        word_year = p[1]
        education = p[2]

        jop['城市'] = city
        jop['工作历时'] = word_year
        jop['学历'] = education

    # 发布人
    info_publis = list(li.find_all('div', attrs={'class': 'info-publis'})[0].stripped_strings)

    author = info_publis[0]
    position = info_publis[1]
    pub_portraits = li.find_all('div', attrs={'class': 'info-publis'})
    for protrait in pub_portraits:
        protrait = protrait.find_all('img')[0]['src']
        jop['发布人的头像'] = protrait

    jop['发布人'] = author
    jop['职位'] = position


    jops.append(jop)

print(jops)

