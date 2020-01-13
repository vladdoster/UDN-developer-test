<div align="center">

# Simple user data ingestions app with DB viewer/updater for UDN

Completed in ~6 hours

### Screenshots

### DB view

![](https://github.com/vladdoster/UDN-developer-test/blob/master/docs/assets/different_users.png)

![](https://github.com/vladdoster/UDN-developer-test/blob/master/docs/assets/search.png)

### Adding new user

![](https://github.com/vladdoster/UDN-developer-test/blob/master/docs/assets/new_user.png)

### Updating existing user using admin pane

![](https://github.com/vladdoster/UDN-developer-test/blob/master/docs/assets/admin.png)

### Admin panel

![](https://github.com/vladdoster/UDN-developer-test/blob/master/docs/assets/admin_overall.png)

</div>

# To run
```shell script
./scripts/run.sh
```
Starts up app and runs migrations if need be. Should need no help.


#### Create superuser to access admin panel
```shell script
./scripts/createsuperuser.sh
```
The nice thing is you can run this as many times as you want and it
cleanly deals with an error if the admin already exists using custom 
management commands

#### Misc. scripts
```shell script
./scripts/something.sh
```
These can be found in /scripts/ and they do more narrow tasks. Run them from the root directory so something
along the lines of 

#### Admin Panel
If you prefer a nicer UI, everything is hooked into the admin panel.

Run
```shell script
./scripts/createsuperuser.sh
```
to get details about credentials.

#### Design Choice
Broke down schema into 3 tables and wrote some custom code to avoid formsets to make POC easier to 
iterate on and helps use easily maintain referential integrity. Also if we wanted to do some analytics on a single table down 
the road, smaller tables to deal and/or less complex query. I would need to turn of CASCADING to maintain referential integrity.

##### DB
Postgresql because of its performance and my familiarity with it. Using Django's ORM abstracts any low-level DB stuff
so it doesn't matter much until we need to scale to multiple nodes / sharding.

##### Docker
Used docker-compose to help me iterate quickly when having to tear up/down things. There is no load-balancer in front, but it
would be trivial to add something like NGINX, Apache, or Caddy.

##### Django
Because batteries are nice.

##### Frontend
I used a mix of vanilla JS, Jquery, and Bootstrap V4. It could look better, but functionality > looks in a rapid POC. Also, I 
know that you all probably have an idea of what you want it to look like.

#### Known TODOs / Bugs
- [x] I need to write the JS to be able to add another input so that environmental exposures and genetic mods. get their own record for 
each issue. I just didnt want to cheap out and write a comma separator function and my solution is more elegant on the backend where
I wouldn't want to be validating data coming in and trying to make sure the delimiter was correct or other random checks. There is one bug where
the text areas arent rendering on the updateParticipantDataView and I couldn't locate it immediately. I will figure it out sometime on 
January 8th, 2020. Other than that... seems to work. Of course I need to write a few sanity unit tests but it seemed like feature creep/out of scope.
A user should be able to delete a participant, but more feature creep?
