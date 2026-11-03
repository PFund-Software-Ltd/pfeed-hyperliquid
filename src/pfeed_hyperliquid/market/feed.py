from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar, cast

if TYPE_CHECKING:
    from pfeed.market.requests.base_request import MarketFeedBaseRequest
    from pfund_blocks.typing import Message

    from pfeed_hyperliquid.source import Hyperliquid

import pfeed as pe
import polars as pl
from pfeed.market.data_model import MarketDataModel
from pfeed.market.requests.stream_request import MarketFeedStreamRequest
from pfeed.streaming.market import MarketFeedStreamingMixin


class BybitMarketFeed(
    MarketFeedStreamingMixin[MarketFeedStreamRequest, MarketDataModel],
    pe.MarketFeed["Hyperliquid", "MarketFeedBaseRequest", MarketDataModel]
):
    pass
