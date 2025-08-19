from solutions.SUM.sum_solution import SumSolution


class TestSum():
    def test_sum(self):
        assert SumSolution().compute(1, 2) == 3

    def test_integer():
        assert SumSolution().check_type(1,2)
        assert SumSolution().check_type('two', 1.2) == False

    def test_positive():
        assert SumSolution().check_positive(1,2)
        assert SumSolution().check_positive(-1,2) == False 
        assert SumSolution().check_positive(-1,-2) == False

    def test_upper_limit():
        assert SumSolution().check_upper_limit(100,2)
        assert SumSolution().check_upper_limit(101,200)
       