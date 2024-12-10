from ldap3 import Server, Connection, ALL

LDAP_ADDRESS = "ldap://HOST:PORT"  

LDAP_BIND_DN = "cn=CN_,cn=users,dc=DC_,dc=com,dc=tw"
LDAP_BIND_PASSWORD = "PASSWORD"
LDAP_BASE_DN = "dc=DC_,dc=com,dc=tw"


def ldap_login(username, password):
    # connect to LDAP Server
    server = Server(LDAP_ADDRESS, use_ssl=True, get_info=ALL)
    bind_conn = Connection(server, LDAP_BIND_DN, LDAP_BIND_PASSWORD, auto_bind=True)

    search_filter = f"(sAMAccountName={username})"

    # return status True / False
    if not bind_conn.search(LDAP_BASE_DN, search_filter, attributes=['*']):
        print("LDAP Server Searching Error")
        return False

    # check if entry exists
    if len(bind_conn.entries) == 0:
        print(f"User not found for user: {username}")
        return False

    # get user dn to login
    user_dn = bind_conn.response[0]['dn']

    user_conn = Connection(server, user_dn, password, auto_bind=True)
    if user_conn.bind():
        print(f"Authentication Successful for user: {username}")
        return True
    else:
        print(f"Authentication Failed for user: {username}")
        return False


if __name__ == '__main__':

    username = "USERNAME"  
    password = "PASSWORD"  

    if ldap_login(username, password):
        print(f"Login successful for user: {username}")
    else:
        print(f"Login failed for user: {username}")
