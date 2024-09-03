import allure
import pytest
import logging

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils

class TestCRUDBooking(object):
    @allure.title("Test CRUD operation Update (PUT)")
    @allure.description(
        "Verify that Full Update with the booking ID and Token is working."
    )
    def test_update_booking_id_token(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        put_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = put_requests(
            url=put_url,
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            payload=payload_create_booking(),
            auth=None,
            in_json=False
        )
        # Check response key values
        verify_response_key(response.json().get("firstname"), "Amit")
        verify_response_key(response.json().get("lastname"), "Brown")
        # Check HTTP status code
        verify_http_status_code(response, 200)

    def test_delete_booking_id(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        delete_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = delete_requests(
            url=delete_url,
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            auth=None,
            in_json=False
        )
        verify_response_delete(response.text)
        verify_http_status_code(response, 201)  # Status code for successful delete

