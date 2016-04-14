Appium Python - Mobile Web Testing
---
## Install
### Install appium [?](http://appium.io/getting-started.html?lang=en)

```shell
# with npm
npm install -g appium

# start appium server
appium
```

### Install python bindings

```shell
# with pip
pip install Appium-Python-Client
pip install pytest
```

### Android set up [?](http://appium.io/slate/en/master/?python#android-setup)

```shell
export ANDROID_HOME=$your_local_sdk
```

## Run test

```shell
py.test google_test.py
```
General steps:

- Connect your device to the PC
- Update the [desired capabilities](http://appium.io/slate/en/master/?python#appium-server-capabilities) with your device info
- Open terminal and start appium in one tab `$ appium`
- Open another tab and run test `py.test google_test.py`

## Write tests
See API documents for appium client library `python`
[Appium Python](http://appium.io/slate/en/master/?python#appium-client-libraries)

