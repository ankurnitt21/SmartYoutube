# Smart Tube

Smart Tube is a web application that can be used for searching a keyword in a paticular YouTube video that directs you to the portion of the video relevant to your query by conducting speech recognition searches.
***
  
### Installation
***
- Clone repository
```sh
$ git clone https://github.com/ankurnitt21/SmartYoutube.git
```
- Move Inside Folder
```sh
$ cd SmartYoutube
```
- Install libraries
```sh
$ pip install -r requirements.txt
```
```sh
$ python -m pip install --upgrade pytube
```
# Running App
***
```sh
$ python3 app.py
```
***
# Deploying app to Heroku
#### (Assuming You are already logged in through CLI)
```sh
$ heroku create
```
```sh
$ git add .
```
```sh
$ git commit -m 'commit name'
```
```sh
$ git push heroku master
```
***
# Run on Heroku
#### You start by assigning your app some server resources by typing:
```sh
$ heroku ps:scale web=1
```
#### To stop your application, you simply scale it down to zero by typing:

```sh
$ heroku ps:scale web=0
```
