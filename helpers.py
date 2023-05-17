# Ce fichier est pour des fonctions qui seront utilisés dans le main.py


import re
import unittest

def check_password_validity(password: str) -> bool:
    pw_pattern = r"(?=.*[A-Z]+.*)(?=.*[a-z]+.*)(?=.*[0-9]+.*)(?=.*[^\s]+.*)(?=.*[!@#$%?&*_]+.*).{8,}"
    response = re.search(pw_pattern, password)
    if not response:
        return False
    else:
        return True
    
    
class Tests(unittest.TestCase):
    def test_password_validator(self):
        self.assertEqual(check_password_validity('Maxim Barbe'), False)
        self.assertEqual(check_password_validity('Password2327*'), True)
        self.assertEqual(check_password_validity('Werty1*'), False)
        self.assertEqual(check_password_validity('testPassword*'), False)
        self.assertEqual(check_password_validity('totoBlub1241561*?21'), True)
    
if __name__ == '__main__':
    unittest.main()