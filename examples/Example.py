from tfd_py import Config, Uoid
from tfd_py.api import BasicInformation
import asyncio

configuration = Config(
    api_key='YOUR_API_KEY_HERE', # Replace with your actual API key otherwise it will throw an error
    # Language can be be changed to any of the following: ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es
    # Default is 'en' (English)
    language='en'
    )

async def main():
    username=input("Enter your TFD name: ")
    #Fetches the uoid for the given TFD name
    ouid = await Uoid.get(username)
    #Fetches the basic information for the given uoid
    information = await BasicInformation.get(ouid)
    #Fetches the formatted basic information for the given uoid
    information_formatted = await BasicInformation.get_formatted(ouid)
    print(information)
    print(information_formatted)

if __name__ == "__main__":
    asyncio.run(main())