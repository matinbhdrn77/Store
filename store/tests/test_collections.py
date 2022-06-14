from django.contrib.auth.models import User
from rest_framework import status
import pytest

@pytest.fixture
def authenticate_user(api_client):
    def do_authenticate_user(is_staff):
        return api_client.force_authenticate(user=User(is_staff=is_staff))
    return do_authenticate_user


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_annonymous_returns_401(self, create_collection):
        response = create_collection({'title': 'a'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    def test_if_user_is_not_admin_return_403(self, authenticate_user, create_collection):
        authenticate_user(False)
        response = create_collection({'title': 'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_return_400(self, authenticate_user, create_collection):
        authenticate_user(True)
        response = create_collection({'title': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_return_201(self, authenticate_user, create_collection):
        authenticate_user(True)
        response = create_collection({'title': 'a'})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0