# from lib.funding_round import *
# from lib.venture_capitalist import *
from lib.startup import *

# code here
# e.g.
s1 = Startup( 'Pied Piper', 'Richard Hendricks', 'www.pp.com' )
startup1 = Startup("Acme Inc.", "John Smith", "www.hi.com")
startup2 = Startup("Beta Corp.", "Jane Doe", "www.jd.com")
startup3 = Startup("Gamma Co.", "John Smith", "www.bye.com")



Startup.find_by_founder("John Smith")

# if founder_startup:
#     print(f"Found startup '{founder_startup.name}' with founder '{founder_startup.founder}'")
# else:
#     print(f"No startups found with founder name '{founder_name}'")





# do not remove
import ipdb; ipdb.set_trace()
