from owlracle_python import OwlracleAPI
import pytest
import os


API_KEY = os.getenv("OwlracleAPIKey")


@pytest.fixture
def owlracle_instance():
    owlracle = OwlracleAPI(API_KEY)
    return owlracle

def test_get_gas_fee_estimation(owlracle_instance):
    response = owlracle_instance.get_gas_fee_estimation()

    assert isinstance(response, dict)
    assert isinstance(response["timestamp"], str) 
    assert isinstance(response["lastBlock"], int)
    assert isinstance(response["avgTime"], (int, float))

def test_get_gas_history(owlracle_instance):
    response = owlracle_instance.get_gas_history()

    assert isinstance(response, dict)
    assert isinstance(response["candles"][0]["timestamp"], str)
    assert isinstance(response["candles"][0]["samples"], int)
    assert isinstance(response["candles"][0]["avgGas"], (int, float))

def test_get_api_key_information(owlracle_instance):
    response = owlracle_instance.get_api_key_information()

    assert isinstance(response, dict)
    assert isinstance(response["apiKey"], str)
    assert response["apiKey"] == owlracle_instance._api_key

    response = owlracle_instance.get_api_key_information(api_key="randomnonsense")
    assert isinstance(response, dict)
    assert response["error"]["status"] == 400

def test_get_api_key_credit_recharge_history(owlracle_instance):
    response = owlracle_instance.get_api_key_credit_recharge_history()

    assert isinstance(response, dict)
    assert isinstance(response["recharges"], list)

    response = owlracle_instance.get_api_key_credit_recharge_history(api_key="randomnonsense")
    assert isinstance(response, dict)
    assert response["error"]["status"] == 400

def test_get_api_key_usage_log(owlracle_instance):
    response = owlracle_instance.get_api_key_usage_log()

    assert isinstance(response, dict)
    assert isinstance(response["logs"][0]["network"], str)
    assert response["logs"][0]["network"] == owlracle_instance.network

    response = owlracle_instance.get_api_key_usage_log(api_key="randomnonsense")
    assert isinstance(response, dict)
    assert response["error"]["status"] == 400

def test_get_rpc_endpoint(owlracle_instance):
    response = owlracle_instance.get_rpc_endpoint()

    assert isinstance(response, list)
    assert isinstance(response[0]["network"], str)
    assert response[0]["network"] == owlracle_instance.network