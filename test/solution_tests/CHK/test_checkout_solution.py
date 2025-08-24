from solutions.CHK.checkout_solution import CheckoutSolution


class CheckoutSolution():
    def test_checkoutA(self):
        assert CheckoutSolution().checkout('A') == 50
    
    def test_checkoutB(self):
        assert CheckoutSolution().checkout('B') == 30
    
    def test_checkoutC(self):
        assert CheckoutSolution().checkout('C') == 20

    def test_checkoutC(self):
        assert CheckoutSolution().checkout('D') == 15

    def test_checkoutE(self):
        assert CheckoutSolution().checkout('E') == 40
    
    def test_checkoutF(self):
        assert CheckoutSolution().checkout('F') == 10

    def test_checkoutMultiple(self):
        assert CheckoutSolution().checkout('BB') == 45
        assert CheckoutSolution().checkout('AAA') == 130
        assert CheckoutSolution().checkout('AAAAA') == 200
        assert CheckoutSolution().checkout('EEB') == 80
        assert CheckoutSolution().checkout('EE') == 80
        assert CheckoutSolution().checkout('FFF') == 20
        assert CheckoutSolution().checkout('FFFFFF') == 40
        assert CheckoutSolution().checkout('EEBBBAAA') == 255
        assert CheckoutSolution().checkout('HHHHH') == 45
        assert CheckoutSolution().checkout('HHHHHHHHHH') == 80

    def test_illegal_input(self):
        assert CheckoutSolution().checkout('X*') == -1
    
    def test_new_item(self):
        CheckoutSolution().new_item('?',700)
        assert CheckoutSolution().price['?'] == 700
    
    def test_add_offer(self):
        key='3A'
        offer_type=1
        CheckoutSolution().add_offer(offer_type, key, 3, 'A', 130)
        assert key in CheckoutSolution().offers[offer_type]
    
    def test_count_chars(self):
        CheckoutSolution().count_chars('ABBBC')
        counts=CheckoutSolution().counts
        assert counts['A'] == 1
        assert counts['B'] == 3
        assert counts['C'] == 1