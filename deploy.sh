# Very simple script that moves the code to the deployment server

# Makes a zip file
zip devops.zip *.py *.db static/swagger.json || exit 1

# Uses scp to move the zip file to the server
scp devops.zip ddd233@cs47831.fulgentcorp.com:~/ || exit 1

# Connects to the server via ssh and sets up the new code
ssh ddd233@cs47831.fulgentcorp.com << EOF
	bash ~/upgrade.sh
EOF

# Remove the zip file on local system
rm devops.zip
