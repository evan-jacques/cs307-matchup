import update_server
import time

last = 0
while True:
	if last < time.time():
		update_server.run()
		last = time.time() + 30
	else:
		time.sleep(10)
