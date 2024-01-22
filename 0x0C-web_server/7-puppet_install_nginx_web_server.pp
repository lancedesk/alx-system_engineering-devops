$default_file = 'https://raw.githubusercontent.com/lancedesk/alx-system_engineering-devops/master/0x0C-web_server/default'
$default_file_location = '/etc/nginx/sites-available/default'

# Ensure package information is up-to-date
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
}

# Install Nginx package
package { 'nginx':
  ensure  => installed,
  require => Exec['apt-update'],
}

# Create a default index.html
file { 'Create index.html':
  require => Package['nginx'],
  path    => '/var/www/html/index.html',
  content => 'Hello World!\n',
}

# Create a default 404 error page
file { 'Create 404.html':
  require => Package['nginx'],
  path    => '/var/www/html/404.html',
  content => 'Ceci n\'est pas une page\n',
}

# Configure Nginx main configuration file and restart Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  require => Package['nginx'],
  notify  => Service['nginx'],
  content => file($default_file),
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
