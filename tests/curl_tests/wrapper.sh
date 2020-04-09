# Runs as part of the pipeline. Start the service locally runs the curl tests
# and kills the server
servicePID=$!
./test_driver.sh localhost 12188
test_result=$?
kill -9 $servicePID
echo "Service shut down, ending stage..."
exit $test_result
