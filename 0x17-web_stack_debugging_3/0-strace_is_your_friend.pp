# Fix for Apache 500 error

exec { 'fix_apache_500_error':
  command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
