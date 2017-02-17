import urllib2
import json

url = "https://api.github.com/repos/scikit-learn/scikit-learn/issues?labels=easy"

resp = urllib2.urlopen(url).read()
json_resp = json.loads(resp)

print type(json_resp)