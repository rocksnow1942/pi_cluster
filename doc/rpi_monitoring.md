### CMDs to monitor the Raspberry Pi

```bash
# check the CPU temperature
vcgencmd measure_temp
# temp=62.0'C

# check the CPU frequency
vcgencmd measure_clock arm
# frequency(45)=600117184

# check the GPU frequency
vcgencmd measure_clock core
# frequency(0)=500007584

# check the CPU voltage
vcgencmd measure_volts
# volt=0.7200V

# check the GPU voltage
vcgencmd measure_volts core

# check the memory usage
free -h
#               total        used        free      shared  buff/cache   available
#Mem:           7.9Gi       811Mi       5.5Gi       355Mi       2.0Gi       7.1Gi
#Swap:          199Mi          0B       199Mi

# check the disk usage
df -h

# check fan speed
cat /sys/devices/platform/cooling_fan/hwmon/*/fan1_input
# 5431

# Check S.M.A.R.T. status of the disk
# first install smartmontools
sudo apt-get install smartmontools
# then check the status
sudo smartctl -a /dev/sda
```

Test system properties:

```bash
# test SD card speed
# https://forums.raspberrypi.com/viewtopic.php?t=31925
# test write speed:
sync; echo 3 | sudo tee /proc/sys/vm/drop_caches
dd if=/dev/zero of=~/test.tmp bs=500K count=1024
# 524288000 bytes (524 MB, 500 MiB) copied, 27.6649 s, 19.0 MB/s

# test read speed:
sync; echo 3 | sudo tee /proc/sys/vm/drop_caches
dd if=~/test.tmp of=/dev/null bs=500K count=1024
# 524288000 bytes (524 MB, 500 MiB) copied, 6.14367 s, 85.3 MB/s
```
