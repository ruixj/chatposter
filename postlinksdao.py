 # -*- coding: utf-8 -*-
#import MySQLdb  
import urllib
import urllib2
import json

class postlinksDAO:
    url = 'http://www.microlele.com:8080/seckill/postlinks/postlink'
    def __init__(self):
        pass

#    @staticmethod
#    def addLink(value):
#        try:  
#            conn = MySQLdb.connect(host='localhost',user='root',passwd='root',port=3306)  
#            conn.set_character_set('utf8')
#            cur = conn.cursor()  
          
#            conn.select_db('seckill')  
          
            #value = ['http://http://blog.csdn.net/acdreamers/article/details/21186457']  
#            cur.execute('insert into post_links(title,link_name) values(%s,%s)',value)  
          
#            conn.commit()  
#            cur.close()  
#            conn.close()  

#        except MySQLdb.Error,msg:  
#            print "MySQL Error %d: %s" %(msg.args[0],msg.args[1])  
    @staticmethod
    def addLinkByPost(recorddict):
        try:  
            postdata = {}
            postdata['title']     = recorddict['Text']
            postdata['linkName'] = recorddict['Url']

            encodedata = urllib.urlencode(postdata,'utf-8')

            jdata = json.dumps(postdata)  
            print jdata
            headers = {"Content-type":"application/json","Accept": "application/json"}  
            req   = urllib2.Request(postlinksDAO.url, jdata,headers) 
            #req   = urllib2.Request(url, encodedata) 
            response = urllib2.urlopen(req)   
            res = response.read()
            print res
        except urllib2.HTTPError,e:
            print "The server couldn't fulfill the request"
            print "Error code:",e.code
            print "Return content:",e.read()
        except urllib2.URLError,e:
            print e.reason



if __name__ == "__main__" :
    value = ['http://http://blog.csdn.net/acdreamers/article/details/21186457']
    #postlinksDAO.addLink(value)
    linkrecord = {}
    linkrecord['Text'] = u'我的文章'
    linkrecord['Url']  = u'www.baidu.com'

    postlinksDAO.addLinkByPost(linkrecord)
    
