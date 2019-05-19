import unittest
import sources
Sources = sources.Sources

class TestSources(unittest.TestCase):
    """
    Text class that defines test cases 
    for the sources class behaviours.
    
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.

    """

    def setUp(self):
        """
        Set up method to create a new_source instance
        before each test cases.
        """
        # self.new_source = Sources("id", name, url, country, description)
        self.new_source = Sources("ABC-Z", "News Cast", "https://www.news-cast.com ", "Kenya", "We provide in depth news from all around Kenya, with a 5 year experience..."  )

    

if __name__ == "__main__":
    unittest.main()