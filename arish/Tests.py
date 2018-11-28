
import Assign3
import unittest
# test created by Arish Kakadiya
class TestProject(unittest.TestCase):

    def test_showNumRows(self):
        print("Test made by Arish Kakadiya")
        data = Assign3.DataReader("32100054.csv")
        dList = data.rowList()
        self.assertTrue(Assign3.showNumRows(dList), 30559)


if __name__ == '__main__':
        unittest.main()