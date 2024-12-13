# LDAP Login


**(also provided Traditional Chinese version document [README-CH.md](README-CH.md).)**

An example of logging into LDAP using the `ldap3` library. The process first binds with an admin DN and password to search for the username in the directory. It then retrieves the user data, extracts the user's DN, and finally logs into LDAP using the user's DN and password.

## Overview

- Language: Python v3.12.3
- Library: ldap3 v2.9.1

## Run

### Env

Modify the LDAP connection variables in the script: `LDAP_ADDRESS`, `LDAP_BIND_DN`, `LDAP_BIND_PASSWORD`, `LDAP_BASE_DN`  

Set the username and password in the script: `username`, `password`

### Install Module
```bash
pip install ldap3
```

### Run
```bash
python ldap_login.py
```