# encoding: UTF-8
import re
import urllib2
import urllib

class Reg_test(object):
	#def open_url(url):
	#	return urllib2.urlopen(url).read()
	def get_bing_similar(self,title,content):
		answer_url = "http://cn.bing.com/search?q="+urllib.quote(title+content+"+    -zhidao.baidu.com")
        #answer_url="http://cn.bing.com/search?q=%E8%BF%99%E9%A6%96%E6%AD%8C%E5%8F%AB%E4%BB%80%E4%B9%88%E5%90%8D%E5%AD%97+-zhidao.baidu.com"                                                                                     
		#print answer_url
		msg=urllib2.urlopen(answer_url).read()
		p = re.compile(r'class=" b_goodBadge">最佳答案(.*?)</strong> \.\.\.')
		mstr=p.findall(msg)#.decode('utf-8').encode('utf-8'))                                                                                                                                                                    
		#print msg
		answer=''
		for word in mstr:
			#print word.decode('utf-8')#.encode('utf-8')                                                                                                                                                                         
                                                                                                                                                                                                                                 
			p =re.compile(r'</?\w+[^>]*>')
			filt=p.split(word)
			for chinese in filt:
		            #print chinese.decode('utf-8')
			    answer=answer+chinese
			return answer
#          def get_meta_douban(self,field):
#                  return re.findall(field+':</span>&nbsp;(.*?)\n'.decode('utf-8').encode('utf-8'), msg, re.DOTALL)
                  
                  

if __name__ == "__main__":
	answer_url="http://music.douban.com/subject_search?search_text="+urllib.quote("杨丞琳 左边")

	print answer_url
	msg =urllib2.urlopen(answer_url).read()
	p = re.compile(r'music.douban.com/subject/(.*?)/')

	mstr=p.findall(msg)
	print mstr
        deep_url='http://music.douban.com/subject/'+urllib.quote(mstr[0])
        print deep_url
        msg =urllib2.urlopen(deep_url).read()
        demo=r'    <span class="pl">流派:</span>&nbsp;流行<br />'
        #print msg
        p = re.compile(r'<span class="pl">(.*?)$')
        print p.findall(demo)
        
        #print p_style.findall(msg,re.DOTALL)
        #print msg
        #Reg_test.get_meta_douban("发行时间")
        print re.findall('发行时间:</span>&nbsp;(.*?)\n'.decode('utf-8').encode('utf-8'), msg, re.DOTALL)
        style=re.findall('流派:</span>&nbsp;(.*?)\n'.decode('utf-8').encode('utf-8'), msg, re.DOTALL)
        for word in style:
                print word.decode('utf-8')
        Product_ID=re.findall('条型码:</span>&nbsp;(.*?)\n'.decode('utf-8').encode('utf-8'), msg, re.DOTALL)  
        for word in Product_ID:
                print word.decode('utf-8')
        ISRC=re.findall('ISRC:</span>&nbsp;(.*?)\n'.decode('utf-8').encode('utf-8'), msg, re.DOTALL) 
        for word in ISRC:                                                                               
                print word.decode('utf-8')      
                
        zpk_url='http://www.cavca.org/zpk.php?page=1'
        print zpk_url
        msg=urllib2.urlopen(zpk_url).read()
        print msg
        zpk=re.findall('<td height="40" bgcolor="#F4F4F4">(.*?)</td>'.decode('utf-8').encode('utf-8'), msg, re.DOTALL)
        #print zpk[2].decode('utf-8')
        for meta in zpk:
                print meta.decode('gbk')
