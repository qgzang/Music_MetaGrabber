﻿import os 
import io
from mydb import Meta
from mutagen.mp3 import MP3
import mutagen.id3
from mutagen.easyid3 import EasyID3
import sys


#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')#改变标准输出的默认编码  
reload(sys)
sys.setdefaultencoding('utf-8')

meta = Meta()
index_match=0
path = 'F:\\QQmusic\\320K\\waiting' 
#path='D:\\Kuwo_2_2'
for file in os.listdir(path): 
		if file.find('-')>0:
			file_seg=file.split('-')
			song=file_seg[0].decode('gbk').encode('utf-8')
			artist=file_seg[1].decode('gbk').encode('utf-8')
			album=file_seg[2].split('.')[0].decode('gbk').encode('utf-8')
			try:   
    				mp3_path=song+'-'+artist+'.mp3'
    				meta.insert_new(song,artist,album,mp3_path)
    							#print album
    							#meta.update_album_like(album,song,artist)
    							#print index_match
					#newname=match[0]+' - '+match[1]+'.lrc' 
					#os.rename(os.path.join(path,file),os.path.join(path+'\\match\\',newname)) 
					#print match[0],match[1],index_match
					#meta.update_lrc_like(song,artist)					
    			except Exception, e:
        			print e
#2400+中完全一致的1393个
#用了like之后为1572个
#图片match的1008个
#lrc-match的1474
#1320个有专辑信息