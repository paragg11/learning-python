def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.spVoice")
    speak.Speak(str)

if __name__ == '__main__':
    import requests
    import json
    url = "https://newsapi.org/v2/everything?q=tesla&from=2022-03-04&sortBy=publishedAt&apiKey=API_KEY"

    response = requests.get(url)
    text = response.txt
    my_json = json.loads(text)
    for i in range(0,11):
        speak(my_json['articles'][i]['title'])