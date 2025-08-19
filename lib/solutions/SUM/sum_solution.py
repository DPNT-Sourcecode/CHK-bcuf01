
class SumSolution:
    
    def compute(self, x, y):
        if self.check_type(x,y):
            if self.check_positive(x,y):
                if self.check_upper_limit(x,y):
                    return x+y
    
    def check_type(self, x,y):
        return isinstance(x, int) and isinstance(y,int)    
    
    def check_positive(self, x, y):
        return (x>=0) and (y>=0)
    
    def check_upper_limit(self, x, y):
        return (x<101) and (y<101)

