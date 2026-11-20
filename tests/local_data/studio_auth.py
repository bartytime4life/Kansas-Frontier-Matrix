"""Real, disposable account sessions for protected Studio regression tests."""

from unittest.mock import patch

from tools.local_data.intake_studio import accounts
from tools.local_data.intake_studio.studio_access import COOKIE


OWNER = "owner"
PHRASE = "Synthetic integration passphrase 42!"


def signed_in_headers(test, account_store):
    # Test-only KDF cost, as in the account unit suite. Runtime has no override.
    test.enterContext(patch.dict(accounts.KDF, {"n": 1024}))
    account_store.bootstrap(account_store.issue_setup_code(), OWNER, PHRASE)
    return session_headers(account_store)


def session_headers(account_store):
    """Sign the existing synthetic owner in again, e.g. after a server restart."""
    token = account_store.login(OWNER, PHRASE)
    principal = account_store.session(token)
    return {"Cookie": COOKIE + "=" + token, "X-KFM-CSRF": principal["csrf"]}
