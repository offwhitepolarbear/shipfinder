import json

import aiohttp
import urllib3
from bs4 import BeautifulSoup

from main.shipping_code.resource.tracking_url import TrackingUrl

http = urllib3.PoolManager()


class DeliveryServiceCompanyRequester:

    def get_delivery_info(self, tracking_number, company):
        url_infos = TrackingUrl.url_list
        url = url_infos.get(company)
        if url is not None:
            response = http.request("GET", url+tracking_number)
            print(response.url)
            # print(response.getheaders())
            json_response = "application/json" in response.getheader("Content-Type")
            print(response.status)
            if response.status == 200:

                response_data = response.data.decode("utf-8")

                if company == "우체국":
                    self.kr_post_response_parser(response_data)

                if json_response:
                    print(json.loads(response_data).get("info"))
                else:
                    pass
                    # print(response_data)
            # print(response.json())
            # async with aiohttp.ClientSession() as session:
            #     async with session.get(delivery_url) as response:
            #         if response.status == 200:
            #             print(response)

    def kr_post_response_parser(self, response):
        soup = BeautifulSoup(response, "html.parser")
        tbody_list = soup.find_all("tbody")
        for tbody in tbody_list:
            print(tbody.text)