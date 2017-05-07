import urllib2
import json
import datetime as dt
import os
import configparser
from time import sleep

labels = "easy"
org = raw_input("Please enter the organization where the repo is hosted: ")
repo = raw_input("Please enter the repo name: ")
labels = raw_input("Enter labels to track: ")
url = "https://api.github.com/repos/" + org + "/" + repo + "/issues?labels=" + labels
begin_time = dt.datetime.utcnow().isoformat()
issues = set()

config = configparser.ConfigParser()
config.read('email-api.conf')
username = config.get('api-data', 'username')
passkey = config.get('api-data', 'passkey')
server = config.get('api-data', 'server')
email_from = config.get('api-data', 'from')
email_to = "Aashil Patel <aashilpatel1993@gmail.com>"
subject = "Github Issue Tracker"

while True:

	resp = urllib2.urlopen(url).read()
	json_resp = json.loads(resp)
	issue_count = 0


	for data in json_resp:

		if data["number"] in issues:
			continue

		issues.add(data["number"])

		if data["created_at"] > begin_time:
			issue_count += 1
			begin_time = data["created_at"]

	if issue_count > 0:

		message = ""

		if issue_count == 1:
			message = str(issue_count) + " new issue available"
		elif issue_count > 1:
			message = str(issue_count) + " new issues available"

		#SQL injection exploits this technique. Should be improved in future
		command = "curl -s --user " + "'" + username+":"+passkey + "' "
		command +=  server + " "
		command += "-F from='"+ email_from + "' "
		command += "-F to='" + email_to + "' "
		command += "-F subject='" + subject + "' "
		command += "-F text='" + message + "'"

		os.system(command)

	sleep(15*60)