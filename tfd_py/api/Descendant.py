import aiohttp, traceback, asyncio, orjson
from ..Config import Config


class Descendant:
    @staticmethod
    async def get(ouid: str) -> dict:
        """Method to fetch descendant information for a given username.

        Args:
            ouid (str): The ouid to fetch information for.

        Raises:
            Exception: If the API request fails or the username is invalid.

        Returns:
            dict: The descendant information associated with the username.
        """
        cfg = Config.get()
        url = f"https://open.api.nexon.com/tfd/v1/user/descendant?ouid={ouid}"
        headers = {
            "x-nxopen-api-key": cfg.api_key,
            "accept": "application/json"
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    return data
                else:
                    if cfg.debug:
                        traceback.print_exc()
                    raise Exception(f"Error fetching descendant information: {response.status} - {response.reason}")
        
        return data
    
    # TODO: Implement get_formatted method 
    # resolve the descendant_id to a descendant name and additional information
    # use https://open.api.nexon.com/static/tfd/meta/{language}/descendant.json for descendant information 