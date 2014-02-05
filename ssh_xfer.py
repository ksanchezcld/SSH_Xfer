# ****************************************#
#  Programa de Transferencia de Archivos  #
#       Ing. Kennedy Sanchez              #
#        (Security + MGP + PS. Auditor)   #
#     @ksanchez_cld on twitter            #  
# **************************************** 	
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paramiko
import os
from sys import stdin

srv = 'SERVER'
prt  = 22
usr = 'USER'
clv = '***'


cnx = paramiko.Transport((srv, prt))
cnx.connect(username = usr, password = clv)

canal = cnx.open_session()
canal.exec_command('mkdir -p /tmp/dir/ && cd /tmp/dir && uptime >>/tmp/dir/uptm.log && hostname >/tmp/dir/host.log')

salida = canal.makefile('rb', -1).readlines()
if salida:
	print salida
else:
	print canal.makefile_stderr('rb', -1).readlines()
cnx.close()
print ('*'*50)
print ('TRANSFIRIENDO ARCHIVOS....')
print ('*'*50)


cnx = paramiko.Transport((srv, prt))
cnx.connect(username = usr, password = clv)

sftp = paramiko.SFTPClient.from_transport(cnx)
archivos = sftp.listdir('/tmp/dir/')
for f in archivos:
  print "Recibiendo ",f
  sftp.get(os.path.join('/tmp/dir/',f),f)
cnx.close()

