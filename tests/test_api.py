"""MCP API helper tests."""

import json

import httpx

from xtree.client import XTreeClient
from xtree_mcp import api
from xtree_mcp.format import as_tool_json


def _envelope(data, **meta):
    return {
        "ok": True,
        "data": data,
        "meta": {"request_id": "01JMCP", **meta},
        "error": None,
    }


def test_as_tool_json_includes_meta():
    transport = httpx.MockTransport(
        lambda r: httpx.Response(200, json=_envelope({"x": 1}, cost_cny=0.5))
    )
    http = httpx.Client(transport=transport, base_url="https://api.xtree.io/api")
    client = XTreeClient(api_key="xt_test", http_client=http)
    raw = api.account_balance(client=client)
    payload = json.loads(raw)
    assert payload["data"]["x"] == 1
    assert payload["_meta"]["cost_cny"] == 0.5
    assert payload["_meta"]["request_id"] == "01JMCP"


def test_wechat_search_videos_path_and_body():
    captured = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["path"] = request.url.path
        captured["body"] = json.loads(request.content.decode())
        return httpx.Response(200, json=_envelope({"items": []}))

    transport = httpx.MockTransport(handler)
    http = httpx.Client(transport=transport, base_url="https://api.xtree.io/api")
    client = XTreeClient(api_key="xt_test", http_client=http)
    api.wechat_search_videos("hello", page=2, session="sess1", client=client)
    assert captured["path"] == "/api/wechat/search/videos"
    assert captured["body"] == {"keyword": "hello", "page": 2, "session": "sess1"}


def test_wechat_accounts_posts_path():
    captured = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["path"] = request.url.path
        captured["body"] = json.loads(request.content.decode())
        return httpx.Response(200, json=_envelope({}))

    transport = httpx.MockTransport(handler)
    http = httpx.Client(transport=transport, base_url="https://api.xtree.io/api")
    client = XTreeClient(api_key="xt_test", http_client=http)
    api.wechat_accounts_posts("gh_363b924965e9", client=client)
    assert captured["path"] == "/api/wechat/accounts/posts/list"
    assert captured["body"]["account_id"] == "gh_363b924965e9"


def test_wechat_channels_feeds_path():
    captured = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["path"] = request.url.path
        captured["body"] = json.loads(request.content.decode())
        return httpx.Response(200, json=_envelope({}))

    transport = httpx.MockTransport(handler)
    http = httpx.Client(transport=transport, base_url="https://api.xtree.io/api")
    client = XTreeClient(api_key="xt_test", http_client=http)
    api.wechat_channels_feeds("ch123", client=client)
    assert captured["path"] == "/api/wechat/channels/feeds/list"
    assert captured["body"]["channel_id"] == "ch123"
