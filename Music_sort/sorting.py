from mutagen.mp3 import MP3
import mutagen.id3
from mutagen.easyid3 import EasyID3
EasyID3.valid_keys["comment"]="COMM::'XXX'"

id3info  = MP3("Adam Lambert - Whataya Want From Me.mp3.mp3", ID3=EasyID3)
for k, v in id3info.items():
    print k,v 