from lib.funding_round import *
from lib.startup import *

class VentureCapitalist:
    all = []
    def __init__(self, name, total_worth):
        self.name = name
        self.total_worth = total_worth
        VentureCapitalist.all.append(self)

    
    def tres_commas_club():
        #returns a list of all v_c instances with more than 
        # 1,000,000,000 total worth

        #if total worth is == or greater than 1,000,000,000, 
        #add it to our list baby!  I think we do this with 
        #setter and getter

        #yes we do bc we are adding validation to our logic :)
        return "rich mfs"
