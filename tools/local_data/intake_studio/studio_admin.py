#!/usr/bin/python3
"""KFM Private Studio — local administration program for this PC.

Run ./tools/local_data/intake_studio/studio-admin.sh with no arguments for a
menu, or with a command (see --help). It changes passwords, manages local Studio
accounts, clears sign-in lockouts and connects the data workspace (Working Data
and the Library) so held intake reviews can be sent onward.

Authority comes from owning the private Studio files on this PC; nothing here is
reachable over HTTP. Passwords are read only from the terminal, never from
command arguments, environment variables or files, and are never printed.
"""
from __future__ import annotations

import argparse
import getpass
import os
from pathlib import Path
import signal
import sys
import time

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from tools.local_data.intake_studio import accounts as acc  # noqa: E402
from tools.local_data.intake_studio import workspace_config as wc  # noqa: E402

STORE = Path.home() / ".local/share/kfm-intake-studio"
STATE = Path.home() / ".local/state/kfm-intake-studio"
ADMIN = "./tools/local_data/intake_studio/studio-admin.sh"

MESSAGES = {
    "USE_A_PASSPHRASE_OF_AT_LEAST_15_CHARACTERS": "Use a passphrase of at least 15 characters. Spaces are fine.",
    "CHOOSE_A_LESS_PREDICTABLE_PASSPHRASE": "That passphrase is too predictable. Choose a different one.",
    "PASSWORD_LENGTH_INVALID": "Passphrases can be at most 128 characters.",
    "LAST_ACTIVE_ADMIN_MUST_REMAIN": "That would leave Studio with no active administrator. Create or enable another administrator first.",
    "ACCOUNT_NOT_FOUND": "No Studio account has that username.",
    "USERNAME_ALREADY_EXISTS": "An account with that username already exists.",
    "USERNAME_REQUIRES_3_TO_48_ASCII_CHARACTERS": "Usernames are 3-48 characters: letters, digits, '.', '_' or '-', starting with a letter.",
    "OWNER_ALREADY_CONFIGURED": "An administrator already exists. Use 'password' to change a password instead.",
    "CREATE_FIRST_OWNER_WITH_SETUP_CODE": "No administrator exists yet. Run 'setup-code' and create the first administrator on the sign-in page.",
    "PRIVATE_STUDIO_ROOT_REQUIRED": "The Studio account folder is missing or not private (it must be owned by you, mode 700). Start Studio once, or run 'setup-code'.",
    "UNSAFE_ACCOUNT_STORAGE": "The account database has unsafe permissions or is a link. It must be a regular file owned by you with mode 600.",
    "ACCOUNT_DATABASE_MISSING_RECOVERY_REQUIRED": "The account database is missing but was set up before. Restore it from backup; a new signup is not reopened automatically.",
    "INVALID_ROLE": "Role must be admin, operator or viewer.",
}


class Failure(Exception):
    pass


def explain(error):
    code = str(error)
    return MESSAGES.get(code, code)


def open_accounts(store, create=False):
    store = Path(store).expanduser().absolute()
    if create and not store.exists():
        store.mkdir(parents=True, mode=0o700)
        os.chmod(store, 0o700)
    if not store.is_dir():
        raise Failure(f"No Studio account folder at {store}. Start Studio once, or run '{ADMIN} setup-code'.")
    try:
        return acc.Accounts(store)
    except acc.AccessError as error:
        raise Failure(explain(error)) from error


def ask_passphrase(name, prompt=None):
    if prompt is None:
        if not sys.stdin.isatty():
            raise Failure("Passwords are only accepted from an interactive terminal.")
        prompt = getpass.getpass
    for _ in range(3):
        first = prompt(f"New passphrase for {name}: ")
        try:
            acc.password(first, name, True)
        except acc.AccessError as error:
            print("  " + explain(error)); continue
        if first != prompt("Repeat the new passphrase: "):
            print("  The two entries did not match."); continue
        return first
    raise Failure("Password not changed.")


def running():
    try:
        from tools.local_data.intake_studio.launch_local import running as probe, URL
        return URL if probe() else None
    except Exception:
        return None


def server_pid():
    """PID of a launcher-started Studio, only if /proc confirms it is ours."""
    try:
        pid = int((STATE / "server.pid").read_text().strip())
        proc = Path(f"/proc/{pid}")
        if proc.stat().st_uid != os.getuid():
            return None
        argv = (proc / "cmdline").read_bytes().split(b"\0")
    except (OSError, ValueError):
        return None
    script = Path(argv[1].decode(errors="replace")) if len(argv) > 1 else Path()
    if script.name == "private_server.py" and script.parent.name == "intake_studio":
        return pid
    return None


# ---------------------------------------------------------------- commands

def cmd_status(args):
    url = running()
    print("KFM Private Studio on this PC")
    print(f"  Studio:        {'running at ' + url + '/studio' if url else 'not running (start with ./tools/local_data/intake_studio/start-local.sh)'}")
    print(f"  Account store: {Path(args.store).expanduser()}")
    if Path(args.store).expanduser().is_dir():
        cmd_users(args)
    else:
        print("  Accounts:      not set up yet")
    cmd_workspace_show(args)


def cmd_users(args):
    users = open_accounts(args.store).local_users()
    if not users:
        print(f"  No accounts yet. Run '{ADMIN} setup-code' to create the first administrator.")
        return
    print(f"  {'USERNAME':<24}{'ROLE':<10}{'STATUS':<10}PASSWORD")
    for user in users:
        print(f"  {user['username']:<24}{user['role']:<10}{'enabled' if user['enabled'] else 'disabled':<10}"
              f"{'temporary (must change at sign-in)' if user['must_change'] else 'set'}")


def cmd_password(args, prompt=None):
    accounts = open_accounts(args.store)
    name = acc.username(args.username)
    if not any(u["username"] == name for u in accounts.local_users()):
        raise Failure(explain("ACCOUNT_NOT_FOUND"))
    secret = ask_passphrase(name, prompt)
    result = accounts.local_set_password(name, secret, temporary=args.temporary)
    print(f"Password changed for {result['username']}. Their browser sessions were signed out.")
    if result["temporary"]:
        print("They must choose a new password the next time they sign in.")


def cmd_add_user(args, prompt=None):
    accounts = open_accounts(args.store)
    name = acc.username(args.username)
    print(f"Choose a temporary passphrase for {name}; they must change it at first sign-in.")
    secret = ask_passphrase(name, prompt)
    accounts.local_create(name, args.role, secret)
    print(f"Created {args.role} account {name}.")


def cmd_enable(args, enabled):
    result = open_accounts(args.store).local_update(args.username, enabled=enabled)
    print(f"{result['username']} is now {'enabled' if enabled else 'disabled'}. Their sessions were signed out.")


def cmd_role(args):
    result = open_accounts(args.store).local_update(args.username, role=args.role)
    print(f"{result['username']} is now {result['role']}. Their sessions were signed out.")


def cmd_setup_code(args):
    accounts = open_accounts(args.store, create=True)
    code = accounts.issue_setup_code()
    print("One-time first-administrator setup code (expires in 10 minutes, one use):")
    print("  " + code)
    print("Open http://127.0.0.1:8776/sign-in, enter this code, then choose your username and passphrase.")


def cmd_unlock(args):
    result = open_accounts(args.store).local_unlock()
    print(f"Sign-in limits cleared ({result['cleared']} record(s)). No password was changed.")


def cmd_sign_out_all(args):
    result = open_accounts(args.store).local_revoke_sessions()
    print(f"Signed out {result['revoked']} browser session(s).")


def cmd_audit(args):
    events = open_accounts(args.store).local_audit(args.limit)
    for event in events:
        when = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(event["at"]))
        print(f"  {when}  {event['actor']:<16} {event['action']:<46} {event['target'][:24]}")
    if not events:
        print("  No account activity recorded.")


def cmd_workspace_show(args):
    try:
        values = wc.load(args.config)
    except wc.ConfigError as error:
        print(f"  Data workspace: settings file is invalid — {error}"); return
    print(f"  Data workspace settings: {args.config}")
    if not values:
        print("    Nothing connected. Working Data is required to send held reviews onward.")
        print(f"    Connect it with: {ADMIN} workspace setup")
        return
    for key, (_, _, label) in wc.OPTIONS.items():
        if key in values:
            print(f"    {label}:\n      {values[key]}")
    issues = wc.problems(values)
    for issue in issues:
        print("    ! " + issue)
    if not issues:
        print("    Settings look usable.")


def _save(args, values):
    values = wc.normalize(values)
    issues = wc.problems(values)
    if issues:
        raise Failure("Not saved:\n  " + "\n  ".join(issues))
    wc.save(values, args.config)
    print(f"Saved {args.config}.")
    if running():
        print(f"Studio is running with its previous settings. Apply with: {ADMIN} stop, then start-local.sh")


def cmd_workspace_set(args):
    values = wc.load(args.config)
    values[args.key] = args.value
    _save(args, values)


def cmd_workspace_unset(args):
    values = wc.load(args.config)
    values.pop(args.key, None)
    if args.key == "library_root":
        values.pop("archive_root", None)
    _save(args, values)


def cmd_workspace_init(args):
    """Create a new, empty private Working Data store and connect it."""
    from tools.local_data import manage
    try:
        root = manage.external_root(args.path)
        result = manage.init_store(root)
    except ValueError as error:
        raise Failure(f"Could not initialize {args.path}: {error}") from error
    print(("Initialized new" if result["outcome"] == "INITIALIZED" else "Using existing") + f" Working Data store at {root}.")
    values = wc.load(args.config)
    values["kfm_root"] = str(root)
    _save(args, values)


def cmd_workspace_setup(args, ask=None):
    ask = ask or input
    values = wc.load(args.config)
    print("Connect the data workspace. Press Enter to keep the current value; type '-' to clear it.\n")
    current = values.get("kfm_root", "")
    answer = ask(f"Working Data store folder [{current or 'not set'}]: ").strip()
    if answer == "-":
        values.pop("kfm_root", None)
    elif answer:
        path = Path(answer).expanduser()
        if not (path / ".kfm-local-store.json").exists():
            if ask(f"{path} is not a KFM data store yet. Create a new empty Working Data store there? [y/N]: ").strip().lower() != "y":
                raise Failure("Not changed.")
            from tools.local_data import manage
            try:
                manage.init_store(manage.external_root(str(path)))
            except ValueError as error:
                raise Failure(f"Could not initialize {path}: {error}") from error
            print(f"  Initialized {path}.")
        values["kfm_root"] = str(path)
    for key in ("library_root", "archive_root", "inbox"):
        label = wc.OPTIONS[key][2]
        answer = ask(f"{label} (optional) [{values.get(key, 'not set')}]: ").strip()
        if answer == "-":
            values.pop(key, None)
        elif answer:
            values[key] = answer
    _save(args, values)


def cmd_stop(args):
    pid = server_pid()
    if pid is None:
        if running():
            raise Failure("Studio is running but was not started by the launcher (or its PID record is stale). Stop it with Ctrl+C in its terminal.")
        print("Studio is not running.")
        return
    os.kill(pid, signal.SIGTERM)
    for _ in range(50):
        if not Path(f"/proc/{pid}").exists():
            break
        time.sleep(0.1)
    else:
        raise Failure(f"Studio (PID {pid}) did not stop within 5 seconds.")
    (STATE / "server.pid").unlink(missing_ok=True)
    print("Studio stopped. Start it again with ./tools/local_data/intake_studio/start-local.sh")


# ---------------------------------------------------------------- menu

def menu(args):
    actions = [
        ("Show status, accounts and data workspace", cmd_status),
        ("Change a password", lambda a: cmd_password(_with(a, username=input("Username: ").strip(),
            temporary=input("Make it temporary (they must change it at sign-in)? [y/N]: ").strip().lower() == "y"))),
        ("Add a user", lambda a: cmd_add_user(_with(a, username=input("New username: ").strip(),
            role=(input("Role: admin, operator or viewer [viewer]: ").strip().lower() or "viewer")))),
        ("Enable or disable a user", lambda a: cmd_enable(_with(a, username=input("Username: ").strip()),
            input("Enable (e) or disable (d)? ").strip().lower().startswith("e"))),
        ("Clear sign-in lockouts", cmd_unlock),
        ("Sign out every browser session", cmd_sign_out_all),
        ("Recent account activity", lambda a: cmd_audit(_with(a, limit=40))),
        ("Connect the data workspace (Working Data / Library)", cmd_workspace_setup),
        ("Create the first administrator setup code", cmd_setup_code),
        ("Stop the running Studio", cmd_stop),
    ]
    while True:
        print("\nKFM Private Studio — local administration (this PC only)")
        for number, (label, _) in enumerate(actions, 1):
            print(f"  {number:>2}) {label}")
        print("   q) Quit")
        choice = input("Choose: ").strip().lower()
        if choice in {"q", "quit", "exit", ""}:
            return 0
        if not choice.isdigit() or not 1 <= int(choice) <= len(actions):
            continue
        print()
        try:
            actions[int(choice) - 1][1](args)
        except (Failure, acc.AccessError, wc.ConfigError) as error:
            print("! " + explain(error))
        except (EOFError, KeyboardInterrupt):
            print("\nCancelled.")


def _with(args, **changes):
    copy = argparse.Namespace(**vars(args)); vars(copy).update(changes)
    return copy


def parser():
    p = argparse.ArgumentParser(prog="studio-admin", description=__doc__.split("\n\n")[0],
        epilog="Run with no command for an interactive menu.")
    p.add_argument("--store", default=str(STORE), help="Studio account folder (default: %(default)s)")
    p.add_argument("--config", default=str(wc.CONFIG), help="data workspace settings file (default: %(default)s)")
    sub = p.add_subparsers(dest="command")
    sub.add_parser("status", help="show Studio, accounts and data workspace")
    sub.add_parser("users", help="list Studio accounts")
    c = sub.add_parser("password", help="change any account's password (prompts; never an argument)")
    c.add_argument("username"); c.add_argument("--temporary", action="store_true", help="user must change it at next sign-in")
    c = sub.add_parser("add-user", help="create an account with a temporary password")
    c.add_argument("username"); c.add_argument("--role", choices=acc.ROLES, default="viewer")
    for name in ("enable", "disable"):
        sub.add_parser(name, help=f"{name} an account").add_argument("username")
    c = sub.add_parser("role", help="change an account's role"); c.add_argument("username"); c.add_argument("role", choices=acc.ROLES)
    sub.add_parser("setup-code", help="one-time code to create the first administrator")
    sub.add_parser("unlock", help="clear sign-in lockouts after too many failed attempts")
    sub.add_parser("sign-out-all", help="sign out every browser session")
    c = sub.add_parser("audit", help="recent account activity"); c.add_argument("--limit", type=int, default=40)
    sub.add_parser("stop", help="stop a launcher-started Studio so new settings apply")
    w = sub.add_parser("workspace", help="connect Working Data and the Library").add_subparsers(dest="workspace", required=True)
    w.add_parser("show", help="show data workspace settings")
    w.add_parser("setup", help="guided setup")
    c = w.add_parser("init", help="create a new empty Working Data store and connect it"); c.add_argument("path")
    c = w.add_parser("set", help="set one setting"); c.add_argument("key", choices=sorted(wc.OPTIONS)); c.add_argument("value")
    c = w.add_parser("unset", help="clear one setting"); c.add_argument("key", choices=sorted(wc.OPTIONS))
    return p


COMMANDS = {
    "status": cmd_status, "users": cmd_users, "password": cmd_password, "add-user": cmd_add_user,
    "enable": lambda a: cmd_enable(a, True), "disable": lambda a: cmd_enable(a, False), "role": cmd_role,
    "setup-code": cmd_setup_code, "unlock": cmd_unlock, "sign-out-all": cmd_sign_out_all,
    "audit": cmd_audit, "stop": cmd_stop,
}
WORKSPACE = {"show": cmd_workspace_show, "setup": cmd_workspace_setup, "init": cmd_workspace_init,
             "set": cmd_workspace_set, "unset": cmd_workspace_unset}


def main(argv=None):
    os.umask(0o077)
    args = parser().parse_args(argv)
    args.config = Path(args.config).expanduser()
    try:
        if args.command is None:
            return menu(args)
        (WORKSPACE[args.workspace] if args.command == "workspace" else COMMANDS[args.command])(args)
        return 0
    except (Failure, acc.AccessError, wc.ConfigError) as error:
        print("Error: " + explain(error), file=sys.stderr)
        return 1
    except (EOFError, KeyboardInterrupt):
        print("\nCancelled.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    sys.exit(main())
