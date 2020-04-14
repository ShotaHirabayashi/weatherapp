from django.shortcuts import render
import json
import requests


# Create your views here.


def home(request):

    if request.method == "POST":
        zipcode = request.POST["zipcode"]
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipcode+ "&distance=25&API_KEY=833FDA9A-607E-483A-AAED-AAD1EE733D2B")
        try:
            api = json.loads(api_request.content)
            if api[0]["Category"]["Name"] == "Good":
                categoly_description = "AQI: Good (0 - 50)Air quality is considered satisfactory, and air pollution poses little or no risk."
                c_color = "good"
            elif api[0]["Category"]["Name"] == "Moderate":
                categoly_description = "AQI: Moderate (51 - 100)Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
                c_color = "moderate"
            elif api[0]["Category"]["Name"] == "USG":
                categoly_description = "AQI: Unhealthy for Sensitive Groups (101 - 150)Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
                c_color ="usg"
            elif api[0]["Category"]["Name"] == "Unhralthy":
                categoly_description = "AQI: Unhealthy (151 - 200)Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
                c_color = "unhelthy"
            return render(request,"index.html",{"api":api,"categoly_description":categoly_description,"c_color":c_color})
        except Exception as e:
            api = "Error"
            return render(request,"index.html",{"api":api})

    return render(request,"index.html")



# def home(request):
#     return render(request,"index.html",{})