from owlracle_python import OwlracleAPI
import pprint

pp = pprint.PrettyPrinter(indent=4)
API_KEY = "YOUR_API_KEY"

owlracle = OwlracleAPI(api_key=API_KEY)

result = owlracle.get_gas_fee_estimation()
pp.pprint(result)

result = owlracle.get_gas_fee_estimation(blocks=500, accept=99)
pp.pprint(result)

result = owlracle.get_gas_history()
pp.pprint(result)

result = owlracle.get_gas_history(from_=17849981, to=17949981)
pp.pprint(result)

result = owlracle.get_api_key_information()
pp.pprint(result)

result = owlracle.get_api_key_information(api_key="randomkey")
pp.pprint(result)

result = owlracle.get_api_key_credit_recharge_history()
pp.pprint(result)

result = owlracle.get_api_key_credit_recharge_history(api_key="randomkey")
pp.pprint(result)

result = owlracle.get_api_key_usage_log()
pp.pprint(result)

result = owlracle.get_api_key_usage_log(fromtime=1692462951)
pp.pprint(result)

result = owlracle.get_api_key_usage_log(api_key="randomkey", fromtime=1692462951)
pp.pprint(result)

result = owlracle.get_rpc_endpoint()
pp.pprint(result)