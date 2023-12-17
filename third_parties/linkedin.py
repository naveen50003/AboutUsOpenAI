from dotenv import load_dotenv
import os
import requests

load_dotenv()

def scrape_linedin_profile(linkedin_profile_url: str):
  """scrape information from LinkedIn profiles,
  Manually scrape the information from the LinkedIn profile"""
  api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
  headers = {'Authorization': 'Bearer ' + os.environ["LINKEDIN_API_KEY"]}

  # response = requests.get(api_endpoint,
  #                       params={"url": linkedin_profile_url},
  #                       headers=headers)
  
  # KTR
  response = requests.get('https://gist.githubusercontent.com/naveen50003/ae987da32ccbf4597bf7b539ece9fc3e/raw/3cdd62261436b10980ba3ee16dcc643f2af54067/KTR.json') 

  # Navaneeth
  # response = requests.get('https://gist.githubusercontent.com/naveen50003/486402b3bc3c865cefd34b21deed3b2a/raw/929a920f66b89f6dbf6cd2a78a1e73abad1c77d8/navaneeth-karu.json')

  # Harrison Chase
  # response = requests.get('https://gist.githubusercontent.com/naveen50003/e3a79c81905540045996e2d0bea8488b/raw/7abbc46a689351858b360069d6475f569fe807d4/harrison-chase.json')

  # Eden Marco
  # response = requests.get('https://gist.githubusercontent.com/naveen50003/c8fed8a7e1ffcfa7ba0b5f69d06cf72f/raw/dcbcc43f444a13d72e03f3babd3159157e156e9c/eden-marco.json')
  
  """ Clean the empty fields to avoid succeeding Lang chain model(chat GPT) tokes limits=4096 tokes"""

  data = response.json()
  data = {
    k: v
    for k,v in data.items()
    if v not in ([], "", "", None)
      and k not in ["people_also_viewed","certifications"]
  }
  if data.get("groups"):
    for group_dic in data.get("groups"):
      group_dic.pop("profile_pic_url")

  return data

