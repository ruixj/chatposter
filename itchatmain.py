import itchat,time
from itchat.content import *
from postlinksdao import *
#import posters.weilele

def printdict(dict):
    for (k,v) in  dict.items():
        print "dict[%s]=" % k,v

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    #printdict(msg.user);
    #msg.user.send('%s: %s' % (msg.type, msg.text))
    if msg['Type'] == SHARING:
        #record = [msg['Text'],msg['Url']]
        print 'record .............: ',msg 
        #postlinksDAO.addLink(record)
        postlinksDAO.addLinkByPost(msg)

    #printdict(msg)
    #value =[msg.text]
    #postlinksDAO.addLink(value)

    

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        msg.user.send(u'@%s\u2005I received: %s' % (
            msg.actualNickName, msg.text))

itchat.auto_login(True)
itchat.run(True)
