#!/usr/bin/env sh

###
# $1 is the torrent magnet
# $2 is the telegram token
# $3 is the telegram channel id or channel username

echo 'downloading the file'
aria2c --seed-time=0 --follow-torrent=false $1

echo 'moving file to current dir'
find . -type f -iname '*mp3' -exec mv {} . \;

echo 'executing uploader'
python3 core.py $2 $3

