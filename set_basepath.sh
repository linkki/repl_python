#!/bin/sh
prod_base_path="https://linkki.github.io/"
local_base_path="http://localhost:"
local_port="8000" || $2

update_base_path() {
  base_path=$1
  sed -i 's,<base href=".*">,<base href="'"${base_path}"'">,' template.html \
  && echo "Base path is now: $1"
  python3 update_html.py index.html perusasiat/*
}

[ "$1" = "prod" ] && update_base_path ${prod_base_path} && exit 0
[ "$1" = "dev" ] && update_base_path ${local_base_path}${local_port} && exit 0

echo "Invalid arguments... \
      \nfirst argument should be 'prod' or 'dev' \
      \nsecond argument should be localhost port (optional, default: 8000)"
