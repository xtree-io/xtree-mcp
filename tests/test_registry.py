"""MCP tool registry tests."""

from xtree_mcp.registry import MCP_TOOLS


def test_mcp_tool_count():
    assert len(MCP_TOOLS) == 9


def test_mcp_tool_names_unique():
    names = [name for name, _ in MCP_TOOLS]
    assert len(names) == len(set(names))


def test_mcp_omits_undelivered_tools():
    slugs = {s for _, s in MCP_TOOLS}
    assert "wechat.search.videos" not in slugs
    assert "wechat.channels.search" not in slugs
    assert not any(s.startswith("wechat.library.") for s in slugs)
