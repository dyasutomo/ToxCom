#!/bin/bash

#git init .
git add .
git commit -m "m"
heroku login 
heroku git:remote -a toxcom
git push -f heroku master

