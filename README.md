# Owlracle Python
[![Python application](https://github.com/alb2001/owlracle-python/actions/workflows/python-app.yml/badge.svg)](https://github.com/alb2001/owlracle-python/actions/workflows/python-app.yml)
[![Downloads](https://static.pepy.tech/badge/owlracle-python)](https://pepy.tech/project/owlracle-python)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI](https://img.shields.io/pypi/v/owlracle-python)](https://pypi.org/project/owlracle-python/)

A simple Python API wrapper for Owlracle

## Installation

```
pip install owlracle-python
```

## Obtaining API Key
To obtain an API key, you will need to register a new API key on https://owlracle.info/


## Getting Started
To get started, import the package, and initiate a `OwlracleAPI` instance object by passing your API key:
```
from owlracle_python import OwlracleAPI
owlracle = OwlracleAPI(api_key)
```

You can also pass an optional user agent:
```
owlracle = OwlracleAPI(api_key, useragent="User-Agent")
```

Or a different network:
```
owlracle = OwlracleAPI(api_key, network="bsc", useragent="User-Agent")
```

## Queries
Below are a set of queries supported by the [Owlracle API](https://owlracle.info/docs). All data is returned as a Python dictionary for easy data handling.

### Get Gas fee estimation
```
result = owlracle.get_gas_fee_estimation()
print(result)
```

You can also pass the `blocks`, `percentile`, `accept`, `feeinusd`, `eip1559`, `reportwei`, and `calcfrom` parameters:
```
result = owlracle.get_gas_fee_estimation(blocks=500, accept=99)
print(result)
```

### Get Gas history
```
result = owlracle.get_gas_history()
print(result)
```

You can also pass the `from_`, `to`, `candles`, `page`, `timeframe`, `tokenprice`, and `txfee` parameters:
```
result = owlracle.get_gas_history(from_=17849981, to=17949981)
print(result)
```

### Get API key information
By default, the api key supplied on object instance is the one that is checked:
```
result = owlracle.get_api_key_information()
print(result)
```

You can also supply another key to check
```
result = owlracle.get_api_key_information(api_key="randomkey")
print(result)
```

### Get API key credit recharge history
By default, the api key supplied on object instance is the one that is checked:
```
result = owlracle.get_api_key_credit_recharge_history()
print(result)
```

You can also supply another key to check
```
result = owlracle.get_api_key_credit_recharge_history(api_key="randomkey")
print(result)
```

### Get API key usage log
By default, the api key supplied on object instance is the one that is checked:
```
result = owlracle.get_api_key_usage_log()
print(result)
```

You can also supply another key to check
```
result = owlracle.get_api_key_usage_log(api_key="randomkey")
print(result)
```

You can also pass the `fromtime`, `totime`, and `limit` parameters:
```
result = owlracle.get_api_key_usage_log(fromtime=1692462951)
print(result)
```

You can also supply another key to check, while passing the parameters above
```
result = owlracle.get_api_key_usage_log(api_key="randomkey", fromtime=1692462951)
print(result)
```

### Get RPC endpoint
```
result = owlracle.get_rpc_endpoint()
pp.pprint(result)
```

## Testing
A set of tests have been included inside `tests` folder. You will need to setup an environment variable as `OwlracleAPIKey` with your API key

## Chain slugs
These can be obtained from the [API docs](https://owlracle.info/docs), or the `network` attribute using:
```
owlracle.get_rpc_endpoint()
```


## Authors
* [alb2001](https://github.com/alb2001)


## More information
* [owlracle-python on PyPI](https://pypi.org/project/owlracle-python)
* [Owlracle](https://owlracle.info/)
* [Owlracle API](https://owlracle.info/docs)