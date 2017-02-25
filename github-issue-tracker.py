import urllib2
import json
import datetime as dt
from time import sleep

labels = "easy"
url = "https://api.github.com/repos/scikit-learn/scikit-learn/issues?labels="+labels
begin_time = dt.datetime.utcnow().isoformat()
issues = set()

while True:

	resp = urllib2.urlopen(url).read()
	json_resp = json.loads(resp)
	issue_count = 0


	for data in json_resp:

		if data["number"] in issues:
			continue

		issues.add(data["number"])

		if data["created_at"] > old_time:
			issue_count += 1
			old_time = data["created_at"]

	if issue_count > 0:
		print str(issue_count) + " new issues available"

	sleep(15*60)