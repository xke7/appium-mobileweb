#!/usr/bin/env bash

PACKAGE_TO_TEST=$1

if [ "$#" = 0 ]; then
    echo "Error -> Missing parameter to run"
    echo "Please run with ./permissions.sh <package>"
    exit 0
fi

ADB=${ANDROID_HOME}/platform-tools/adb
DEVICES=$(${ADB} devices | grep -v 'List of devices' | cut -f1 | grep '.')

for device in ${DEVICES}; do
    ${ADB} -s ${device} shell pm grant ${PACKAGE_TO_TEST} android.permission.ACCESS_FINE_LOCATION
    ${ADB} -s ${device} shell pm grant ${PACKAGE_TO_TEST} android.permission.READ_CONTACTS
    ${ADB} -s ${device} shell pm grant ${PACKAGE_TO_TEST} android.permission.WRITE_CALENDAR
    ${ADB} -s ${device} shell pm grant ${PACKAGE_TO_TEST} android.permission.GET_ACCOUNTS
done
