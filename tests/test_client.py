from unittest.mock import patch, Mock
from app.client import fetch_animals_page, post_animals_batch


def test_fetch_animals_page_returns_items():
    with patch("app.client.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"items": [{"id": 1, "name": "Dog"}]}

        result = fetch_animals_page(1)
        assert result == [{"id": 1, "name": "Dog"}]


def test_post_animals_batch_handles_retries():
    with patch("app.client.requests.post") as mock_post:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = '{"message": "Helped 1 find home"}'

        mock_post.side_effect = [
            Exception("timeout"),
            Exception("502 Bad Gateway"),
            mock_response,
        ]

        success = post_animals_batch([{"id": 123, "name": "Cat"}])
        assert success is True
        assert mock_post.call_count == 3
