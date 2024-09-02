import allure
import pytest

class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that create booking status and booking ID shoud not be null")
    @allure.description("Create a booking from the payload and verify that booking ID shoud not be null & "
                        "status codeshould be 200 for correct payload")

    def test_create_booking_positive(self):
        pass