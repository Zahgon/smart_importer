"""Wrap importers with smart_importer predictors."""

from __future__ import annotations

from typing import TYPE_CHECKING

from beangulp.importer import Importer

if TYPE_CHECKING:
    import datetime

    from beancount.core.data import Directive

    from smart_importer.predictor import EntryPredictor


class ImporterWrapper(Importer):
    """Wrapper around an importer for enriching it with smart importer logic.

    Args:
        importer: The importer to wrap
        predictor: The entry predictor
    """

    def __init__(self, importer: Importer, predictor: EntryPredictor) -> None:
        self.importer = importer
        self.predictor = predictor

    @property
    def name(self) -> str:
        pass

    def identify(self, filepath: str) -> bool:
        pass

    def account(self, filepath: str) -> str:
        pass

    def date(self, filepath: str) -> datetime.date | None:
        pass

    def filename(self, filepath: str) -> str | None:
        pass

    def deduplicate(
        self, entries: list[Directive], existing: list[Directive]
    ) -> None:
        pass

    def sort(self, entries: list[Directive], reverse: bool = False) -> None:
        pass

    def extract(
        self, filepath: str, existing: list[Directive]
    ) -> list[Directive]:
        pass
