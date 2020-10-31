import unittest
import inspect
from main import *

class UnitTests(unittest.TestCase) :
    def test_criticalRange(self) :
        l = scipy.stats.binom.ppf(0.025,100,0.13 )
        u = scipy.stats.binom.ppf(0.975,100,0.13 )
        lll, uuu = criticalRange( 0.13, 100 )
        self.assertTrue( np.abs(l-lll)<1e-4, "the lower bound for the critical region has been computed incorrectly" )
        self.assertTrue( np.abs(u-uuu)<1e-4, "the upper bound for the critical region has been computed incorrectly" )

    def test_variabels(self) : 
        self.assertTrue( proportion==0.13, "the variable proportion has not been set correctly" )
        self.assertTrue( n_non_uk_birth==20, "the variable n_non_uk_birth has not been set correctly" ) 
        self.assertTrue( nsurveyed==100, "the variable nsurveyed has not been set correctly" )

   def test_hypothesisTest(self) : 
       hhh = hypothesisTest( 20, 0.13, 100 ) 
       self.assertTrue( hhh=="there is insufficient evidence to reject the null hypothesis", "the phrase that is returned by your hypothesis test function is incorrect" )
       self.assertTrue( inspect.getsource(hypothesisTest).find("if")>0, "your hypothesis test function does not contain an if statement" )
       self.assertTrue( inspect.getsource(hypothesisTest).find("the null hypothesis is rejected in favour of the alternative")>0, "The hypothesis test function does not contain the string "the null hypothesis is rejected in favour of the alternative."  This string should be present and output when the sample mean falls outside the critical region." )
