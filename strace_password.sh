 while true ; do sleep 1;  ps -ef | grep ssh | grep priv| awk '{print $2}' | xargs -I '{}'  strace -p {} ; done
