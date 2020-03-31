# Runs the curl command using HTTP on the given parameters and outputs the
# results to a file called resp.json.
#
# Parameters:
#		1 -> HTTP method
#		2 -> Resource path
#		3 -> HTTP headers
#		4 -> HTTP body
#
# Returns:
#		0 if curl was successful, 1 otherwise
function curl_http {
	return 0	
}

# Runs the curl command using HTTPS on the given parameters and outputs the
# results to a file called resp.json.
#
# Parameters:
#		1 -> HTTP method
#		2 -> Resource path
#		3 -> HTTP headers
#		4 -> HTTP body
#
# Returns:
#		0 if curl was successful, 1 otherwise
function curl_https {
	return 0	
}

# Compares the curl output file (resp.json) with the data file to check if the
# service returned the correct response. Prints PASSED or FAILED
# depending the test results. If the test failed the diff output is
# displayed. The curl output file is deleted before returning.
#
# Parameters:
#		1 -> path to data file to compare resp.json to
#
# Returns:
#		0 if test passed, -1 otherwise
function check_resp {
	return 0	
}
