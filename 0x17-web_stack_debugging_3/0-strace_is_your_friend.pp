# find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet
exec { 'fix-wordpress':
  command => 'sudo sed -i s/class-wp-locale.phpp/class-wp-locale.php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
