from lib.venture_capitalist import *
from lib.funding_round import *

class Startup:
    #returns a list of all the startup instances
    all = []
    def __init__(self, name, founder, domain, pivot=100000000):
        self.name = name
        #founder is not allowed to be changed once the startup is instantiated
        self.founder = founder
        #domain is not allowed to be changed once the startup is instantiated
        self._domain = domain
        self.pivot = pivot
       
        Startup.all.append(self)
    
    #method that return the first startup instance whose founders name 
    #matches the arg of a founder's name
    
    @classmethod
    def find_by_founder( cls, founder_name ):
        #if and else statement to find a founder or return 
        #"That is not a startup founder we are familiar with"
        for f in cls.all:
            if f.founder == founder_name:
                return f
        return None
    
    #returns a list of all the different startup domains???  how to do this
    @classmethod
    def domains ( cls ):
        domain_list=[]
        for d in cls.all:
            domain_list.append(d.domain) 

    def get_domain(self): 
        return self._domain
    def set_domain(self, new_domain):
        print("Cannot Change Domain Name")
    domain = property(get_domain, set_domain)
    #do i need setter and getters here?  if so how?????


    

