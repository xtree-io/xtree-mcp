# -*- coding: utf-8 -*-
"""MCP tool registry - keep in sync with server.py @mcp.tool names."""

from __future__ import annotations

# (tool_name, slug)
MCP_TOOLS: list[tuple[str, str]] = [
    ("account_balance", "account.balance"),
    ("wechat_search_articles", "wechat.search.articles"),
    ("wechat_search_videos", "wechat.search.videos"),
    ("wechat_search_accounts", "wechat.search.accounts"),
    ("wechat_channels_search", "wechat.channels.search"),
    ("wechat_channels_feeds", "wechat.channels.feeds"),
    ("wechat_channels_feeds_convert_id", "wechat.channels.feeds.convert-id"),
    ("wechat_articles_metrics", "wechat.articles.metrics"),
    ("wechat_articles_metrics_pro", "wechat.articles.metrics-pro"),
    ("wechat_mp_accounts", "wechat.accounts.posts"),
    ("wechat_accounts_search_by_owner_live", "wechat.accounts.search-by-owner-live"),
    ("wechat_library_search_articles", "wechat.library.articles.search"),
    ("wechat_library_search_articles_tokenized", "wechat.library.articles.tokenized"),
    ("wechat_library_search_accounts", "wechat.library.accounts.search"),
    ("wechat_library_accounts_metrics", "wechat.library.accounts.metrics"),
]
