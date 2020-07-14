#!/usr/bin/python3
import os, platform, threading, time, socket
from queue import Queue

hostname = socket.gethostname()    
ip_address = socket.gethostbyname(hostname)    
ip_split = ip_address.split('.')
dot = '.'

splitted_ip = ip_split[0] + dot + ip_split[1] + dot + ip_split[2] + dot

operating_system = platform.system()
if (operating_system == "Windows"):
	ping_cmd = "ping -n 1 "
elif (operating_system == "Linux"):
	ping_cmd = "ping -c 1 "
else :
   ping_cmd = "ping -c 1 "

startTime = time.time()
print ("Scanning in Progress:\n")

try:
	def net_scan(address):
		addr = splitted_ip + str(address)
		comm = ping_cmd + addr
		try:
			response = os.popen(comm)
			for line in response.readlines():
				if(line.count("TTL")):
					print("[+] ", addr)
					break
		except:
			pass
	
	def threader():
		while True:
			worker = q.get()
			net_scan(worker)
			q.task_done()
	
	q = Queue()
	startTime = time.time()
	for x in range(100):
		t = threading.Thread(target = threader)
		t.daemon = True
		t.start()
	
	for worker in range(1, 255):
		q.put(worker)
	q.join()
	print('Time taken:', time.time() - startTime)	

except KeyboardInterrupt:
	print("[ - ] Exiting the program. Please wait ...")