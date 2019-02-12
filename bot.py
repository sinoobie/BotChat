#!usr/bin/python
#Author: KANG-NEWBIE
'''
jangan nakalin aku kak, aku masih smp:'(

udah open source jangan di recode bangsad!
'''
from fbchat import Client
from fbchat.models import *
from os import system

g=('\033[1;32m')
c=('\033[1;36m')
w=('\033[1;37m')
r=('\033[1;31m')

Q=open('q.txt','r').readlines()
A=open('a.txt','r').readlines()
QA={}
for q,a in zip(Q,A):
	QA[q.replace('\n','').lower()]=a.replace('\n','')


class Main_Client(Client):
	QA=QA
	tol=False
	def onMessage(self,author_id,message_object,thread_id=None,thread_type=ThreadType.USER,**kwargs):
		self.markAsRead(author_id)
		print(message_object)
		if message_object.text==None and len(message_object.attachments)>0:
			self.send(Message(text='''Ngak ngerti.gua djancok!!.'''),thread_id=thread_id,thread_type=thread_type)
		else:
			self.msg=message_object.text
			self.msg=self.msg.lower()
			print(self.msg)

		if author_id != self.uid:
			if self.msg in Main_Client.QA.keys():
				getans=Main_Client.QA.get(self.msg)
				self.messge_send=self.send(Message(text=getans),thread_id=thread_id,thread_type=thread_type)
				Main_Client.tol=True
			else:
				Main_Client.tol=True
				self.messge_send=self.send(Message(text='''Ngak Ngerti Kak:'('''),thread_id=thread_id,thread_type=thread_type)
		self.markAsDelivered(author_id,self.messge_send)

system('clear')
print("""%s
 BOT CHAT%s
 ,_     _‚
 |\\\___//|	%sAuthor: KANG-NEWBIE%s
 |=6   6=|	%sContact: https://t.me/kang_nuubi%s
 \=._Y_.=/	%sGithub: https://github.com/KANG-NEWBIE%s
  )  `  (    ,	%sTEAM: CRABS (t.me/CRABS_ID)%s
 /       \  ((
 |       |   ))
/| |   | |\_//
\| |._.| |/-`
 '"'   '"'
"""%(c,r,g,r,g,r,g,r,g,r))
email=input('%semail or username:%s '%(g,w))
passs=input('%sPassword:%s '%(g,w))
client=Main_Client(email,passs)
client.listen()
