# Puppet manifest to install and configure Nginx

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Add a line to the Nginx configuration to perform a 301 redirect
file_line { 'nginx_redirect_line':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  require => Package['nginx'],
}

# Create index.html with "Hello World!"
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [Package['nginx'], File['/etc/nginx/sites-available/default']],
}
