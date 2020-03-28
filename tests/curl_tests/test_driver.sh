#!/usr/bin/env bash

# ==========================================
# Driver script for black-box endpoint tests
# ==========================================

# Names and order of all test scripts to run
test_scripts=(
	test_get_all.sh
	test_get_by_id.sh
	test_post.sh
	test_put.sh
	test_delete.sh
)

# Run all tests, stopping if one returns a nonzero error code
for test_script in "${test_scripts[@]}"; do
	bash "$test_script" || { echo "STOPPING TEST..." ; exit 1; }
done
