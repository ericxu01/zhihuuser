# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymssql

class ZhihuuserPipeline(object):
    def process_item(self, item, spider):
        return item
        # if item['text']:
        #     item['text'] = item['text'].replace("'", "‘")
        #     item['tags'] = str(item['tags']).replace("'", "‘")
        #     return item
        # else:
        #     from scrapy.exceptions import DropItem
        #     return DropItem('Missing Text')


class DBPipeline(object):

    def process_item(self, item, spider):


        # # '''
        # # 如果和本机数据库交互，只需修改链接字符串
        # # conn=pymssql.connect(host='.',database='Michael')
        # # '''
        cur = conn.cursor()
        print("insert into [Test].[dbo].[scrapy_quotes20180205]([id] ,[name] ,[url_token] ,[gender] ,[follower_count] ,[headline] ,[articles_count] ,[answer_count]) values('" + str(
            item['id']) + "','" + str(item['name']) + "','" + str(item['url_token']) + "','" + str(
            item['gender']) + "','" + str(item['follower_count'])+ "','" + str(item['headline']) + "','" + str(item['articles_count'])+ "','" + str(item['answer_count']) + "')")
        cur.execute(
            "insert into [Test].[dbo].[scrapy_quotes20180205]([id] ,[name] ,[url_token] ,[gender] ,[follower_count] ,[headline] ,[articles_count] ,[answer_count]) values('" + str(
                item['id']) + "','" + str(item['name']) + "','" + str(item['url_token']) + "','" + str(
                item['gender']) + "','" + str(item['follower_count']) + "','" + str(item['headline']) + "','" + str(
                item['articles_count']) + "','" + str(item['answer_count']) + "')")

        # 提交数据
        conn.commit()
        # 关闭cur
        cur.close()
        # 关闭连接
        conn.close()
        # 将数据以文件费方式存储到本地
        # file = open("autohomeUserInfo.txt", "a")  # 已追加的方式打开文件，不存在则创建
        # file.write(scra)
        # file.write('\n')
        # file.close()
        # print item_string

        return item
