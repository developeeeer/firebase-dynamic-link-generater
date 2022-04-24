# Install & Execution
1. git clone
2. pip install -r requirements.txt
3. .env create
```commandline
# .env file
API_KEY=xxx
BASE_DOMAIN_URI_PREFIX=xxx
ANDROID_PACKAGE_NAME=xxx
IOS_BUNDLE_ID=xxx
IOS_CUSTOM_SCHEME=xxx
IOS_IPAD_BUNDLE_ID=xxx
IOS_APP_STORE_ID=xxx
SOCIAL_IMAGE_LINK=xxx
SERVICE_BASE_URL=xxx
```
4. 処理対象のファイルを {project}/config/target_list.csvとして保存する
```commandline
# csvのColumn設計
email, username, id
```
5. mainを実行

