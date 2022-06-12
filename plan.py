import datetime
from dateutil.relativedelta import relativedelta

MUSIC = "MUSIC"
VIDEO = "VIDEO"
PODCAST = "PODCAST"

class Plan:
    def __init__(self) -> None:
        self.duration = None
        self.price = None
        self.streaming_type = None
        
    def get_price(self):
        pass
    

class FreePlan(Plan):
    def __init__(self, streaming_type) -> None:
        self.duration = relativedelta(months=1)
        self.price = self.get_price(streaming_type)
    
    def get_price(self, streaming_type):
        if streaming_type in [MUSIC, VIDEO, PODCAST]:
            return 0
        else:
            raise ValueError("Acceptable values for plan streaming_type: MUSIC, VIDEO, PODCAST")
        
class PersonalPlan(Plan):
    def __init__(self, streaming_type) -> None:
        self.duration = relativedelta(months=1)
        self.price = self.get_price(streaming_type)
    
    def get_price(self, streaming_type):
        if streaming_type == MUSIC:
            return 100
        elif streaming_type == VIDEO:
            return 200
        elif streaming_type == PODCAST:
            return 100
        else:
            raise ValueError("Acceptable values for plan streaming_type: MUSIC, VIDEO, PODCAST")
        
class PremiumPlan(Plan):
    def __init__(self, streaming_type) -> None:
        self.duration = relativedelta(months=3)
        self.price = self.get_price(streaming_type)
    
    def get_price(self, streaming_type):
        if streaming_type == MUSIC:
            return 250
        elif streaming_type == VIDEO:
            return 500
        elif streaming_type == PODCAST:
            return 300
        else:
            raise ValueError("Acceptable values for plan streaming_type: MUSIC, VIDEO, PODCAST")
        