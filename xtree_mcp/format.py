"""Format API responses for MCP tool output."""

from __future__ import annotations

import json
from typing import Any

from xtree.types import APIResponse, ResponseMeta


def meta_dict(meta: ResponseMeta) -> dict[str, Any]:
    out: dict[str, Any] = {
        "request_id": meta.request_id,
        "cost_cny": meta.cost_cny,
        "balance_cny": meta.balance_cny,
        "rate_limit_remaining": meta.rate_limit_remaining,
    }
    for key in (
        "observation_id",
        "observed_at",
        "basis",
        "contract_rev",
        "origin",
        "cache_hit",
        "cache_age_sec",
    ):
        value = getattr(meta, key)
        if value is not None:
            out[key] = value
    return out


def as_tool_json(resp: APIResponse[Any]) -> str:
    """Return business data plus _meta footer for Agent transparency."""
    payload = {"data": resp.data, "_meta": meta_dict(resp.meta)}
    return json.dumps(payload, ensure_ascii=False)
