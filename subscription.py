
from plan import *

DATEFORMAT = "%d-%m-%Y"
NOTIFICATIONBUFFER = 10

class Subscription:
    def __init__(self, streaming_start, streaming_type, plan) -> None:
        self.renewal_date = self.get_renewal_date(streaming_start, plan)
        self.streaming_type = streaming_type      
    
    def get_renewal_date(self, streaming_start, plan):
        rd = streaming_start + plan.duration - datetime.timedelta(days=NOTIFICATIONBUFFER)
        return rd
        
    