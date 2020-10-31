import numpy as np
import scipy.stats
  
def criticalRange( proportion, nsurveyed ) : 
  # Your code to calculate the critical region should go here
  lower = 
  upper = 
  return lower, upper
  
def hypothesisTest( n_non_uk_birth, proportion, nsurveyed ) : 
  l, u = criticalRange( proportion, nsurveyed )
  # You need to use the l and u values that are returned from the critical range
  # function above within an if statement.  This if statement should decide whether 
  # there is sufficient evidence to reject the null hypothesis.  The code should
  # then return either the statement about the null hypothesis being rejected or
  # the statement about there being insufficient evidence to reject the null 
  # hypothesis form the flowchart.
  
# This variable needs to be set using the information in the statement of the problem
proportion =   
# This variable  needs to be set using the information in the statement of the problem
n_non_uk_birth = 
# This variable  needs to be set using the information in the statement of the problem
nsurveyed = 
print( hypothesisTest( n_non_uk_birth, proportion, nsurveyed ) )
  
