from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, Literal

if TYPE_CHECKING:
    from pfeed.base.feed import BaseFeed

import httpx2
from pfeed.dataflow.retry_policy import RetryPolicy
from pfeed.enums import (
    DataAccessType,
    DataCategory,
    DataProviderType,
    DataType,
)
from pfeed.source import BaseSource, SourceMetadata

from pfeed_hyperliquid.market.feed import HyperliquidMarketFeed


class Hyperliquid(BaseSource):
    Feeds: ClassVar[dict[DataCategory, type[BaseFeed]]] = {
        DataCategory.MARKET_DATA: HyperliquidMarketFeed,
    }
    metadata: ClassVar[SourceMetadata] = SourceMetadata(...)

    market_feed: HyperliquidMarketFeed
