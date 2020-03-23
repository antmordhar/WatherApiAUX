import unittest
from llamada import llamada 
import service as service

class TestServiceARIMA(unittest.TestCase):

    def test_llamada(self):
        try:
            llamada(24)
        except ExceptionType:
            self.fail("llamada() raised ExceptionType unexpectedly!")

    def test_index(self):
        response,ok=service.index()
        self.assertEqual(ok, 200)
    def test_vc(self):
        response,ok=service.vc()
        self.assertEqual(ok, 200)
    def test_co(self):
        response,ok=service.co()
        self.assertEqual(ok, 200)
    def test_sd(self):
        response,ok=service.sd()
        self.assertEqual(ok, 200)
    

if __name__ == '__main__':
    unittest.main()