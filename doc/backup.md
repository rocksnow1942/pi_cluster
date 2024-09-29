### Backup and Restore of RPi boot SD card

Raspberry Pi uses a SD card as it's boot drive. The SD card can be suffering
from wear even if enabled wear leveling. It is a good idea to backup the SD card
periodically. The backup can be used to restore the SD card in case of failure.

#### Backup

1. Copy all files in [image_utils](../image_utils) to the RPi.

   ```sh
   rsync -r image_utils hui@pi:~
   ```

1. Make all files executable and owned by root, move to `/usr/local/bin`.

   ```sh
   # assume in /home/hui/image_utils on the pi
   sudo chown root:root image* && sudo chmod 111 image*
   sudo mv image* /usr/local/bin
   ```

1. Prepare an external drive for saving the backup images.
   Refer to [disk.md](./disk.md) for details.

1. After the disk is mounted, run the following to create initial backup.

   ```sh
   # create an initial backup image of the boot SD card, 8GB is extra space
   sudo image-backup --initial /mnt/bckup1/pi4s_bck_1.img,,8000

   # create incremental backups from inital image
   sudo image-backup /mnt/bckup1/pi4s_bck_1.img
   ```

1. Alternatively, save the backup image to a remote server.

   ```sh
   # mount the samba share drive to /media/nas
   sudo mount -t cifs -o username=<user>,password=<password>,vers=2.0 //pinas/nas /media/nas

   # can also add to /etc/fstab to auto-mount
   # /etc/fstab
   //pinas/nas /media/nas cifs username=<user>,password=<password>,vers=2.0,nofail 0 0
   ```

1. To allow incremental backup on a weekly / monthly basis, create copies of the
   initial backup image, then setup cron jobs to run the incremental backup.

   ```bash
   # Create crontab for root user
   $ sudo crontab -e -u root
   # Incremental backups for every day of the week
   0 4 * * 0 image-backup /mnt/bckup1/pi4s_bck_Sun.img
   0 4 * * 1 image-backup /mnt/bckup1/pi4s_bck_Mon.img
   0 4 * * 2 image-backup /mnt/bckup1/pi4s_bck_Tue.img
   0 4 * * 3 image-backup /mnt/bckup1/pi4s_bck_Wed.img
   0 4 * * 4 image-backup /mnt/bckup1/pi4s_bck_Thu.img
   0 4 * * 5 image-backup /mnt/bckup1/pi4s_bck_Fri.img
   0 4 * * 6 image-backup /mnt/bckup1/pi4s_bck_Sat.img
   0 3 1 * * image-backup /mnt/bckup1/pi4s_bck_Monthly.img
   ```

#### Restore

To restore the boot SD card from the backup image, flush the image to the SD card using
`balenaEtcher` or `dd`.

Using `dd`:

```sh
sudo dd if=/mnt/bckup1/pi4s_bck_1.img of=/dev/sda1
```

### References

1. [How to make live backup of your raspberry Pi](https://nerd-tech.net/2022/09/08/how-to-make-a-live-backup-of-your-raspberry-pi-ubuntu-raspberry-pi-os-server-to-create-live-bootable-iso-images-on-an-external-drive/)
