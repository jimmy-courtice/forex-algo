import requests
import constants.defs as defs

class OandaApi:
  def __init__(self) -> None:
    self.session = requests.Session()
    self.session.headers.update({
      "Authorization": f"Bearer {defs.API_KEY}",
      "Content-Type": "application/json"
    })

  def make_request(self, url, verb='get', code=200, params=None, data=None, headers=None):
    full_url = f"{defs.OANDA_URL}/{url}"
    try:
      response = None
      if verb == "get":
        response = self.session.get(full_url, params=params, data=data, headers=headers)
      if response == None:
        return False, {'error': 'verb not found'}
      if response.status_code == code:
        return True, response.json()
      else:
        return False, response.json()
    except Exception as error:
      return False, {'Exception': error}
  
  def get_account_endpoint(self, endpoint, data_key):
    url = f"/accounts/{defs.ACCOUNT_ID}/{endpoint}"
    ok, data = self.make_request(url)
    if ok == True and data_key in data:
      return data[data_key]
    else:
      print("Error get_account_endpoint()", data)
      return None

  def get_account_summary(self):
    return self.get_account_endpoint("summary", "account")
  
  def get_account_instruments(self):
    return self.get_account_endpoint("instruments", "instruments")