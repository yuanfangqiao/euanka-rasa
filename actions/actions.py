# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions.WeatherApis import get_weather_by_day

from requests import (
    ConnectionError,
    HTTPError,
    TooManyRedirects,
    Timeout
)


class ActionWeatherForm(Action):

    def name(self) -> Text:
        return "weather_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        address =  tracker.get_slot("address")
        date_time = tracker.get_slot("date_time")

        date_time_number = text_date_to_number_date(date_time)

        if isinstance(date_time_number, str):  # parse date_time failed
            dispatcher.utter_message("暂不支持查询 {} 的天气".format([address, date_time_number]))
        else:
            weather_data = get_text_weather_date(address, date_time, date_time_number)
            dispatcher.utter_message(weather_data)

        return []

def get_text_weather_date(address, date_time, date_time_number):
    try:
        result = get_weather_by_day(address, date_time_number)
    except (ConnectionError, HTTPError, TooManyRedirects, Timeout) as e:
        text_message = "{}".format(e)
    else:
       # text_message_tpl = """
       #     {} {} ({}) 的天气情况为：白天：{}；夜晚：{}；气温：{}~{} °C
       # """

       # text_message = text_message_tpl.format(
       #     result['location']['name'],
       #     date_time,
       #     result['result']['date'],
       #     result['result']['text_day'],
       #     result['result']['text_night'],
       #     result['result']["low"],
       #     result['result']["high"],
       # )
       
       weather = result['result']['text_day']
       if result['result']['text_day'] != result['result']['text_night']:
           weather = result['result']['text_day'] + "转" + result['result']['text_night']

       text_message_tpl = """
            {}{}{},{}到{}摄氏度
        """
       text_message = text_message_tpl.format(
            result['location']['name'],
            date_time,
            weather,
            result['result']["low"],
            result['result']["high"],
        )

    return text_message

def text_date_to_number_date(text_date):
    if text_date == "今天":
        return 0
    if text_date == "明天":
        return 1
    if text_date == "后天":
        return 2



class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self):
        return 'action_default_fallback'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="这个我还不会呢，还需要继续学习！")

        return []
