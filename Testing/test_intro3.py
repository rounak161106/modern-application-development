class TestExample:
    def compute(self,x,op): #note selected by pytest
        if op=="+":
            return x+1
        elif op=="-":
            return x-1;

    def test_increment(self):
        assert self.compute(5,"+") == 6;
    
    def test_decrement(self):
        assert self.compute(7,"-") == 8;

# even if 2nd class (which is not following naming convention), has a function which follows naming convention, it will not be tested by pytest