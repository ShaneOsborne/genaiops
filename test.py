import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data = {
  "question": "Should I work out?",
  "chat_history": []
}


body = str.encode(json.dumps(data))

url = 'https://rag-1312-endpoint.eastus2.inference.ml.azure.com/score'
# Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Inp4ZWcyV09OcFRrd041R21lWWN1VGR0QzZKMCIsImtpZCI6Inp4ZWcyV09OcFRrd041R21lWWN1VGR0QzZKMCJ9.eyJhdWQiOiJodHRwczovL21sLmF6dXJlLmNvbSIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0L2RhMmM5NDA2LTU1OTEtNDYyMi1hMWM1LWNmYzBiYzBjZTZjZi8iLCJpYXQiOjE3MzQwODU5NDAsIm5iZiI6MTczNDA4NTk0MCwiZXhwIjoxNzM0MDkwOTQ3LCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFlBQUFBQVB0aldCUFVLSW94cTF6S3laOCtmMWI1Y2tYUHlyeVJZRHVnZnR6TGhvdVMvT3cvWnM2bktyZnNvNElSUVQ1VEVuS2pCSXZMYndCVjI5WG5SdlRMeE9jbFNOc05MbTk5ZXJ2MnFKY2xaVEU9IiwiYW1yIjpbInB3ZCIsInJzYSIsIm1mYSJdLCJhcHBpZCI6ImNiMmZmODYzLTdmMzAtNGNlZC1hYjg5LWEwMDE5NGJjZjZkOSIsImFwcGlkYWNyIjoiMCIsImRldmljZWlkIjoiZjM0MGE0OTgtZmYyNy00ZWFjLTk1NWUtYzY4Nzc2YmJjZjRkIiwiZmFtaWx5X25hbWUiOiJBZG1pbmlzdHJhdG9yIiwiZ2l2ZW5fbmFtZSI6IlN5c3RlbSIsImdyb3VwcyI6WyI1NGFjYjY5ZS1iZmUwLTRmNjgtYThiMS02NjJlOGNkMjM4OGUiXSwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiMjAuMTA3LjQ2LjIwOSIsIm5hbWUiOiJTeXN0ZW0gQWRtaW5pc3RyYXRvciIsIm9pZCI6IjBhM2VkMWFlLTlmN2MtNDQ0Ni1hYzFmLTA1YTZhNWQ5MzFmYyIsInB1aWQiOiIxMDAzMjAwMzlGN0Q4NUZFIiwicmgiOiIxLkFiY0FCcFFzMnBGVklrYWh4Y19BdkF6bXoxOXZwaGpmMnhkTW5kY1dOSEVxbkw3OEFDYTNBQS4iLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzdWIiOiIxT3hVOEtsdHZuVjhpUEQzak53dE82NmJxQ0MtWW5RLVI3VnBJZzY5QzZrIiwidGlkIjoiZGEyYzk0MDYtNTU5MS00NjIyLWExYzUtY2ZjMGJjMGNlNmNmIiwidW5pcXVlX25hbWUiOiJhZG1pbkBNbmdFbnZNQ0FQMTU1OTEyLm9ubWljcm9zb2Z0LmNvbSIsInVwbiI6ImFkbWluQE1uZ0Vudk1DQVAxNTU5MTIub25taWNyb3NvZnQuY29tIiwidXRpIjoiRWRSSWluSDJQVVctWnNsU2VzZGpBQSIsInZlciI6IjEuMCIsInhtc19pZHJlbCI6IjEgMTAifQ.qjrKhkRD3WXxUtExwTqi-lnOEqmcvOv_g8HZUm-TkYB6kxOCcVk6BE1ou-qSgP1DKvpuAOZDiEM4ZlZiFAO2OhVcAtjNNha9D6u71YNRVCKeRB5pcKWBmuHRSN-IIon2KSNOzU1lHaif5ud14K91EPWz1lTKBSPC8hZo5zq6dAbfSxdEtdAEq2MecwBu_P2hadLLdvqbruuM5hMP8pfmwmWtKvZOD9rL8bcovqEQBlu-U5TcS0MRvDGa9bAjdEhxEr4ig1HOmrBc_jEipluSBnkUbKx9La4kpf4vHqwEyE_znLfQKs6zmjVbhx59lVxPivJMUTqw_8qRRWJ6HkmHBA'
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))
