# Kafka examples

This is a little toy example of hooking up python to talk to Kafka and replicate
changes to a property over to a Postgres instance. It is simple and
straightforward. Ansible and virtualbox are used to simulate the various parts
of a larger more complex system. There are three instances that are brought up:
`python`, `kafka` and `postgres`. `python` can be used to publish messages to
`kafka` in a contrived way. `kafka` is a Zookeeper and Kafka combo
box. `postgres` has a Postgres database running on it.



# Go go go

- Do `ansible-galaxy install ANXS.postgresql` to install the Postgres role for ansible. 

- Run `vagrant up`. (Note: This might need to be run three times because of SSH
problems and ansible being unable to find more than one virtualbox at a
time). This takes time but at the end Kafka, Zookeeper and Postgres should be up
and running.

From the root of this directory, execute the following commands in their own sessions:
- `vagrant ssh python` `cd /vagrant/script` `python produce.py`
- `vagrant ssh postgres` `cd /vagrant/script` `python consume.py`
- `vagrant ssh postgres` `psql -U postgres` `select * from props;`

If everything runs correctly, the last command should show the following:
```
postgres=# select * from props;
 id | prop 
----+------
  1 | prop
(1 row)
```

Right now produce is just statically setting the property of a single object. To test a more dynamic situation try the following:
- `vagrant ssh python` `cd /vagrant/script` `python` `import produce` `a= Journaled()` `a.prop="dyn"`
- `vagrant ssh postgres` `cd /vagrant/script` `python consume.py`

The select statement should produce the following:
```
postgres=# select * from props;
 id | prop 
----+------
  1 | dyn
(1 row)
```

So, we can at least get a string to propagate across the system. If you have
other examples of situations you want to see, submit an issue and I'll whip
something up.
