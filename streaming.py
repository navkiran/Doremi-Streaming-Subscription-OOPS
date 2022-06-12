from plan import *
from subscription import *
import datetime


FOUR_DEVICE = "FOUR_DEVICE"
TEN_DEVICE = "TEN_DEVICE"

class Streaming:
    def __init__(self) -> None:
        self.start_date = None
        self.subscriptions = []
        self.categories_subscribed = set()
        self.top_up = None
        self.top_up_category = set()
        self.renewal_amount = 0

    def start_subscription(self,start_date):
        try:
            start_date = datetime.datetime.strptime(start_date, DATEFORMAT)
            self.start_date = start_date
        except TypeError as e:
            print("INVALID_DATE")
            

    def get_plan_type(self, streaming_type, plan_text):
        match plan_text:
            case "FREE":
                return FreePlan(streaming_type)
            case "PERSONAL":
                return PersonalPlan(streaming_type)
            case "PREMIUM":
                return PremiumPlan(streaming_type)
             
    def add_subscription(self, streaming_type, plan_text):
        plan = self.get_plan_type(streaming_type, plan_text)
        new_subscription = Subscription(self.start_date, streaming_type, plan)
        if streaming_type in self.categories_subscribed:
            raise Exception("ADD_SUBSCRIPTION_FAILEDDUPLICATE_CATEGORY")
        else:
            self.categories_subscribed.add(streaming_type)
            
        self.renewal_amount += plan.price
        self.subscriptions.append(new_subscription)
        
    def add_topup(self, topup_type, months):
        if topup_type in self.top_up_category:
            raise Exception("ADD_TOPUP_FAILEDDUPLICATE_TOPUP")
        else:
            self.top_up_category.add(topup_type)
            
        charge = 0
        try:
            months = int(months)
        except TypeError as e:
            print("Wrong type for months")
            
        if topup_type == FOUR_DEVICE:
            charge = months*50
        elif topup_type == TEN_DEVICE:
            charge = months*100
            
        self.renewal_amount += charge
        
    def print_renewal_details(self):
        if len(self.subscriptions) == 0:
            raise Exception("SUBSCRIPTIONS_NOT_FOUND")
        
        for sub in self.subscriptions:
            print(f'RENEWAL_REMINDER {sub.streaming_type} {sub.renewal_date.strftime(DATEFORMAT)}')
        
        print(f'RENEWAL_AMOUNT {self.renewal_amount}')    