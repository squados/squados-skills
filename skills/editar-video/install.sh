#!/bin/sh
set -eu
skill_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
exec python3 "$skill_dir/scripts/install.py" "$@"
