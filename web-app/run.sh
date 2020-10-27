#!/usr/bin/env bash
export IS_DEBUG=${DEBUG:-false}
exec gunicorn -b :${PORT:-5001} --timeout 600 --access-logfile - --error-logfile - run:application