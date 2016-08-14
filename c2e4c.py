#!/usr/bin/env python

'''
Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and prints out both the MIB2 sysName and sysDescr.
'''

from snmp_helper import snmp_get_oid, snmp_extract

list_ips = ['184.105.247.70', '184.105.247.71']

def main():

    for ip in (list_ips):  
        sysName_OID = '1.3.6.1.2.1.1.5.0'
        sysDescr_OID = '1.3.6.1.2.1.1.1.0'
        community_string = 'galileo'
        snmp_port = '161'      
        a_device = (ip, community_string, snmp_port)
            
        snmp_name_data = snmp_get_oid(a_device, oid = sysName_OID)
        snmp_descr_data = snmp_get_oid(a_device, oid = sysDescr_OID)
        print "#################"
        print "\nFor IP {}: ".format(ip) + '\n' 
        print "SNMP NAME MIB OID IS: \n", (snmp_extract(snmp_name_data))   
        print "\nSNMP DESCRP MIB OID IS: \n", (snmp_extract(snmp_descr_data))

if __name__ == "__main__":
    main()
    
