### Auto create database from form registry Account

### Auto create user follow form after create database

### Auto config ssl using `certbot`
#### method:
  + drop the custom_module `base_` to the target server (i will call it server A) you want auto config ssl certbot.
  + drop the `registry_account module` to the second server you want have registry page (server B).
  + config the url ip to your server ip andress in config.py (registry_account/config.py)
  + activate `base_` in server A.
  + activate `registry_account` in server B.

### Auto config nginx to add certificate

### Auto add user registry information to target database for tracking 

