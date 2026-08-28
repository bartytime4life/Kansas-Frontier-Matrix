# KFM Python no-network startup guard

This directory contains the opt-in Python startup guard used by bounded CI
steps that must fail before common IPv4 or IPv6 egress paths can leave the
process.

Add this directory to `PYTHONPATH` and set `KFM_NO_NETWORK=1` before starting
Python:

```bash
export KFM_NO_NETWORK=1
export PYTHONPATH="$PWD/tools/ci/kfm_no_network:$PWD${PYTHONPATH:+:$PYTHONPATH}"
python -c 'import sitecustomize; assert sitecustomize.GUARD_ACTIVE'
```

Python imports `sitecustomize.py` during interpreter startup. The guard denies
IPv4 and IPv6 socket connection attempts, connected and destination-bearing
socket sends, direct resolver entry points, and `urllib` URL opens while leaving
Unix-domain sockets available for local test harnesses. It is inactive unless
`KFM_NO_NETWORK` is exactly `1`.

When active, the public `socket.SocketType` alias, the private
`_socket.SocketType` alias, and direct construction through the private
`_socket.socket` module entry point are routed through the guarded
`socket.socket` subclass. Other private extension factories and APIs remain
outside this bounded constructor proof.

This is process-startup enforcement, not an operating-system firewall,
container policy, network namespace, runner-wide sandbox, dependency-install
control, or proof that non-Python commands cannot reach a network. A workflow
using it must keep those limits explicit and run a negative probe at the exact
revision under review.
