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

if [ "$#" -ne 2 ]; then
	echo "Usage: $0 [host-name] [port-number]"
	echo ""
	echo "Example: $0 fulgentcorp.com 8080"
	exit 1
fi

# Make hostname and port number available to other test scripts
host_name="$1"
export host_name

port_number="$2"
export port_number

# Start up the server
python3 ../../main.py -i $host_name -p $port_number &
servicePID=$!

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
kill -9 $servicePID

exit $test_result
