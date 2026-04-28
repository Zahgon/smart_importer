"""Machine learning pipelines for data extraction."""

from __future__ import annotations

import operator
from typing import TYPE_CHECKING

import numpy
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import make_pipeline

if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import Any

    from beancount.core.data import Transaction


class NoFitMixin:
    """Mixin that implements a transformer's fit method that returns self."""

    def fit(self, *_: Any, **__: Any) -> Any:
        """A noop."""
        pass


def txn_attr_getter(attribute_name: str) -> Callable[[Transaction], Any]:
    """Return attribute getter for a transaction that also handles metadata."""
    pass


class NumericTxnAttribute(BaseEstimator, TransformerMixin, NoFitMixin):  # type: ignore[misc]
    """Get a numeric transaction attribute and vectorize."""

    def __init__(self, attr: str) -> None:
        self.attr = attr
        self._txn_getter = txn_attr_getter(attr)

    def transform(
        self, data: list[Transaction], _y: None = None
    ) -> numpy.ndarray[tuple[int, ...], Any]:
        """Return list of entry attributes."""
        pass


class AttrGetter(BaseEstimator, TransformerMixin, NoFitMixin):  # type: ignore[misc]
    """Get a string transaction attribute."""

    def __init__(self, attr: str, default: str | None = None) -> None:
        self.attr = attr
        self.default = default
        self._txn_getter = txn_attr_getter(attr)

    def transform(self, data: list[Transaction], _y: None = None) -> list[Any]:
        """Return list of entry attributes."""
        pass


class StringVectorizer(CountVectorizer):  # type: ignore[misc]
    """Subclass of CountVectorizer that handles empty data."""

    def __init__(
        self,
        tokenizer: Callable[[str], list[str]] | None = None,
        token_pattern: None | str = r"(?u)\b\w\w+\b",
    ) -> None:
        super().__init__(
            ngram_range=(1, 3),
            tokenizer=tokenizer,
            token_pattern=token_pattern,
        )

    def fit_transform(self, raw_documents: list[str], y: None = None) -> Any:
        pass

    def transform(self, raw_documents: list[str], _y: None = None) -> Any:
        pass


def get_pipeline(
    attribute: str,
    tokenizer: Callable[[str], list[str]] | None,
    token_pattern: None | str = r"(?u)\b\w\w+\b",
) -> Any:
    """Make a pipeline for a given entry attribute."""
    pass
