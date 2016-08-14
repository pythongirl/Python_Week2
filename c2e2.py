#!/usr/bin/env python
'''
a. Write a script that connects using telnet to the pynet-rtr1 router. Execute the 'show ip int brief' command on the router and return the output.

Try to do this on your own (i.e. do not copy what I did previously). You should be able to do this by using the following items:

telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
remote_conn.read_until(<string_pattern>, TELNET_TIMEOUT)
remote_conn.read_very_eager()
remote_conn.write(<command> + '\n')
remote_conn.close()

'''

import telnetlib
import time
import sys
TELNET_PORT = 23
TELNET_TIMEOUT = 6

def telnet_connection(ip_addr, TELNET_PORT, TELNET_TIMEOUT):

    try:
        return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except:
        sys.exit("Connection timed-out")

def login(remote_conn, username, password):
    remote_conn.read_until('sername', TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    remote_conn.read_until('assword', TELNET_TIMEOUT)
    remote_conn.write(password + '\n')

def send_command(remote_conn, cmd):
    remote_conn.write(cmd + '\n')
    time.sleep(1)
    return remote_conn.read_very_eager()

def main():

    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'

    remote_conn = telnet_connection(ip_addr, 23, 6)

    login(remote_conn, username, password)
    print ("Connection to IP address {} successful!!").format(ip_addr)

    send_command(remote_conn, ('terminal length 0' + '\n'))

    output = send_command(remote_conn, ('show ip int brief' + '\n'))
    print ('\n' + "Show ip interface output is:" + '\n')
    print output  

if __name__ == '__main__':
    main()


