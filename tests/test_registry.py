"""MCP tool registry tests."""

from xtree_mcp.registry import MCP_TOOLS


def test_mcp_tool_count():
    assert len(MCP_TOOLS) == 15


def test_mcp_tool_names_unique():
    names = [name for name, _ in MCP_TOOLS]
    assert len(names) == len(set(names))


def test_mcp_library_tools():
    library = [(n, s) for n, s in MCP_TOOLS if s.startswith("wechat.library.")]
    assert len(library) == 4
    slugs = {s for _, s in library}
    assert slugs == {
        "wechat.library.articles.search",
        "wechat.library.articles.tokenized",
        "wechat.library.accounts.search",
        "wechat.library.accounts.metrics",
    }
