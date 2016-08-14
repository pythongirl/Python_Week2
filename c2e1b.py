'''
Determine which version of PySNMP and Paramiko are installed.
'''

#Make sure these exist from python interpreter
import pysnmp
import paramiko

print "Pysnmp version is: ", (pysnmp.__version__)

print "Paramiko version is: ", (paramiko.__version_info__)

