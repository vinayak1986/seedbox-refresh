#!/bin/bash
rm seedq.sh;
# Change on Mar 31, 2019. Pass arguments to Pythons script if both dates were entered.
if [ -n "$1" -a -n "$2" ]
 then
  python3 seedbox.py $1 $2
else
  python3 seedbox.py
fi
lftp -f seedq.sh;
#unrar e -r the.big.bang.theory.s12e07.internal.720p.web.x264-bamboozle.rar;
#find . -name "*.iso" -exec 7z x -o+ {} \;
#7z x ox_litlwu1dt.iso;
cd /mnt/library/TV;
find . -name "*.rar" -exec unrar x -o+ {} \;
#find . -type f -name "*.rar" -exec rm -f {} \;
find . -type f -name "*.rar" -delete;
find . -type f -name "*.nfo" -exec rm -f {} \;
find . -type f -name "*.sfv" -exec rm -f {} \;
#find . -type f -regex ".+r[0-9]+$" -exec rm -f {} \;
find . -type f -regex ".+r[0-9]+$" -delete;
#find . -regex ".+[Ss]ample.+" -exec rm -rf {} \;
find . -regex ".+[Ss]ample.+" -delete;
find . -regex ".+[Ss]ample$" -exec rm -rf {} \;
cd /mnt/library/Movies;
find . -name "*.rar" -exec unrar x -o+ {} \;
find . -type f -name "*.rar" -exec rm -f {} \;
find . -type f -name "*.nfo" -exec rm -f {} \;
find . -type f -name "*.sfv" -exec rm -f {} \;
find . -type f -regex ".+r[0-9]+$" -exec rm -f {} \;
find . -regex ".+[Ss]ample.+" -exec rm -rf {} \;
find . -regex ".+[Ss]ample$" -exec rm -rf {} \;
cd /mnt/library/Videos;
find . -name "*.rar" -exec unrar x -o+ {} \;
find . -type f -name "*.rar" -exec rm -f {} \;
find . -type f -name "*.nfo" -exec rm -f {} \;
find . -type f -name "*.sfv" -exec rm -f {} \;
find . -type f -regex ".+r[0-9]+$" -exec rm -f {} \;
find . -regex ".+[Ss]ample.+" -exec rm -rf {} \;
cd /mnt/library/Other;
find . -name "*.rar" -exec unrar x -o+ {} \;
find . -name "*.iso" -exec 7z x -o* {} \;
find . -type f -name "*.rar" -exec rm -f {} \;
find . -type f -name "*.iso" -exec rm -f {} \;
find . -type f -name "*.nfo" -exec rm -f {} \;
find . -type f -name "*.sfv" -exec rm -f {} \;
find . -type f -regex ".+r[0-9]+$" -exec rm -f {} \;
find . -regex ".+[Ss]ample.+" -exec rm -rf {} \;
#ls -R | grep -P "\.r\d+$" | xargs -d"\n" rm;
#ls -R | grep -P "\.rar$" | xargs -d"\n" rm;
#ls -R | grep -P "\.nfo$" | xargs -d"\n" rm;
#ls -R | grep -P "\.sfv$" | xargs -d"\n" rm;
#rm -r Sample;
#cd /mnt/library/Movies;
#find . -name "*.rar" -exec unrar x -o+ {} \;
#ls -R | grep -P "\.r\d+$" | xargs -d"\n" rm;
#ls -R | grep -P "\.rar$" | xargs -d"\n" rm;
#ls -R | grep -P "\.nfo$" | xargs -d"\n" rm;
#ls -R | grep -P "\.sfv$" | xargs -d"\n" rm;
#rm -r Sample;
#cd /mnt/library/Videos;
#find . -name "*.rar" -exec unrar x -o+ {} \;
#ls -R | grep -P "\.r\d+$" | xargs -d"\n" rm;
#ls -R | grep -P "\.rar$" | xargs -d"\n" rm;
#ls -R | grep -P "\.nfo$" | xargs -d"\n" rm;
#ls -R | grep -P "\.sfv$" | xargs -d"\n" rm;
#rm -r Sample;
#cd /mnt/library/Other;
#find . -name "*.iso" -exec 7z x -o+ {} \;
#find . -name "*.rar" -exec unrar x -o+ {} \;
#ls -R | grep -P "\.r\d+$" | xargs -d"\n" rm;
#ls -R | grep -P "\.rar$" | xargs -d"\n" rm;
#ls -R | grep -P "\.nfo$" | xargs -d"\n" rm;
#ls -R | grep -P "\.sfv$" | xargs -d"\n" rm;
#ls -R | grep -P "\.iso$" | xargs -d"\n" rm;
#rm -r Sample;
#ls | grep -P "\.r.{2}$" | xargs -d"\n" rm
#ls | grep -P "METCON$" | xargs -d"\n" rm -r
#ls | grep -P "\.sfv$" | xargs -d"\n" rm
#ls | grep -P "\.nfo$" | xargs -d"\n" rm




