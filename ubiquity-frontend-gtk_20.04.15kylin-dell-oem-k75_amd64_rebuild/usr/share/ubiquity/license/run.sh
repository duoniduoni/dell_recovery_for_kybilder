#!/bin/sh
set -e

. /usr/share/debconf/confmodule

db_input high ubiquity/agree_license || true
# db_get ubiquity/use_nonfree
# if [ "$RET" = "true" ]; then
# fi
