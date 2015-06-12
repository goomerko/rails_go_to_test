# to run
# python resolver_test.py

import unittest
from resolver import *

class ResolverTest(unittest.TestCase):

	def test_is_test_returns_true(self):
		file = '/test/foo/something_test.rb'
		r = Resolver().is_test(file)
		self.assertEqual(r, True)

	def test_is_test_returns_true_for_erb_test(self):
		file = '/test/views/something.html.erb_test.rb'
		r = Resolver().is_test(file)
		self.assertEqual(r, True)

	def test_is_test_returns_false(self):
		file = '/app/foo/something.rb'
		r = Resolver().is_test(file)
		self.assertEqual(r, False)

	def test_is_test_returns_false_for_erb(self):
		file = '/test/views/something.html.erb.rb'
		r = Resolver().is_test(file)
		self.assertEqual(r, False)

	# get_source

	def test_finds_source(self):
		file = '/test/something/foo_test.rb'
		r = Resolver().get_source(file)
		self.assertEqual(len(r), 2)
		self.assertEqual(r[0], '/app/something/foo.rb')
		self.assertEqual(r[1], '/something/foo.rb')

	def test_finds_source_from_erb(self):
		file = '/test/views/namespace/users/_something.html.erb_test.rb'
		r = Resolver().get_source(file)
		self.assertEqual(len(r), 2)
		self.assertEqual(r[0], '/app/views/namespace/users/_something.html.erb')
		self.assertEqual(r[1], '/views/namespace/users/_something.html.erb')

	def test_finds_source_from_haml(self):
		file = '/test/views/documents/update.html.haml_test.rb'
		r = Resolver().get_source(file)
		self.assertEqual(len(r), 2)
		self.assertEqual(r[0], '/app/views/documents/update.html.haml')
		self.assertEqual(r[1], '/views/documents/update.html.haml')

	def test_finds_source_from_lib(self):
		file = '/test/lib/something/foo_test.rb'
		r = Resolver().get_source(file)
		self.assertEqual(len(r), 1)
		self.assertEqual(r[0], '/lib/something/foo.rb')

	# get_test

	def test_finds_test(self):
		file = '/app/models/user.rb'
		r = Resolver().get_test(file)
		self.assertEqual(len(r), 1)
		self.assertEqual(r[0], '/test/models/user_test.rb')

	def test_finds_test_from_lib(self):
		file = '/lib/foo/utility.rb'
		r = Resolver().get_test(file)
		self.assertEqual(len(r), 1)
		self.assertEqual(r[0], '/test/lib/foo/utility_test.rb')

	def test_finds_test_from_erb(self):
		file = '/app/views/users/new.html.erb'
		r = Resolver().get_test(file)
		self.assertEqual(len(r), 1)
		self.assertEqual(r[0], '/test/views/users/new.html.erb_test.rb')

	def test_finds_test_from_haml(self):
		file = '/app/views/account/login.html.haml'
		r = Resolver().get_test(file)
		self.assertEqual(len(r), 1)
		self.assertEqual(r[0], '/test/views/account/login.html.haml_test.rb')

	def test_finds_test_from_other(self):
		file = '/foo/user.rb'
		r = Resolver().get_test(file)
		self.assertEqual(len(r), 1)
		self.assertEqual(r[0], '/test/foo/user_test.rb')

	# run
	# returns either the source or spec depending on the given file

	def test_run(self):
		file = '/app/decorators/namespace/user_decorator.rb'
		r = Resolver().run(file)
		self.assertEqual(len(r), 1)
		self.assertEqual(r[0], '/test/decorators/namespace/user_decorator_test.rb')

	def test_run_from_lib(self):
		file = '/lib/utilities/namespace/foo.rb'
		r = Resolver().run(file)
		self.assertEqual(len(r), 1)
		self.assertEqual(r[0], '/test/lib/utilities/namespace/foo_test.rb')

	def test_run_from_test(self):
		file = '/test/controllers/namespace/foo_controller_test.rb'
		r = Resolver().run(file)
		self.assertEqual(len(r), 2)
		self.assertEqual(r[0], '/app/controllers/namespace/foo_controller.rb')
		self.assertEqual(r[1], '/controllers/namespace/foo_controller.rb')

	def test_run_from_test_lib(self):
		file = '/test/lib/namespace/foo_test.rb'
		r = Resolver().run(file)
		self.assertEqual(len(r), 1)
		self.assertEqual(r[0], '/lib/namespace/foo.rb')

	def test_run_for_erb_test(self):
		file = '/test/views/namespace/users/_new.html.erb_test.rb'
		r = Resolver().run(file)
		self.assertEqual(len(r), 2)
		self.assertEqual(r[0], '/app/views/namespace/users/_new.html.erb')
		self.assertEqual(r[1], '/views/namespace/users/_new.html.erb')

if __name__ == '__main__':
	unittest.main()
