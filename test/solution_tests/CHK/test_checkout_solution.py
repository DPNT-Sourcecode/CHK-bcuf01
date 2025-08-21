from solutions.CHK.checkout_solution import CheckoutSolution


class CheckoutSolution():
    def test_checkoutA(self):
        assert CheckoutSolution().checkout('A') == 50

    def test_checkoutMultiple(self):
        assert CheckoutSolution().checkout('BB') == 45
        assert CheckoutSolution().checkout('AAA') == 130

       