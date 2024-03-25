#!/bin/bash

curl -H "Authorization: token <ACCESS_TOKEN>" \
     https://api.github.com/orgs/<ORG_NAME>/repos?per_page=20 \
     > repos.json    

 for repo in $(jq -r '.[].ssh_url' repos.json); do 
    git clone $repo
done
    
 

