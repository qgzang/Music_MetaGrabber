# -*- coding: utf-8 -*-
import MySQLdb

class BaseDB(object):
    def __init__(self, database=None, user=None, passwd=None, host=None):
        self.database = database if database else 'mysql'
        self.user = user if user else 'root'
        self.passwd = passwd if passwd else '654321'
        #self.host = host if host else '114.243.222.166'#不需要输端口号
        self.host = host if host else 'localhost'

    @property
    def db(self):
        return MySQLdb.connect(self.host, self.user, self.passwd, self.database, charset='utf8')

    @classmethod
    def instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def _execute(self, *args, **kwargs):
        conn = self.db
        cur = conn.cursor()
        cur.execute(*args, **kwargs)
        insert_id = cur.lastrowid
        conn.commit()
        return insert_id
        
    def _query_rows(self, *args):
        cur = self.db.cursor()
        cur.execute(*args)
        return cur.fetchall()

    def test_db(self):
        return self._query_rows('show tables')

class MydbV2(BaseDB):
    def __init__(self):
        BaseDB.__init__(self, database='metadata')

    def insert_data(self, song, artist, language, producer, rights_owner):
        self._execute(r'insert ignore cavca_zpk(song, artist, language, producer, rights_owner) '
                      r'values (%s, %s, %s, %s, %s)', (song, artist, language, producer, rights_owner))

    def insert_song(self, song, artist,album,top):
        self._execute('update meta_test set lyricist = '+lyricist+',composer='+composer+',arrangement='+arrangement+' where song='+song+' and artist='+artist+';'
                      , (song, artist, album,top))

    def insert_lyric(self, lyricist,composer,arrangement,song,artist):
		self._query_rows('update meta set lyricist = '+lyricist+',composer='+composer+',arrangement='+arrangement+' where song='+song+' and artist='+artist)
					  
    def get_id(self, song, artist):
         return self._query_rows('select id from meta where song=%s and artist=%s', (song, artist))

    def update_mp3_path(self,mp3_path,song, artist) :
        self._execute('update meta set mp3_path=%s where song=%s and artist=%s', (mp3_path,song, artist))
    def update_lrc_path(self,lrc_path,song, artist) :
        self._execute('update meta set lyric_path=%s where song=%s and artist=%s', (lrc_path,song, artist))
    def update_cover_path(self,cover_path,song, artist) :
        self._execute('update meta set album_img_path=%s where song=%s and artist=%s', (cover_path,song, artist))

    def get_name(self, song):
        return self._query_rows('select id from meta where song=%s', song)

    def get_zpk(self, song, artist):
        return self._query_rows('select language,producer,rights_owner from cavca_zpk where song=%s and artist=%s', (song, artist))

    def update_zpk(self,languange,producer,rights_owner,song,artist)  :
        self._execute('update meta set language=%s ,producer=%s,rights_owner=%s where song=%s and artist=%s', (languange,producer,rights_owner,song,artist))

    def update_match_name(self,match_name,song) :
        self._execute('update meta set match_name=%s where song=%s', (match_name,song))    

    def updat_song(self, lyricist, composer, arrangement, fxtime, song, artist):
        self._execute('update meta set lyricist=%s, composer=%s, arrangement=%s,album_release=%s where song=%s and artist=%s', (lyricist, composer, arrangement, fxtime,song, artist))
	
