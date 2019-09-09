# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/8 0008 19:50'

'''
select方法结合css选择器的使用
'''
from bs4 import BeautifulSoup
from bs4.element import Tag


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


soup = BeautifulSoup(html, "lxml")

# 1、获取所有h3标签（select（））
# h3s = soup.select('h3')
# for h3 in h3s:
#     print(h3)


# 2、获取第二个h3标签
# h3 = soup.select('h3')[1]
# print(h3)


# 3、所有class等于job-title的div标签（单个属性条件）
# job_title = soup.select('div.job-title')
# job_title = soup.select('div[class="job-title"]')
# for title in job_title:
#     print(title)


# 5、获取所有a标签的href属性（先获取a标签，在获取其href）
# aList = soup.select('a')
# for a in aList:
#     href = a['href']
#     print(href)


liList = soup.select('li')[1:]
for li in liList:
    job = {}


    url = li.select('a')[0]['href']  # a标签中的href属性

    datas = list(li.stripped_strings) # 获取li子孙非标签字符串。并删掉空白字符串
    title = datas[0]
    pay_month = datas[1]
    city = datas[2]

    job['职位'] = title
    job['月薪'] = pay_month
    job['城市'] = city

    print(job)

    break