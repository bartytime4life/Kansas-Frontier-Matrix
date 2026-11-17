"""Local Studio identities. No external identity provider or plaintext passwords.

Passwords: scrypt N=2**17, r=8, p=1 (128 MiB); sessions: random, server-side,
hashed at rest. This does not protect against the operating-system account
that owns these files, and must not be exposed beyond literal loopback HTTP.
"""
from __future__ import annotations

from contextlib import contextmanager
import argparse
import getpass
import hashlib
import hmac
import json
import os
from pathlib import Path
import re
import secrets
import sqlite3
import stat
import threading
import time
import unicodedata
import uuid

ROLES = ("admin", "operator", "viewer")
IDLE_SECONDS = 1800
ABSOLUTE_SECONDS = 28800
MAX_USERS = 64
MAX_AUDIT = 20000
KDF = dict(n=2**17, r=8, p=1, maxmem=256 * 1024 * 1024, dklen=32)
_KDF_LIMIT = threading.BoundedSemaphore(2)
# Offline, intentionally bounded denylist; not a claim of exhaustive breach screening.
BLOCKLIST = {"passwordpassword", "passwordpassword1", "123456789012345", "1234567890123456",
             "qwertyuiopasdfgh", "letmeinletmein123", "kansasfrontiermatrix", "kfmstudioadmin123"}


class AccessError(ValueError):
    def __init__(self, code, status=400):
        super().__init__(code)
        self.status = status


def digest(value):
    return hashlib.sha256(value.encode("utf-8") if isinstance(value, str) else value).hexdigest()


def username(value):
    if not isinstance(value, str) or not re.fullmatch(r"[a-zA-Z][a-zA-Z0-9_.-]{2,47}", value):
        raise AccessError("USERNAME_REQUIRES_3_TO_48_ASCII_CHARACTERS")
    return value.lower()


def password(value, user="", setting=False):
    if not isinstance(value, str):
        raise AccessError("INVALID_PASSWORD")
    value = unicodedata.normalize("NFC", value)
    if not 1 <= len(value) <= 128 or len(value.encode("utf-8")) > 512 or "\x00" in value:
        raise AccessError("PASSWORD_LENGTH_INVALID")
    if setting:
        if len(value) < 15:
            raise AccessError("USE_A_PASSPHRASE_OF_AT_LEAST_15_CHARACTERS")
        if value.casefold() in BLOCKLIST | {user.casefold(), (user * 3).casefold()} or len(set(value)) < 3:
            raise AccessError("CHOOSE_A_LESS_PREDICTABLE_PASSPHRASE")
    return value


def hash_password(value):
    salt = secrets.token_bytes(16)
    with _KDF_LIMIT:
        key = hashlib.scrypt(value.encode("utf-8"), salt=salt, **KDF)
    return "scrypt-v1$" + salt.hex() + "$" + key.hex()


def verify_password(value, encoded):
    # Fixed production cost; parameters cannot be supplied by a request or database row.
    try:
        version, salt, expected = encoded.split("$")
        if version != "scrypt-v1" or not re.fullmatch(r"[0-9a-f]{32}", salt) or not re.fullmatch(r"[0-9a-f]{64}", expected):
            raise ValueError()
        with _KDF_LIMIT:
            actual = hashlib.scrypt(value.encode("utf-8"), salt=bytes.fromhex(salt), **KDF)
        return hmac.compare_digest(actual.hex(), expected)
    except (ValueError, TypeError, AttributeError):
        return False


def csrf(token):
    return hmac.new(token.encode(), b"kfm-studio-csrf-v1", hashlib.sha256).hexdigest()


class Accounts:
    """App-local accounts, not Linux login accounts. All changes are transactional."""
    def __init__(self, root, clock=time.time):
        self.root = Path(root).absolute()
        self.path = self.root / "studio-accounts.sqlite3"
        self.marker = self.root / ".studio-accounts-required"
        self.clock = clock
        self.session_namespace = secrets.token_bytes(32)
        self.lock = threading.RLock()
        self._initialize()
        self.dummy_hash = hash_password(secrets.token_urlsafe(32))

    def _check_path(self, path):
        if path.is_symlink():
            raise AccessError("UNSAFE_ACCOUNT_STORAGE", 503)
        info = path.stat()
        if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) & 0o077 or info.st_nlink != 1:
            raise AccessError("UNSAFE_ACCOUNT_STORAGE", 503)

    def _initialize(self):
        if self.root.is_symlink() or not self.root.is_dir():
            raise AccessError("PRIVATE_STUDIO_ROOT_REQUIRED", 503)
        info = self.root.stat()
        if info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) & 0o077:
            raise AccessError("PRIVATE_STUDIO_ROOT_REQUIRED", 503)
        with self.lock:
            if self.marker.exists():
                self._check_path(self.marker)
                if not self.path.exists():
                    raise AccessError("ACCOUNT_DATABASE_MISSING_RECOVERY_REQUIRED", 503)
            if not self.path.exists():
                fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY | os.O_NOFOLLOW, 0o600)
                os.close(fd)
            self._check_path(self.path)
            with self.db() as db:
                db.executescript("""
                CREATE TABLE IF NOT EXISTS metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS users (id TEXT PRIMARY KEY, username TEXT UNIQUE NOT NULL,
                  password_hash TEXT NOT NULL, role TEXT NOT NULL CHECK(role IN ('admin','operator','viewer')),
                  enabled INTEGER NOT NULL, must_change INTEGER NOT NULL, version INTEGER NOT NULL, created REAL NOT NULL);
                CREATE TABLE IF NOT EXISTS sessions (token_hash TEXT PRIMARY KEY, user_id TEXT NOT NULL,
                  version INTEGER NOT NULL, created REAL NOT NULL, touched REAL NOT NULL);
                CREATE TABLE IF NOT EXISTS attempts (key TEXT PRIMARY KEY, failures INTEGER NOT NULL,
                  until REAL NOT NULL, touched REAL NOT NULL);
                CREATE TABLE IF NOT EXISTS audit (sequence INTEGER PRIMARY KEY, at REAL NOT NULL,
                  actor TEXT NOT NULL, action TEXT NOT NULL, target TEXT NOT NULL);
                """)
                db.execute("INSERT OR IGNORE INTO metadata VALUES ('database_id',?)", (uuid.uuid4().hex,))
                database_id = db.execute("SELECT value FROM metadata WHERE key='database_id'").fetchone()[0]
            if self.marker.exists():
                if self.marker.read_text().strip() != database_id:
                    raise AccessError("ACCOUNT_DATABASE_IDENTITY_MISMATCH", 503)
            else:
                fd = os.open(self.marker, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
                with os.fdopen(fd, "w") as stream:
                    stream.write(database_id + "\n"); stream.flush(); os.fsync(stream.fileno())

    @contextmanager
    def db(self):
        self._check_path(self.path)
        for suffix in ("-journal", "-wal", "-shm"):
            sidecar = Path(str(self.path) + suffix)
            if sidecar.exists() or sidecar.is_symlink():
                self._check_path(sidecar)
        db = sqlite3.connect(self.path.as_uri() + "?mode=rw", uri=True, timeout=5)
        db.row_factory = sqlite3.Row
        try:
            db.execute("PRAGMA synchronous=FULL")
            db.execute("BEGIN IMMEDIATE")
            yield db
            db.commit()
        except BaseException:
            db.rollback(); raise
        finally:
            db.close()

    def _audit(self, db, actor, action, target=""):
        if db.execute("SELECT COUNT(*) FROM audit").fetchone()[0] >= MAX_AUDIT:
            raise AccessError("ACCOUNT_AUDIT_FULL_EXPORT_AND_REVIEW_REQUIRED", 503)
        db.execute("INSERT INTO audit(at,actor,action,target) VALUES (?,?,?,?)",
                   (self.clock(), actor, action, target))

    def initialized(self):
        with self.db() as db:
            return bool(db.execute("SELECT 1 FROM users LIMIT 1").fetchone())

    def issue_setup_code(self):
        """Local command only; never exposed as an HTTP action."""
        code = secrets.token_urlsafe(32)
        with self.db() as db:
            if db.execute("SELECT 1 FROM users LIMIT 1").fetchone():
                raise AccessError("OWNER_ALREADY_CONFIGURED")
            db.execute("INSERT OR REPLACE INTO metadata VALUES ('setup',?)",
                       (json.dumps({"hash": digest(code), "expires": self.clock() + 600}),))
            self._audit(db, "local-console", "setup_code_issued")
        return code

    def _throttle(self, db, key):
        now = self.clock()
        row = db.execute("SELECT * FROM attempts WHERE key=?", (key,)).fetchone()
        if row and row["until"] > now:
            raise AccessError("SIGN_IN_TEMPORARILY_LIMITED", 429)
        return row

    def _failure(self, db, key):
        now = self.clock()
        row = db.execute("SELECT * FROM attempts WHERE key=?", (key,)).fetchone()
        n = (row["failures"] if row and now - row["touched"] < 3600 else 0) + 1
        until = now + (min(900, 30 * 2 ** min(5, n - 5)) if n >= 5 else 0)
        db.execute("INSERT OR REPLACE INTO attempts VALUES (?,?,?,?)", (key, n, until, now))
        db.execute("DELETE FROM attempts WHERE touched<?", (now - 86400,))
        if db.execute("SELECT COUNT(*) FROM attempts").fetchone()[0] > 2048:
            raise AccessError("SIGN_IN_TEMPORARILY_LIMITED", 429)

    def bootstrap(self, code, name, secret):
        name = username(name); secret = password(secret, name, True)
        encoded = None
        with self.lock:
            error = None
            with self.db() as db:
                if db.execute("SELECT 1 FROM users LIMIT 1").fetchone():
                    raise AccessError("OWNER_ALREADY_CONFIGURED", 409)
                self._throttle(db, "setup")
                saved = db.execute("SELECT value FROM metadata WHERE key='setup'").fetchone()
                setup = json.loads(saved[0]) if saved else {}
                if not isinstance(code, str) or len(code) > 128 or setup.get("expires", 0) <= self.clock() or not hmac.compare_digest(setup.get("hash", ""), digest(code)):
                    self._failure(db, "setup"); error = AccessError("SETUP_CODE_INVALID_OR_EXPIRED", 403)
                else:
                    encoded = hash_password(secret)
                    db.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?,?)",
                               (uuid.uuid4().hex, name, encoded, "admin", 1, 0, 1, self.clock()))
                    db.execute("DELETE FROM metadata WHERE key='setup'")
                    self._audit(db, name, "first_owner_created", name)
            if error: raise error
        return {"configured": True}

    def session_hash(self, token):
        return hmac.new(self.session_namespace, token.encode(), hashlib.sha256).hexdigest()

    def login(self, name, secret):
        # Uniform response for nonexistent, disabled, and wrong-password accounts.
        try: name = username(name)
        except AccessError: name = "invalid"
        try: secret = password(secret)
        except AccessError: secret = "invalid"
        key = "login:" + digest(name)
        with self.lock:
            error = None; token = None
            with self.db() as db:
                self._throttle(db, key); self._throttle(db, "global-login")
                row = db.execute("SELECT * FROM users WHERE username=?", (name,)).fetchone()
                valid = verify_password(secret, row["password_hash"] if row else self.dummy_hash)
                if not row or not row["enabled"] or not valid:
                    self._failure(db, key); self._failure(db, "global-login")
                    self._audit(db, "unauthenticated", "login_failed", digest(name))
                    error = AccessError("INVALID_USERNAME_OR_PASSWORD", 401)
                else:
                    now = self.clock(); token = secrets.token_urlsafe(32)
                    db.execute("DELETE FROM attempts WHERE key=?", (key,))
                    db.execute("DELETE FROM sessions WHERE touched<? OR created<?", (now-IDLE_SECONDS, now-ABSOLUTE_SECONDS))
                    if db.execute("SELECT COUNT(*) FROM sessions WHERE user_id=?", (row["id"],)).fetchone()[0] >= 8:
                        db.execute("DELETE FROM sessions WHERE token_hash=(SELECT token_hash FROM sessions WHERE user_id=? ORDER BY created LIMIT 1)", (row["id"],))
                    db.execute("INSERT INTO sessions VALUES (?,?,?,?,?)", (self.session_hash(token), row["id"], row["version"], now, now))
                    self._audit(db, name, "login_succeeded")
            if error: raise error
        return token

    def session(self, token):
        if not isinstance(token, str) or not re.fullmatch(r"[A-Za-z0-9_-]{43}", token):
            return None
        with self.db() as db:
            row = db.execute("SELECT u.*,s.created AS session_created,s.touched,s.version AS session_version FROM sessions s JOIN users u ON u.id=s.user_id WHERE token_hash=?", (self.session_hash(token),)).fetchone()
            now = self.clock()
            if not row or not row["enabled"] or row["version"] != row["session_version"] or now-row["touched"] > IDLE_SECONDS or now-row["session_created"] > ABSOLUTE_SECONDS:
                db.execute("DELETE FROM sessions WHERE token_hash=?", (self.session_hash(token),)); return None
            db.execute("UPDATE sessions SET touched=? WHERE token_hash=?", (now, self.session_hash(token)))
            return {"id": row["id"], "username": row["username"], "role": row["role"],
                    "mustChangePassword": bool(row["must_change"]), "csrf": csrf(token)}

    def logout(self, token):
        with self.db() as db:
            db.execute("DELETE FROM sessions WHERE token_hash=?", (self.session_hash(token),))

    def _reauth(self, actor, secret):
        """Checks current role/enabled state; a stale session object cannot authorize."""
        key = "reauth:" + actor["id"]
        error = None
        with self.db() as db:
            self._throttle(db, key)
            row = db.execute("SELECT * FROM users WHERE id=? AND enabled=1", (actor["id"],)).fetchone()
            valid = verify_password(password(secret), row["password_hash"] if row else self.dummy_hash)
            if not row or not valid:
                self._failure(db, key); error = AccessError("CURRENT_PASSWORD_INCORRECT", 403)
            else: db.execute("DELETE FROM attempts WHERE key=?", (key,))
        if error: raise error
        return dict(row)

    def change_password(self, actor, current, new):
        with self.lock:
            row = self._reauth(actor, current)
            new = password(new, row["username"], True)
            if verify_password(new, row["password_hash"]):
                raise AccessError("CHOOSE_A_NEW_PASSPHRASE")
            encoded = hash_password(new)
            with self.db() as db:
                db.execute("UPDATE users SET password_hash=?,must_change=0,version=version+1 WHERE id=?", (encoded, row["id"]))
                db.execute("DELETE FROM sessions WHERE user_id=?", (row["id"],))
                self._audit(db, row["username"], "password_changed_sessions_revoked", row["username"])
        return {"signedOut": True}

    def manage(self, actor, value):
        allowed = {"action", "currentPassword", "username", "password", "role", "enabled"}
        if not isinstance(value, dict) or set(value)-allowed:
            raise AccessError("INVALID_ACCOUNT_REQUEST")
        with self.lock:
            owner = self._reauth(actor, value.get("currentPassword", ""))
            if owner["role"] != "admin" or owner["must_change"]:
                raise AccessError("ADMIN_REQUIRED", 403)
            action = value.get("action"); name = username(value.get("username"))
            role = value.get("role", "viewer")
            if role not in ROLES: raise AccessError("INVALID_ROLE")
            if action not in {"create", "reset", "update"}: raise AccessError("UNKNOWN_ACCOUNT_ACTION")
            encoded = hash_password(password(value.get("password"), name, True)) if action in {"create", "reset"} else None
            with self.db() as db:
                row = db.execute("SELECT * FROM users WHERE username=?", (name,)).fetchone()
                if action == "create":
                    if row: raise AccessError("USERNAME_ALREADY_EXISTS", 409)
                    if db.execute("SELECT COUNT(*) FROM users").fetchone()[0] >= MAX_USERS:
                        raise AccessError("ACCOUNT_LIMIT_REACHED")
                    db.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?,?)", (uuid.uuid4().hex, name, encoded, role, 1, 1, 1, self.clock()))
                else:
                    if not row: raise AccessError("ACCOUNT_NOT_FOUND", 404)
                    enabled = value.get("enabled", bool(row["enabled"]))
                    if type(enabled) is not bool: raise AccessError("INVALID_ENABLED_VALUE")
                    role = value.get("role", row["role"])
                    loses_admin = row["role"] == "admin" and row["enabled"] and (action == "reset" or not enabled or role != "admin")
                    if loses_admin and db.execute("SELECT COUNT(*) FROM users WHERE role='admin' AND enabled=1 AND must_change=0").fetchone()[0] <= 1:
                        raise AccessError("LAST_ACTIVE_ADMIN_MUST_REMAIN", 409)
                    if action == "reset":
                        db.execute("UPDATE users SET password_hash=?,must_change=1,version=version+1 WHERE id=?", (encoded, row["id"]))
                    else:
                        db.execute("UPDATE users SET role=?,enabled=?,version=version+1 WHERE id=?", (role, int(enabled), row["id"]))
                    db.execute("DELETE FROM sessions WHERE user_id=?", (row["id"],))
                self._audit(db, owner["username"], "account_" + action, name)
        return {"updated": True, "sessionsRevoked": action != "create"}

    def users(self, actor):
        if actor["role"] != "admin": raise AccessError("ADMIN_REQUIRED", 403)
        with self.db() as db:
            return [dict(row) for row in db.execute("SELECT username,role,enabled,must_change,created FROM users ORDER BY username")]

    def audit(self, actor):
        if actor["role"] != "admin": raise AccessError("ADMIN_REQUIRED", 403)
        with self.db() as db:
            return [dict(row) for row in db.execute("SELECT * FROM audit ORDER BY sequence DESC LIMIT 500")]

    # ---- Local console administration (studio_admin.py). No HTTP route reaches these.
    # Authority comes from owning the private account files on this PC, the same
    # boundary as local_reset. Every change is audited as "local-console".

    @staticmethod
    def _active_admins(db):
        return db.execute("SELECT COUNT(*) FROM users WHERE role='admin' AND enabled=1 AND must_change=0").fetchone()[0]

    def _local_row(self, db, name):
        row = db.execute("SELECT * FROM users WHERE username=?", (username(name),)).fetchone()
        if not row: raise AccessError("ACCOUNT_NOT_FOUND", 404)
        return row

    def local_users(self):
        with self.db() as db:
            return [dict(row) for row in db.execute("SELECT username,role,enabled,must_change,created FROM users ORDER BY username")]

    def local_audit(self, limit=50):
        limit = max(1, min(int(limit), 500))
        with self.db() as db:
            return [dict(row) for row in db.execute("SELECT * FROM audit ORDER BY sequence DESC LIMIT ?", (limit,))]

    def local_set_password(self, name, new, temporary=False):
        """Set any account's password from this PC. Revokes that account's sessions."""
        name = username(name); encoded = hash_password(password(new, name, True))
        with self.lock, self.db() as db:
            row = self._local_row(db, name)
            permanent_admin = row["role"] == "admin" and row["enabled"] and not row["must_change"]
            if temporary and permanent_admin and self._active_admins(db) <= 1:
                raise AccessError("LAST_ACTIVE_ADMIN_MUST_REMAIN", 409)
            db.execute("UPDATE users SET password_hash=?,must_change=?,version=version+1 WHERE id=?",
                       (encoded, int(bool(temporary)), row["id"]))
            db.execute("DELETE FROM sessions WHERE user_id=?", (row["id"],))
            db.execute("DELETE FROM attempts WHERE key IN (?,?,?)", ("login:" + digest(name), "global-login", "reauth:" + row["id"]))
            self._audit(db, "local-console", "local_password_set_temporary" if temporary else "local_password_set", name)
        return {"username": name, "temporary": bool(temporary), "sessionsRevoked": True}

    def local_create(self, name, role, temporary_password):
        name = username(name)
        if role not in ROLES: raise AccessError("INVALID_ROLE")
        encoded = hash_password(password(temporary_password, name, True))
        with self.lock, self.db() as db:
            if db.execute("SELECT 1 FROM users WHERE username=?", (name,)).fetchone():
                raise AccessError("USERNAME_ALREADY_EXISTS", 409)
            if db.execute("SELECT COUNT(*) FROM users").fetchone()[0] >= MAX_USERS:
                raise AccessError("ACCOUNT_LIMIT_REACHED")
            if not db.execute("SELECT 1 FROM users LIMIT 1").fetchone():
                raise AccessError("CREATE_FIRST_OWNER_WITH_SETUP_CODE", 409)
            db.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?,?)", (uuid.uuid4().hex, name, encoded, role, 1, 1, 1, self.clock()))
            self._audit(db, "local-console", "local_account_create", name)
        return {"username": name, "role": role, "temporary": True}

    def local_update(self, name, role=None, enabled=None):
        with self.lock, self.db() as db:
            row = self._local_row(db, name)
            role = row["role"] if role is None else role
            enabled = bool(row["enabled"]) if enabled is None else enabled
            if role not in ROLES: raise AccessError("INVALID_ROLE")
            if type(enabled) is not bool: raise AccessError("INVALID_ENABLED_VALUE")
            permanent_admin = row["role"] == "admin" and row["enabled"] and not row["must_change"]
            if permanent_admin and (not enabled or role != "admin") and self._active_admins(db) <= 1:
                raise AccessError("LAST_ACTIVE_ADMIN_MUST_REMAIN", 409)
            db.execute("UPDATE users SET role=?,enabled=?,version=version+1 WHERE id=?", (role, int(enabled), row["id"]))
            db.execute("DELETE FROM sessions WHERE user_id=?", (row["id"],))
            self._audit(db, "local-console", "local_account_update", row["username"])
        return {"username": row["username"], "role": role, "enabled": enabled, "sessionsRevoked": True}

    def local_unlock(self):
        """Clear sign-in throttling after a lockout. Does not change any password."""
        with self.lock, self.db() as db:
            cleared = db.execute("DELETE FROM attempts").rowcount
            self._audit(db, "local-console", "local_sign_in_limits_cleared")
        return {"cleared": cleared}

    def local_revoke_sessions(self):
        with self.lock, self.db() as db:
            revoked = db.execute("DELETE FROM sessions").rowcount
            self._audit(db, "local-console", "local_all_sessions_revoked")
        return {"revoked": revoked}

    def local_reset(self, name, new):
        """Break-glass OS-owner command. No HTTP route, no return of old password."""
        name = username(name); encoded = hash_password(password(new, name, True))
        with self.lock, self.db() as db:
            row = db.execute("SELECT id FROM users WHERE username=? AND role='admin'", (name,)).fetchone()
            if not row: raise AccessError("LOCAL_RECOVERY_REQUIRES_EXISTING_ADMIN")
            db.execute("UPDATE users SET password_hash=?,enabled=1,must_change=0,version=version+1 WHERE id=?", (encoded, row["id"]))
            db.execute("DELETE FROM sessions")
            self._audit(db, "local-console", "break_glass_admin_reset_all_sessions_revoked", name)


def main():
    parser = argparse.ArgumentParser(description="Private KFM Studio account setup/recovery; never supply passwords as command arguments.")
    parser.add_argument("--store", type=Path, required=True)
    parser.add_argument("action", choices=("setup-code", "reset-admin"))
    parser.add_argument("--username")
    args = parser.parse_args()
    os.umask(0o077)
    accounts = Accounts(args.store)
    if args.action == "setup-code":
        print("One-time first-owner setup code (expires in 10 minutes):")
        print(accounts.issue_setup_code())
    else:
        if not args.username: parser.error("--username is required for reset-admin")
        first = getpass.getpass("New admin passphrase: ")
        if first != getpass.getpass("Repeat new passphrase: "): parser.error("Passphrases do not match")
        accounts.local_reset(args.username, first)
        print("Admin password changed. All browser sessions revoked. No evidence or intake records changed.")


if __name__ == "__main__":
    main()
