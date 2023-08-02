from datetime import datetime,date
from dateutil.relativedelta import relativedelta

today=datetime.now()
today_refactored = today.strftime("%d/%m/%Y")
six_months = date.today() + relativedelta(months=+6)
six_months_refactored = six_months.strftime("%d/%m/%Y")


class FlightData:
    def serach_url(self):
        search_endpoint = "https://tequila-api.kiwi.com/v2/search"
        return search_endpoint

    def today(self):
        return today_refactored

    def six_month_date(self):
        return six_months_refactored

    def flight_api(self):
        x ={
            "apikey": "QginnzKHTaXtlS_NsCqnrO1COPLEBFr1",
        }

        return x