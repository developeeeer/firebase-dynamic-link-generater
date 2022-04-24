from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))

# setup .env
API_KEY = os.getenv("API_KEY")
BASE_DOMAIN_URI_PREFIX = os.getenv("BASE_DOMAIN_URI_PREFIX")
ANDROID_PACKAGE_NAME = os.getenv("ANDROID_PACKAGE_NAME")
IOS_BUNDLE_ID = os.getenv("IOS_BUNDLE_ID")
IOS_CUSTOM_SCHEME = os.getenv("IOS_CUSTOM_SCHEME")
IOS_IPAD_BUNDLE_ID = os.getenv("IOS_IPAD_BUNDLE_ID")
IOS_APP_STORE_ID = os.getenv("IOS_APP_STORE_ID")
SOCIAL_IMAGE_LINK = os.getenv("SOCIAL_IMAGE_ßLINK")

BASE_URL = os.getcwd()

SERVICE_BASE_URL = os.getenv('SERVICE_BASE_URL')

END_POINT = rf"https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key={API_KEY}"
HEADERS = {"Content-Type": "application/json"}
DEFAULT_PARAMS = {
"dynamicLinkInfo": {
    "domainUriPrefix": BASE_DOMAIN_URI_PREFIX,
    "link": "",
    "androidInfo": {
      "androidPackageName": ANDROID_PACKAGE_NAME,
    },
    "iosInfo": {
      "iosBundleId": IOS_BUNDLE_ID,
      "iosCustomScheme": IOS_CUSTOM_SCHEME,
      "iosIpadBundleId": IOS_IPAD_BUNDLE_ID,
      "iosAppStoreId": IOS_APP_STORE_ID,
    },
    "navigationInfo": {
      "enableForcedRedirect": False,
    },
    "socialMetaTagInfo": {
      "socialTitle": "",
      "socialDescription": "",
      "socialImageLink": SOCIAL_IMAGE_LINK
    }
  },
  "suffix": {
    "option": "UNGUESSABLE"
  }
}

DEFAULT_PARAMS_LONG_DYNAMIC_LINK = {
   "longDynamicLink": f"{BASE_DOMAIN_URI_PREFIX}"
                      f"?apn={ANDROID_PACKAGE_NAME}"
                      f"&ibi={IOS_BUNDLE_ID}",
   "suffix": {
     "option": "UNGUESSABLE"
   }
}