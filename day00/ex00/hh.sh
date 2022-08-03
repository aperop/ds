#!/bin/sh

role_name="${1/ /+}"
curl -s -k -H 'User-Agent: api-test-agent' "https://api.hh.ru/vacancies?text=$role_name&per_page=20" | jq > hh.json
