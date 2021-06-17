import requests
import lxml.html as lh
from Mailing import sendingMail
import os

url = os.environ["URL"]
latestNoticeBackup = ""

# create a handler to handle the contents of the website
page = requests.get(url)

# store the contents of the website under doc
doc = lh.fromstring(page.content)

# Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')

# sanity check
# check the length of the first 5 rows
# result = [len(T) for T in tr_elements[:5]]
# print(result)

# taking the first row second column data i.e. new notice detail
i = 0
col = []
for t in tr_elements[1]:
    i += 1
    newNotice = t.text_content()
    if i == 2:
        break

# storing the new notice if available
if newNotice != latestNoticeBackup:
    latestNoticeBackup = newNotice
    sendingMail(os.environ['SENDER'],os.environ['RECEIVER'] , os.environ['PASSWORD'], latestNoticeBackup)
