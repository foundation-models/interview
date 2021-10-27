from unittest import TestCase, main


def findCheapestPrice(n, flights, src, dst, k, src_flight = None):
    if n == 0:
        return -1
    if src_flight is not None and src_flight[1] == dst:
        return 0
    if n == 1:
        if flights[0][1] == dst:
            return flights[0][2]
        else:
            return -1
    price = float("inf")
    if k == -1:
        return price
    for flight in flights:
        if flight[0] != src:
            continue
        price = min(price, findCheapestPrice(n-1, flights, flight[1], dst, k-1, flight) + flight[2])
    return price

class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1), 200)
        self.assertEqual(findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0), 500)
        self.assertEqual(findCheapestPrice(n = 1, flights = [[0,1,100]], src = 0, dst = 1, k = 0), 100)
        self.assertEqual(findCheapestPrice(n = 1, flights = [[0,1,100]], src = 0, dst = 0, k = 0), -1)
        self.assertEqual(findCheapestPrice(n = 0, flights = [], src = 0, dst = 1, k = 0), -1)
    
if __name__ == "__main__":
    main()