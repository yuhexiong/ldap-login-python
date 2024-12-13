# LDAP Login

使用 `ldap3` 套件登入 LDAP 的範例，先以 admin 帳密登入 LDAP 後檢驗 username 是否存在於名單中，將使用者資料取出並解析出 DN ，最後以使用者 DN 和密碼登入 LDAP。

## Overview

- 語言: Python v3.12.3
- 套件: ldap3 v2.9.1

## Run

### Env

修改程式內的 LDAP 連線變數：`LDAP_ADDRESS`, `LDAP_BIND_DN`, `LDAP_BIND_PASSWORD`, `LDAP_BASE_DN`  

修改程式內的 登入帳號密碼：`username`, `password`


### Install Module
```bash
pip install ldap3
```

### Run
```bash
python ldap_login.py
```

