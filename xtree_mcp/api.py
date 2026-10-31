"""XTREE API calls used by MCP tools."""

from __future__ import annotations

from typing import Any

from xtree.client import XTreeClient

from xtree_mcp.format import as_tool_json

_client: XTreeClient | None = None


def get_client() -> XTreeClient:
    global _client
    if _client is None:
        _client = XTreeClient()
    return _client


def reset_client(client: XTreeClient | None = None) -> None:
    global _client
    if _client is not None:
        _client.close()
    _client = client


def _search_body(
    *,
    keyword: str,
    page: int = 1,
    session: str | None = None,
    **extra: Any,
) -> dict[str, Any]:
    body: dict[str, Any] = {"keyword": keyword, "page": page, **extra}
    if session is not None:
        body["session"] = session
    return body


def account_balance(client: XTreeClient | None = None) -> str:
    c = client or get_client()
    return as_tool_json(c.request("GET", "/account/balance"))


def wechat_search_articles(
    keyword: str,
    page: int = 1,
    session: str | None = None,
    *,
    client: XTreeClient | None = None,
) -> str:
    """搜一搜公众号文章。翻页须回传上一轮 data.session。"""
    c = client or get_client()
    body = _search_body(keyword=keyword, page=page, session=session)
    return as_tool_json(c.request("POST", "/wechat/search/articles", json=body))


def wechat_search_videos(
    keyword: str,
    page: int = 1,
    session: str | None = None,
    *,
    client: XTreeClient | None = None,
) -> str:
    c = client or get_client()
    body = _search_body(keyword=keyword, page=page, session=session)
    return as_tool_json(c.request("POST", "/wechat/search/videos", json=body))


def wechat_search_accounts(
    keyword: str,
    page: int = 1,
    session: str | None = None,
    *,
    client: XTreeClient | None = None,
) -> str:
    c = client or get_client()
    body = _search_body(keyword=keyword, page=page, session=session)
    return as_tool_json(c.request("POST", "/wechat/search/accounts", json=body))


def wechat_channels_search(
    keyword: str,
    page: int = 1,
    session: str | None = None,
    *,
    client: XTreeClient | None = None,
) -> str:
    c = client or get_client()
    body = _search_body(keyword=keyword, page=page, session=session)
    return as_tool_json(c.request("POST", "/wechat/channels/search", json=body))


def wechat_channels_feeds(
    channel_id: str,
    page: int = 1,
    session: str | None = None,
    *,
    client: XTreeClient | None = None,
) -> str:
    """视频号作品列表。翻页须回传上一轮 data.session。"""
    c = client or get_client()
    body: dict[str, Any] = {"page": page, "channel_id": channel_id}
    if session is not None:
        body["session"] = session
    return as_tool_json(c.request("POST", "/wechat/channels/feeds/list", json=body))


def wechat_articles_metrics(
    url: str,
    *,
    client: XTreeClient | None = None,
) -> str:
    """获取公众号文章阅读、拇指赞、在看等指标。"""
    c = client or get_client()
    return as_tool_json(c.request("POST", "/wechat/articles/metrics", json={"url": url}))


def wechat_articles_metrics_pro(
    url: str,
    *,
    client: XTreeClient | None = None,
) -> str:
    """获取公众号文章扩展互动指标（含分享、收藏、评论数等）。"""
    c = client or get_client()
    return as_tool_json(c.request("POST", "/wechat/articles/metrics/pro", json={"url": url}))


def wechat_accounts_posts(
    account_id: str,
    page: int = 1,
    cursor: str | None = None,
    *,
    client: XTreeClient | None = None,
) -> str:
    """公众号历史发文列表。翻页须回传上一轮 data.next_cursor。"""
    c = client or get_client()
    body: dict[str, Any] = {"page": page, "account_id": account_id}
    if cursor is not None:
        body["cursor"] = cursor
    return as_tool_json(c.request("POST", "/wechat/accounts/posts/list", json=body))


def wechat_accounts_search_by_owner_live(
    owner_name: str,
    page: int = 1,
    *,
    client: XTreeClient | None = None,
) -> str:
    """实时主体名下搜号（legacy web_search_owner_mp）。"""
    c = client or get_client()
    return as_tool_json(
        c.request(
            "POST",
            "/wechat/accounts/search-by-owner/live",
            json={"owner_name": owner_name, "page": page},
        )
    )


def wechat_channels_feeds_convert_id(
    export_id: str | None = None,
    object_id: str | None = None,
    *,
    client: XTreeClient | None = None,
) -> str:
    """视频号 export_id 与 object_id 互转。"""
    c = client or get_client()
    body: dict[str, Any] = {}
    if export_id is not None:
        body["export_id"] = export_id
    if object_id is not None:
        body["object_id"] = object_id
    return as_tool_json(c.request("POST", "/wechat/channels/feeds/convert-id", json=body))


def wechat_library_search_articles(
    keyword: str,
    page: int = 1,
    page_size: int = 20,
    *,
    client: XTreeClient | None = None,
) -> str:
    """关键词搜索微信文章库（需 ES 灌库）。Phase 2。"""
    c = client or get_client()
    return as_tool_json(
        c.wechat.library.search_articles(keyword, page=page, page_size=page_size)
    )


def wechat_library_search_articles_tokenized(
    keyword: str,
    page: int = 1,
    page_size: int = 20,
    *,
    client: XTreeClient | None = None,
) -> str:
    """分词搜索微信文章库（需 ES 灌库）。Phase 2。"""
    c = client or get_client()
    return as_tool_json(
        c.wechat.library.search_articles_tokenized(
            keyword, page=page, page_size=page_size
        )
    )


def wechat_library_search_accounts(
    keyword: str,
    page: int = 1,
    page_size: int = 20,
    *,
    client: XTreeClient | None = None,
) -> str:
    """关键字查公众号库（需 ES 灌库）。Phase 2。"""
    c = client or get_client()
    return as_tool_json(
        c.wechat.library.search_accounts(keyword, page=page, page_size=page_size)
    )


def wechat_library_accounts_metrics(
    name: str,
    *,
    client: XTreeClient | None = None,
) -> str:
    """获取公众号预估粉丝与指数（需 ES 灌库）。name 为公众号名称。Phase 2。"""
    c = client or get_client()
    return as_tool_json(c.wechat.library.accounts_metrics(name=name))
