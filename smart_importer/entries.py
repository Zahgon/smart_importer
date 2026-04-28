"""Helpers to work with Beancount entry objects."""

from __future__ import annotations

from typing import TYPE_CHECKING

from beancount.core.data import Posting, Transaction

if TYPE_CHECKING:
    from collections.abc import Sequence
    from typing import Any

    from beancount.core.data import Directive


def update_postings(
    transaction: Transaction, accounts: list[str]
) -> Transaction:
    """Update the list of postings of a transaction to match the accounts.

    Expects the transaction to be updated to have exactly one posting,
    otherwise it is returned unchanged. Adds empty postings for all the
    accounts - if the account of the single existing posting is found
    in the list of accounts, it is placed there at the first occurence,
    otherwise it is appended at the end.
    """
    pass


def set_entry_attribute(
    entry: Transaction, attribute: str, value: Any, overwrite: bool = False
) -> Transaction:
    """Set an entry attribute."""
    pass


def merge_non_transaction_entries(
    imported_entries: Sequence[Directive],
    enhanced_transactions: Sequence[Directive],
) -> list[Directive]:
    """Merge modified transactions back into a list of entries."""
    pass
