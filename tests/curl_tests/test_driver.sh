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

if [ "$#" -ne 3 ]; then
	echo "Usage: $0 [host-name] [port-number] [servicePID]"
	echo ""
	echo "Example: $0 fulgentcorp.com 8080 17000"
	exit 1
fi

# Sleep for 5 seconds before running the test, this prevents a connection
# refused error from curl during the pipeline stage
sleep 5

# Make hostname and port number available to other test scripts
host_name="$1"
export host_name

port_number="$2"
export port_number

# Assume pass
test_result=0

# Run all tests, stopping if one returns a nonzero error code
for test_script in "${test_scripts[@]}"; do
	bash "$test_script" || { 
		echo "STOPPING TEST..." ; 
		test_result=1 ;
		break;
	}
done

# Kill the server before exit
kill -9 $3
echo "Service killed..."

exit $test_result
