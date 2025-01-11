import unittest
import subprocess

class TestApp(unittest.TestCase):
    
    def test_hello_world(self):
        # Run the app.py script and capture the output
        result = subprocess.run(['python3', 'app.py'], stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8').strip()
        
        # Check if the output is "Hello, World!"
        self.assertEqual(output, 'Hey Aakash')

if __name__ == '__main__':
    unittest.main()
