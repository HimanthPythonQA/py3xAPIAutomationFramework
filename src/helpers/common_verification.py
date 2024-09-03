# Common Verification
# HTTP Status Code
# Headers
# Data Verification
# JSON schema

def verify_http_status_code(response_data, expect_data):
    assert response_data.status_code == expect_data, \
        f"Expected status code {expect_data}, but got {response_data.status_code}"



def verify_response_key(key, expected_data):
    assert key == expected_data, \
        f"Expected key value {expected_data}, but got {key}"


def verify_json_key_for_not_null(key):
    assert key is not None, "Failed - Key is None"
    assert key != 0, f"Failed - Key is zero: {key}"
    assert key > 0, f"Failed - Key is not greater than zero: {key}"


def verify_json_key_for_not_null_token(key):
    assert key is not None, "Failed - Token is None"
    assert key != 0, f"Failed - Token is zero: {key}"


def verify_response_key_should_not_be_none(key):
    assert key is not None, "Failed - Response key should not be None"


def verify_response_delete(response):
    assert "Created" in response, \
        f"Expected 'Created' in response, but got {response}"