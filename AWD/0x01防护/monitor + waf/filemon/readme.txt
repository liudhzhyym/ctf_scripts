gcc monitor2.c md5.c -o filemonitor
./filemonitor /var/www/html /tmp ���Ը����Ŀ¼


./filemonitor /tmp `find /var/www/html -type d -print | xargs echo` 
����Ŀ¼  ��ǰĿ¼�µ�bak  
./bak/var/www/html
./bak/tmp

---------------------------------------------------------------------------------------------------------
dir='/var/www/html'
rm -rf bak && mkdir bak && mkdir -p ./bak$dir && cp -a $dir/* ./bak$dir 
gcc monitor2.c md5.c -o filemonitor &&./filemonitor `find $dir -type d -print | xargs echo`