import requests
import json

KEY = 'SjzqFO7Y2uqTnUvUV'  # API key(私钥)
UID = ""  # 用户ID, TODO: 当前并没有使用这个值,签名验证方式将使用到这个值

LOCATION = 'beijing'  # 所查询的位置，可以使用城市拼音、v3 ID、经纬度等
API = 'https://api.seniverse.com/v3/weather/daily.json'  # API URL，可替换为其他 URL
UNIT = 'c'  # 单位
LANGUAGE = 'zh-Hans'  # 查询结果的返回语言


def fetch_weather(location, start=0, days=15):
    result = requests.get(API, params={
        'key': KEY,
        'location': location,
        'language': LANGUAGE,
        'unit': UNIT,
        'start': start,
        'days': days
    }, timeout=2)
    return result.json()


def get_weather_by_day(location, day=1):
    print("location:",location,"day:",day)
    result = fetch_weather(location)
    normal_result = {
        "location": result["results"][0]["location"],
        "result": result["results"][0]["daily"][day]
    }

    return normal_result

if __name__ == '__main__':
    default_location = "深圳"
    result = fetch_weather(default_location)
    print(json.dumps(result, ensure_ascii=False),"\n")

    default_location = "深圳"
    result = get_weather_by_day(default_location,1)
    print(json.dumps(result, ensure_ascii=False))
