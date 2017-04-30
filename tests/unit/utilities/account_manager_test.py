# -*- coding: utf-8 -*-
"""Test cases for UI.utilities.account_manager.AccountManager package."""

import unittest

from UI.utilities.account_manager import AccountManager


class AccountManagerTestCase(unittest.TestCase):

    def test_init(self):
        expected_login = 'user@example.com'
        expected_password = 'secret'

        result = AccountManager(expected_login, expected_password)

        assert expected_login == result.login_email
        assert expected_password == result.password
