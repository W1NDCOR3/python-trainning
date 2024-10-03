import unittest
from app.account_dispatcher import AccountDispatcher



# Mock Account class for testing
class Account:
    def __init__(self, account_id):
        self.id = account_id

class TestAccountDispatcher(unittest.TestCase):

    def setUp(self):
        """This method runs before each test case."""
        self.dispatcher = AccountDispatcher()
        self.test_account = Account(1)

    def test_add_account(self):
        """Test if the account is added successfully."""
        self.dispatcher.add_account(self.test_account)
        self.assertEqual(self.dispatcher.get_account(1), self.test_account)

    def test_get_account(self):
        """Test getting an existing account."""
        self.dispatcher.add_account(self.test_account)
        account = self.dispatcher.get_account(1)
        self.assertEqual(account, self.test_account)

    def test_get_account_raises_exception(self):
        """Test if ValueError is raised for a missing account."""
        with self.assertRaises(ValueError):
            self.dispatcher.get_account(99)

    def test_remove_account(self):
        """Test if the account is removed successfully."""
        self.dispatcher.add_account(self.test_account)
        removed_account = self.dispatcher.remove_account(1)
        self.assertEqual(removed_account, self.test_account)
        # After removing, ensure the account is no longer in the dispatcher
        with self.assertRaises(ValueError):
            self.dispatcher.get_account(1)

    def test_remove_account_raises_exception(self):
        """Test if ValueError is raised for trying to remove a missing account."""
        with self.assertRaises(ValueError):
            self.dispatcher.remove_account(99)

if __name__ == "__main__":
    unittest.main()
