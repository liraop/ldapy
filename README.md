## LDAPy

A LDAP web interface on Flask, deployed on Docker.

### The idea
This project will enable
* users to change their info;
* users change their password;
* admins to manage general directory objects;
* SSL on client-domain connections;

This project is actually a self-taught attempt to master python development, good practices in python projects and programming in general.
For code style and projects guidelines, I'm following [Google's Python Style Guide](https://google.github.io/styleguide/pyguide.html) as primary source. PEP8 as a secondary one.

### Currently using:
* Flask
* [ldap3](http://ldap3.readthedocs.io/) library

### How to run  
Just `git clone` it then run Docker build to make your own image.
I'm still working on how to get things more useful to general usage.
It's not a priority at the moment, however.
