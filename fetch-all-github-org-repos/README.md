## Description

A simple script to fetch all the repositories from an organization.

---

## Script logic

## Step 1

Fetch all the repositories information and store it to a json file. You will need an access token for that. To
generate the token, go to the link: https://github.com/settings/tokens. Then, click on 'generate a new token'.
You can use the classic way. Provide the `repo` permission. A token will be generated. Copy it and paste it to the
script.

## Step 2

Iterate through the array of json objects from the json file and git clone the ssh url.

---

Thank you
