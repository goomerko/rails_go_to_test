Rails Go to Test
================

This Sublime 3 plugin derive from https://github.com/sporto/rails_go_to_spec, changing it to work with tests instead of specs.

From a .rb file this plug-in will open the relevant test. If the test doesn't exist it asks if it should be created.

Only supports _test.rb files at the moment.

Installation
------------

Using Sublime Package Control
http://wbond.net/sublime_packages/package_control

Install rails_go_to_test

Usage
-----
- Run from menu > Goto > Rails Go to Test
- Default key binding is command + shift + y
- Or run from command palette 'Rails Go to Test'

Dev
----

git clone git@github.com:goomerko/rails_go_to_test.git RailsGoToTest

Testing
-------

  python resolver_test.py

Acknowledgements
-----------

Thanks to [reInteractive](http://www.reinteractive.net/) for providing the time to work on this.
