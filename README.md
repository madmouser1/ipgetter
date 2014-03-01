About
=========

This module is designed to fetch your external IP address from the internet.
It is used mostly when behind a NAT.
It picks your IP randomly from a serverlist to minimize request overhead on a single server


API Usage
=========

$ >>> import ipgetter

$ >>> myip = ipgetter.myip()

$ >>> myip

'8.8.8.8'

ChangeLog
=========

0.1 (2014-02-28)
 * You can retrieve your IP.
 * Serverlist = 16 servers
