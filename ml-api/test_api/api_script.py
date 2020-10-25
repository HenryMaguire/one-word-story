# import json
# import time
# import requests
# from lease_term_extractor.config import config
# from urllib3.exceptions import MaxRetryError

# with open(config.DATASETS_PATH / "testing_data" / 'ScheduleOfNoticesOfLeases_357180.json', 'r') as f:
#     schedule_1 = json.load(f)



# try:
#     ti = time.time()
#     url = "http://lease-term-extractor-development.azurewebsites.net/v1/predict/columns_and_lease_terms"

#     response = requests.post(url, json=schedule_1)
#     assert response.status_code ==200
#     assert response.json
#     #print(response.json())

#     response = requests.post(url, json=schedule_2)
#     assert response.status_code ==200
#     assert response.json
#     version = response.json()['version']
#     t = (time.time() - ti)
#     print(f"cloud dev endpoint seems to work in {t:.{6}} seconds with version : {version}")
# except Exception as e:
#     print(e)
#     print("cloud dev endpoint broken")
