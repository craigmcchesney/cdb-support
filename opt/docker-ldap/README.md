# traveler-ldap
openladp docker container for traveler development

## The base docker images

https://github.com/osixia/docker-openldap
and https://github.com/osixia/docker-phpLDAPadmin

## Usage

run `docker-compose up` to start the containers. The images will be downloaded and initialize for the first time run.

You can check the state of the openladp service via the php ldap admin web
<https://localhost:6443>

There is a default admin account that you can use to log in
user name: `cn=admin,dc=example,dc=org`
password: `admin`

This admin account will also be used by traveler for ldap interactions.

You can add or modify user records in the web interface easily.

The `seed/traveler.ldif` file will be loaded by the `slapd` when it

You can find the initial users including their uid and password in `seed/traveler.ldif`. 
