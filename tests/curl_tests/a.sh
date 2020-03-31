source ./curl_util.sh

url="http://cs47832.fulgentcorp.com:12186/properties"

curl_http "GET" "$url" "" ""

if [ $? -ne 0 ]; then
	echo "curl_http failed"
fi

cat resp.json
rm resp.json
exit 0
