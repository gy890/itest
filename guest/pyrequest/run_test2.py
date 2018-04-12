import unittest
from guest.pyrequest.interface import *

if __name__ == "__main__":
    suite1 = unittest.TestLoader().loadTestsFromTestCase(AddEventTest)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(AddGuessTest)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(GetEventListTest)
    suite4 = unittest.TestLoader().loadTestsFromTestCase(GetGuestListTest)
    suite5 = unittest.TestLoader().loadTestsFromTestCase(UserSignTest)

    suite = unittest.TestSuite([suite1, suite2, suite3, suite4, suite5])
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
