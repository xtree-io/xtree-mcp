"""MCP library API tests."""

import json

import httpx
import pytest

from xtree.client import XTreeClient
from xtree_mcp import api


def _envelope(data, **meta):
    return {
        "ok": True,
        "data": data,
        "meta": {"request_id": "01JMCP", **meta},
        "error": None,
    }


@pytest.fixture
def mock_client():
    captured = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["method"] = request.method
        captured["path"] = request.url.path
        if request.content:
            captured["body"] = json.loads(request.content.decode())
        return httpx.Response(200, json=_envelope({"items": []}))

    transport = httpx.MockTransport(handler)
    http = httpx.Client(transport=transport, base_url="https://api.xtree.io/api")
    client = XTreeClient(api_key="xt_test", http_client=http)
    return client, captured


def test_wechat_library_search_articles(mock_client):
    client, captured = mock_client
    api.wechat_library_search_articles("AI", page=2, page_size=10, client=client)
    assert captured["path"] == "/api/wechat/library/articles/search"
    assert captured["body"] == {"keyword": "AI", "page": 2, "page_size": 10}


def test_wechat_library_search_articles_tokenized(mock_client):
    client, captured = mock_client
    api.wechat_library_search_articles_tokenized("AI", page=1, page_size=15, client=client)
    assert captured["path"] == "/api/wechat/library/articles/search/tokenized"
    assert captured["body"] == {"keyword": "AI", "page": 1, "page_size": 15}


def test_wechat_library_search_accounts(mock_client):
    client, captured = mock_client
    api.wechat_library_search_accounts("人民日报", page=3, client=client)
    assert captured["path"] == "/api/wechat/library/accounts/search"
    assert captured["body"] == {"keyword": "人民日报", "page": 3, "page_size": 20}


def test_wechat_library_accounts_metrics(mock_client):
    client, captured = mock_client
    api.wechat_library_accounts_metrics("人民日报", client=client)
    assert captured["path"] == "/api/wechat/library/accounts/metrics"
    assert captured["body"] == {"name": "人民日报"}
