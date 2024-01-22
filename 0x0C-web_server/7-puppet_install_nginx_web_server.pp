# Puppet manifest to install and configure Nginx on web server

# Ensure package information is up-to-date
exec { 'update system':
    command => '/usr/bin/apt-get update',
}

# Install Nginx package
package { 'nginx':
	ensure => 'installed',
	require => Exec['update system']
}

# Create a default index.html
file {'/var/www/html/index.html':
	content => 'Hello World!'
}

# Create a redirect
exec {'redirect_me':
	command => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

# Ensure server is running / start server
service {'nginx':
	ensure => running,
	require => Package['nginx']
}
