#!/usr/bin/env python


import re
import random
from sys import version_info

PY3K = version_info >= (3, 0)

if PY3K:
    import urllib.request as urllib
else:
    import urllib2 as urllib

__version__ = "0.3.2"


def myip():
    return IPgetter().get_externalip()

class IPgetter(object):
    '''
    This class is designed to fetch your external IP address from the internet.
    It is used mostly when behind a NAT.
    It picks your IP randomly from a serverlist to minimize request overhead
    on a single server
    '''
    
    def __init__(self):
        self.server_list = ['http://ip.dnsexit.com',
                            'http://ifconfig.me/ip',
                            'http://ipecho.net/plain',
                            'http://checkip.dyndns.org/plain',
                            'http://ipogre.com/linux.php',
                            'http://whatismyipaddress.com/',
                            'http://ip.my-proxy.com/',
                            'http://websiteipaddress.com/WhatIsMyIp',
                            'http://getmyipaddress.org/',
                            'http://showmyipaddress.com/',
                            'http://www.my-ip-address.net/',
                            'http://myexternalip.com/raw',
                            'http://www.canyouseeme.org/',
                            'http://www.trackip.net/',
                            'http://myip.dnsdynamic.org/',
                            'http://icanhazip.com/']
        
    def get_externalip(self):
        '''
        This function gets your IP from a random server
        '''
        
        random.shuffle(self.server_list)
        myip = ''
        for server in self.server_list:
            myip = self.fetch(server)
            if myip != '':
                return myip
            else:
                continue
        return ''        
       
    def fetch(self, server):
        '''
        This function gets your IP from a specific server
        '''
        
        opener = urllib.build_opener()
        opener.addheaders = [('User-agent', "Mozilla/5.0")]
        
        try:
            url = opener.open(server)
            content = url.read().decode('utf-8') if PY3K else url.read()
            m = re.search('(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)',content)
            myip = m.group(0)
            return myip if len(myip) > 0 else ''
        except Exception:
            return ''
        finally:
            if url:
                url.close()
        
    def test(self):
        '''
        This functions tests the consistency of the servers on the list when retrieving your IP.
        All results should be the same.
        '''
        
        resultdict = {}
        for server in self.server_list:
            resultdict.update(**{server:self.fetch(server)})
            
        ips = sorted(resultdict.values())
        ips_set = set(ips)
        print('\nNumber of servers: {}'.format(len(self.server_list)))
        print("IP's :")
        for ip, ocorrencia in zip(ips_set, map(lambda x: ips.count(x), ips_set)):
            print('{0} = {1} ocurrenc{2}'.format(ip if len(ip) > 0 else 'broken server', ocorrencia, 'y' if ocorrencia == 1 else 'ies'))
        print('\n') 
        print(resultdict)
