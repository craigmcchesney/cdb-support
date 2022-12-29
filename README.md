# Overview

The cdb-support repo provides tools for managing an ecosystem that includes the [Component Database (CDB)](https://github.com/AdvancedPhotonSource/ComponentDB) and [Traveler](https://github.com/AdvancedPhotonSource/traveler) applications developed at Argonne National Laboratory's [Advanced Photon Source](https://aps.anl.gov/) and Michigan State University's [Facility for Rare Isotope Beams](https://frib.msu.edu/), respectively.

I've installed these applications at several particle accelerator and other large-scale experimental/research facilities, and decided it would be useful to have a common approach and set of tools for administering such an ecosystem.  Currently, I'm deploying servers on AWS Lightsail that include these applications plus supporting services, including:

- Centos 8 stream Linux operating system
- MariaDB relational database service
- MongoDB noSQL datbase service
- shared TLS certificate to enable secure HTTPS protocol across all applications and administrative tools
- [OpenLDAP](https://github.com/osixia/docker-openldap) authentication service
- [phpLDAPadmin](https://github.com/osixia/docker-phpLDAPadmin) for managing LDAP service
- [NGINX](https://www.nginx.com/resources/glossary/nginx/) reverse proxy engine to provide uniform URL interface across all tools and applications and improve security by exposing a single external network port on the application server
- [Payara](https://www.payara.fish/) Java EE application server
- Component Database (CDB) application
- Traveler application
- CDB-Traveler integration via CDB plugin
- web portals for administration of LDAP and Payara services
- Mongo Express web portal providing GUI front-end to MongoDB

## cdb-support and cdb-deployment github repos

I created two github repos to support building these servers.  This repo, cdb-support, contains scripts and other tools intended to be used in all server deployments.  The other, [cdb-deployment](https://github.com/craigmcchesney/cdb-deployment), contains artifacts such as config files that vary between server deployments.

This cdb-support repo contains the following directories:

- bin - Includes scripts for managing the various applications and services, including the cdb and traveler applciations, ldap, mongodb, and mysql. It has scripts for starting and stopping the entire ecosystem and utilities for managing the TLS certificate via "certbot".  I've also begun development of a Python customization tool for configuring a new application server instance.
- sql - Includes some common SQL for initializing a new CDB MySQL database, or manipulating an existing one.
- customization - Includes config file templates with substitution variables as input to the customization tool.
- env - Sets up the user's Linux environment for utilizing the two two repos.
- openldap - Provides docker compose configuration for OpenLDAP and phpLDAPadmin tools.



