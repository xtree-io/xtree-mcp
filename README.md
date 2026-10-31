# xtree-mcp — XTREE MCP server

MCP server that exposes [XTREE](https://www.xtree.io) **real-time raw data** tools for AI agents (Cursor, Claude Desktop, and any MCP client). Fetch WeChat search / Channels / article metrics and more — **not** a BI or copywriting product.

Tools call `https://api.xtree.io` with your own API Key and wallet (pay per call).

## Install / run

Package may not be on PyPI yet. Prefer GitHub:

```bash
# one-shot via uvx
uvx --from "git+https://github.com/xtree-io/xtree-mcp.git" xtree-mcp
```

Or install editable after cloning:

```bash
git clone https://github.com/xtree-io/xtree-mcp.git
cd xtree-mcp
pip install "git+https://github.com/xtree-io/xtree-python.git"
pip install -e .
```

## Get an API Key

1. Sign up at [www.xtree.io](https://www.xtree.io/login?tab=signup).
2. Set `XTREE_API_KEY=xt_live_...`.

## Cursor / Claude config

```json
{
  "mcpServers": {
    "xtree": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/xtree-io/xtree-mcp.git", "xtree-mcp"],
      "env": {
        "XTREE_API_KEY": "xt_live_..."
      }
    }
  }
}
```

## Billing

Each tool call is a billed API request from your wallet (CNY). Incomplete delivery is not billed. Unit prices: [API Catalog](https://www.xtree.io/catalog). Scenario playbooks (when to call which tool, pagination): [xtree-skills](https://github.com/xtree-io/xtree-skills).

## Docs

- Website docs: https://www.xtree.io/docs
- OpenAPI: https://api.xtree.io/api/openapi.json
- Python SDK: https://github.com/xtree-io/xtree-python
- Skills: https://github.com/xtree-io/xtree-skills

## Environment

| Variable | Required | Default |
|----------|----------|---------|
| `XTREE_API_KEY` | yes | — |
| `XTREE_BASE_URL` | no | `https://api.xtree.io/api` |
| `XTREE_VERIFY_CODE` | no | — |

## Mirror notice

**Do not develop in this repository.** Public mirror only. Issues welcome. Contact: [business@xtree.io](mailto:business@xtree.io).

## License

MIT.
