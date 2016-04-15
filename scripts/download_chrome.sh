#! /bin/sh

LATEST=`curl -s http://commondatastorage.googleapis.com/chromium-browser-continuous/Android/LAST_CHANGE`

echo Latest Chromium Android at ${LATEST}

TMP_DL='temp'
mkdir -p ${TMP_DL}

REMOTE_APK=http://commondatastorage.googleapis.com/chromium-browser-continuous/Android/${LATEST}/chrome-android.zip

echo Downlaoding ${REMOTE_APK} to ${TMP_DL}
curl ${REMOTE_APK} -o ${TMP_DL}/chrome-android.zip

echo Extracting ChromiumTestShell.apk to ${TMP_DL}
unzip ${TMP_DL}/chrome-android.zip -d ${TMP_DL}/
adb -s emulator-5554 install ${TMP_DL}/chrome-android/apks/ShellTest.apk

rm -r ${TMP_DL}
