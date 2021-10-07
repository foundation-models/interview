from unittest import TestCase, main

from utility import list_to_linked_list

class TestUtility(TestCase):
    
    def test_list_to_linked_list(self):
        print(list_to_linked_list([1,2,3,4,5]))


if __name__ == "__main__":
    main()