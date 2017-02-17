import urllib2
import json
import datetime as dt
from time import sleep

labels = "easy"
url = "https://api.github.com/repos/scikit-learn/scikit-learn/issues?labels="+labels
old_time = dt.datetime.utcfromtimestamp(0).isoformat()

while True:

	resp = urllib2.urlopen(url).read()
	json_resp = json.loads(resp)

	new_time = json_resp[0]["created_at"]

	if new_time > old_time:
		old_time = new_time
		print "A new easy issue has been created at "+ old_time

	sleep(60*15)