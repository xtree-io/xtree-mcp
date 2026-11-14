"""MCP server entry — exposes XTREE API as Agent tools."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from xtree_mcp import api

mcp = FastMCP(
    "xtree",
    instructions=(
        "XTREE 极树 — 新媒体数据服务。"
        "调用工具获取账号、粉丝、内容、音视频、评论等实时原始 JSON 数据（微信搜一搜、视频号、文章互动、历史发文等）。"
        "实时接口（搜一搜/视频号/发文）翻页时必须将上一轮响应 data.session 作为 session 参数回传。"
        "每次响应含 _meta.cost_cny 与 _meta.request_id。"
    ),
)


@mcp.tool()
def account_balance() -> str:
    """查询 API 账户余额（免费，不扣费）。"""
    return api.account_balance()


@mcp.tool()
def wechat_search_articles(keyword: str, page: int = 1, session: str | None = None) -> str:
    """搜一搜：搜索微信公众号文章。翻页时将上一轮 data.session 传入 session。"""
    return api.wechat_search_articles(keyword, page=page, session=session)


@mcp.tool()
def wechat_search_accounts(keyword: str, page: int = 1, session: str | None = None) -> str:
    """搜一搜：搜索微信公众号账号。翻页时将上一轮 data.session 传入 session。"""
    return api.wechat_search_accounts(keyword, page=page, session=session)


@mcp.tool()
def wechat_channels_feeds(
    channel_id: str,
    page: int = 1,
    session: str | None = None,
) -> str:
    """获取指定视频号的作品列表。channel_id 来自搜索或 resolve 接口。"""
    return api.wechat_channels_feeds(channel_id, page=page, session=session)


@mcp.tool()
def wechat_articles_metrics(url: str) -> str:
    """获取微信公众号文章的阅读数、点赞数、在看数等指标。url 为文章链接。"""
    return api.wechat_articles_metrics(url)


@mcp.tool()
def wechat_articles_metrics_pro(url: str) -> str:
    """获取微信公众号文章扩展互动指标（含分享、收藏、评论数等）。url 为文章链接。"""
    return api.wechat_articles_metrics_pro(url)


@mcp.tool()
def wechat_accounts_posts(
    account_id: str,
    page: int = 1,
    cursor: str | None = None,
) -> str:
    """获取公众号历史发文列表。account_id 当前需传 gh_id。翻页回传 data.next_cursor。"""
    return api.wechat_accounts_posts(account_id, page=page, cursor=cursor)


@mcp.tool()
def wechat_accounts_search_by_owner_live(owner_name: str, page: int = 1) -> str:
    """实时主体名下搜号（legacy web_search_owner_mp）。"""
    return api.wechat_accounts_search_by_owner_live(owner_name, page=page)


@mcp.tool()
def wechat_channels_feeds_convert_id(
    export_id: str | None = None,
    object_id: str | None = None,
) -> str:
    """视频号 export_id 与 object_id 互转。至少提供其一。"""
    return api.wechat_channels_feeds_convert_id(export_id=export_id, object_id=object_id)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
