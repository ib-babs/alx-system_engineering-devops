<h1>0x0A. Configuration management</h1>

<blockqoute>
<h3>Background Context</h3>

When I was working for SlideShare, I worked on an auto-remediation tool called <a href="https://intranet.alxswe.com/rltoken/0zbIzBqH_ktMmRQvJwZs2A">Skynet</a> that monitored, scaled and fixed Cloud infrastructure. I was using a parallel job-execution system called MCollective that allowed me to execute commands to one or multiple servers at the same time. I could apply an action to a selected set of servers by applying a filter such as the server’s hostname or any other metadata we had (server type, server environment…). At some point, a bug was present in my code that sent <code>nil</code> to the filter method.

There were 2 pieces of bad news:

When MCollective receives <code>nil</code> as an argument for its filter method, it takes this to mean ‘all servers’
The action I sent was to terminate the selected servers
I started the parallel job-execution and after some time, I realized that it was taking longer than expected. Looking at logs I realized that I was shutting down SlideShare’s entire document conversion environment. Actually, 75% of all our conversion infrastructure servers had been shut down, resulting in users not able to convert their PDFs, powerpoints, and videos… Pretty bad!

Thanks to Puppet, we were able to restore our infrastructure to normal operation in under 1H, pretty impressive. Imagine if we had to do everything manually: launching the servers, configuring and linking them, importing application code, starting every process, and obviously, fixing all the bugs (you should know by now that complicated infrastructure always goes sideways)…

Obviously writing Puppet code for your infrastructure requires an investment of time and energy, but in the long term, it is for sure a must-have.
</blockqoute>
<br><hr>
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/292/4i8il3B.gif" alt="Sylvain Kalache got worked up">
By <bold>Sylvain Kalache</bold>

# Note on Versioning

Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

<i>Install puppet</i>
<code>
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
</code>

You do not need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.
Puppet 5 Docs

<i>Install puppet-lint</i>
`$ gem install puppet-lint`
