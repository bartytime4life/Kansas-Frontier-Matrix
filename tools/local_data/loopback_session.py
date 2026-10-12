"""Owner capability for loopback operators; HTTP browser headers are not identity."""
import secrets


def session_matches(headers, token):
    values = headers.get_all("X-KFM-Session", [])
    return len(values) == 1 and secrets.compare_digest(values[0].encode("utf-8"), token.encode("utf-8"))


def print_connection_links(token, service, origins):
    # Fragments never reach the HTTP server. Keep this operator terminal private.
    print("Open a connection link in your browser (keep it private; renew after restart):", flush=True)
    for origin in sorted(origins):
        print(f"{origin}/#kfm-{service}={token}", flush=True)
