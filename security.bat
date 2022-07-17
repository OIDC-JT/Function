#!/bin/bash 
setsebool -P antivirus_can_scan_system 1 
yum install -y epel-release 
yum install -y clamav-server clamav-data clamav-update clamav-filesystem clamav clamav-scanner-systemd clamav-devel clamav-lib clamav-server-systemd 
cp /usr/share/doc/clamd.conf /etc/clamd.d/ 
sed -i -e "s/^Example/#Example/" /etc/clamd.d/clamd.conf 
sed -i -e "s/^Example/#Example/" /etc/clamd.d/scan.conf 
sed -i -e "s/^Example/#Example/" /etc/freshclam.conf 
freshclam 
echo "[Unit]" >> /usr/lib/systemd/system/clam-freshclam.service 
echo "Description = freshclam scanner" >> /usr/lib/systemd/system/clam-freshclam.service 
echo "After = network.target" >> /usr/lib/systemd/system/clam-freshclam.service 
echo "[Service]" >> /usr/lib/systemd/system/clam-freshclam.service 
echo "Type = forking" >> /usr/lib/systemd/system/clam-freshclam.service 
echo "ExecStart = /usr/bin/freshclam -d -c 4" >> /usr/lib/systemd/system/clam-freshclam.service 
echo "Restart = on-failure" >> /usr/lib/systemd/system/clam-freshclam.service 
echo "PrivateTmp = true" >> /usr/lib/systemd/system/clam-freshclam.service 
echo "RestartSec = 20sec" >> /usr/lib/systemd/system/clam-freshclam.service 
echo "[Install]" >> /usr/lib/systemd/system/clam-freshclam.service 
echo "WantedBy=multi-user.target" >> /usr/lib/systemd/system/clam-freshclam.service 
systemctl enable clam-freshclam 
systemctl enable clamd@scan 
systemctl start clam-freshclam 
systemctl start clamd@scan 
systemctl status clam-freshclam 
systemctl status clamd@scan 
echo "#!/bin/sh" >> /usr/local/bin/clamscan.sh 
echo "SDATE=$(date "+%%Y-%%m-%%d %%H:%%M:%%S")" >> /usr/local/bin/clamscan.sh 
echo "echo $'\n\nStart Date :' $SDATE >> /root/text.txt" >> /usr/local/bin/clamscan.sh 
echo "clamscan -ri / >> /root/text.txt" >> /usr/local/bin/clamscan.sh 
chmod 755 /usr/local/bin/clamscan.sh 
cat <(crontab -l) <(echo "00 04 * * * /usr/local/bin/clamscan.sh") | crontab -
