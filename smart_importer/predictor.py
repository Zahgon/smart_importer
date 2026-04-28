"""Machine learning importer decorators."""

# pylint: disable=unsubscriptable-object

from __future__ import annotations

import logging
import threading
from typing import TYPE_CHECKING, Any, Callable

from beancount.core.data import (
    Close,
    Open,
    Transaction,
    filter_txns,
)
from beancount.core.data import sorted as beancount_sorted
from sklearn.pipeline import FeatureUnion, make_pipeline
from sklearn.svm import SVC

from smart_importer.entries import (
    merge_non_transaction_entries,
    set_entry_attribute,
)
from smart_importer.pipelines import get_pipeline
from smart_importer.wrapper import ImporterWrapper

if TYPE_CHECKING:
    from beancount.core import data
    from beangulp.importer import Importer
    from sklearn import Pipeline

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


class EntryPredictor:
    """Base class for machine learning importer helpers.

    Args:
        predict: Whether to add predictions to the entries.
        overwrite: When an attribute is predicted but already exists on an
            entry, overwrite the existing one.
        string_tokenizer: Tokenizer can let smart_importer support more
            languages. This parameter should be an callable function with
            string parameter and the returning should be a list.
        string_token_pattern: Regex for tokenizing text when no custom
            tokenizer is provided. Set to None to disable.
        denylist_accounts: Transations with any of these accounts will be
            removed from the training data.
    """

    # pylint: disable=too-many-instance-attributes

    weights: dict[str, float] = {}
    attribute: str | None = None

    def __init__(  # pylint: disable=too-many-positional-arguments,too-many-arguments
        self,
        predict: bool = True,
        overwrite: bool = False,
        string_tokenizer: Callable[[str], list[str]] | None = None,
        string_token_pattern: str | None = r"(?u)\b\w\w+\b",
        denylist_accounts: list[str] | None = None,
    ) -> None:
        super().__init__()
        self.training_data: list[Transaction] | None = None
        self.open_accounts: dict[str, Open] = {}
        self.denylist_accounts = set(denylist_accounts or [])
        self.pipeline: Pipeline | None = None
        self.is_fitted = False
        self.lock = threading.Lock()
        self.predict = predict
        self.overwrite = overwrite
        self.string_tokenizer = string_tokenizer
        self.string_token_pattern = string_token_pattern

    def wrap(self, importer: Importer) -> ImporterWrapper:
        """Wrap an existing importer with smart importer logic.

        Args:
            importer: The importer to wrap.
        """
        pass

    def hook(
        self,
        imported_entries: list[
            tuple[str, data.Directives, data.Account, Importer]
        ],
        existing_entries: data.Directives,
    ) -> list[tuple[str, data.Directives, data.Account, Importer]]:
        """Predict attributes for imported transactions.

        Args:
            imported_entries: The list of imported entries.
            existing_entries: The list of existing entries as passed to the
                importer - will be used as training data.

        Returns:
            A list of entries, modified by this predictor.
        """
        pass

    def load_open_accounts(self, existing_entries: data.Directives) -> None:
        """Return map of accounts which have been opened but not closed."""
        pass

    def load_training_data(
        self, all_transactions: list[Transaction], account: str
    ) -> None:
        """Load training data, i.e., a list of Beancount entries."""
        pass

    def training_data_filter(self, txn: Transaction, account: str) -> bool:
        """Filter function for the training data."""
        pass

    @property
    def targets(self) -> list[str]:
        """The training targets for the given training data.

        Returns:
            A list training targets (of the same length as the training data).
        """
        pass

    def define_pipeline(self) -> None:
        """Defines the machine learning pipeline based on given weights."""
        pass

    def train_pipeline(self) -> None:
        """Train the machine learning pipeline."""
        pass

    def process_entries(
        self, imported_entries: data.Directives
    ) -> data.Directives:
        """Process imported entries.

        Transactions might be modified, all other entries are left as is.

        Returns:
            The list of entries to be imported.
        """
        pass

    def apply_prediction(
        self, entry: Transaction, prediction: Any
    ) -> Transaction:
        """Apply a single prediction to an entry.

        Args:
            entry: A Beancount entry.
            prediction: The prediction for an attribute.

        Returns:
            The entry with the prediction applied.
        """
        pass

    def process_transactions(
        self, transactions: list[Transaction]
    ) -> list[Transaction]:
        """Process a list of transactions."""
        pass
