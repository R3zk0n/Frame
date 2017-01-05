#!/bin/bash
if [ $# -eq 2 ]
then
	echo 'TLS/SSL..'
	echo "Running TLSSLED.."
	tlssled $1 $2
	exit
else

echo 'Would you like to run DIRB > [Y/N] '
read DIRB
if [ $DIRB == 'Y' ]
then
	echo 'Running DIRB'
	dirb http://$1
fi


	echo 'CISCO Auditing TOOL..'
	CAT -h $1
	echo

	echo 'Running IKE-SCAN kev1..'
	ike-scan $1
	echo

	echo "Running IKE-SCAN kev2"
	ike-scan --ikev2 $1
	echo 
	exit
fi
