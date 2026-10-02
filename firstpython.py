#Display output
print("Hello Rue")


url = "https://api.spacexdata.com/v4/launches/past"

response = requests.get(url)
