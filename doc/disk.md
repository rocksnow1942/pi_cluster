#### Mount and format disks

```bash
# see the basic info of block devices
lsblk

# see the ID of block devices
blkid

# list more detailed information about disks
sudo fdisk -l

# show all currently mounted disks
mount

# unmount a disk
sudo umount /dev/sda1
```

Example output:

```bash
Disk /dev/sda: 1.82 TiB, 2000365289472 bytes, 3906963456 sectors
Disk model: My Passport 0820
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x6dd77bad

Device     Boot      Start        End    Sectors   Size Id Type
/dev/sda1             2048  335548415  335546368   160G 17 Hidden HPFS/NTFS
/dev/sda2        335548416 1927354367 1591805952   759G af HFS / HFS+
/dev/sda3       1927354368 3059877887 1132523520   540G 17 Hidden HPFS/NTFS
/dev/sda4  *    3059877888 3906963455  847085568 403.9G af HFS / HFS+
```

#### Create partitions on a disk

```bash
sudo fdisk /dev/sda

g # create a new empty GPT partition table

n # add a new partition
# then follow the prompts to create a new partition
# skip some bad sectors if needed

w # write the changes to disk
```

#### Format a partition

```bash
# format a partition to exfat for Windows/Mac compatibility
sudo mkfs.exfat -n "bckup1" /dev/sda1
sudo mkfs.exfat -n "bckup2" /dev/sda2
```

### Mount disks

```bash
# create a mount point; typlically under /mnt or /media
sudo mkdir /mnt/bckup1
sudo mkdir /mnt/bckup2

# mount the partition
sudo mount /dev/sda1 /mnt/bckup1
sudo mount /dev/sda2 /mnt/bckup2

# or mount automatically if in /etc/fstab
mount -a
```

### Check disk usage

```bash
# check disk usage
df -h

# check disk usage (better output)
sudo ncdu /
```

### Auto-mount disks at boot

Disks in `/etc/fstab` will be mounted automatically at boot.

```bash
$ cat /etc/fstab

proc                  /proc           proc    defaults          0       0
PARTUUID=4126e203-01  /boot/firmware  vfat    defaults          0       2
PARTUUID=4126e203-02  /               ext4    defaults,noatime  0       1
```

The fstab file is a system configuration file that contains information about
how disks should be mounted. The file is read by the `mount` command to
determine which options should be used when mounting the specified disk.

The columns in the fstab file are as follows:

1. The device to mount
1. The mount point
1. The filesystem type
1. The mount options
1. The dump option (deprecated)
1. fsck order (0 to disable, 1 to check first, 2 to check after root)

Set mount options to nofail to avoid boot failure if not connected.

```bash
# get the UUID of the disk
sudo blkid

# edit /etc/fstab
sudo nano /etc/fstab

# add the following line to /etc/fstab
# set noatime to disable access time updates, which reduces disk writes
UUID=XXXX-XXXX /mnt/bckup1 exfat defaults,nofail,nodiratime,noatime 0 0
UUID=XXXX-XXXX /mnt/bckup2 exfat defaults,nofail,nodiratime,noatime 0 0

# reload /etc/fstab
sudo systemctl daemon-reload
sudo mount -a
```
