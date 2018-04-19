#!/usr/bin/env bash
cat docker-entrypoint-initdb.d/dbsetup.sql | mysql -uroot
