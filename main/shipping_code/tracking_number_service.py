import re

from main.shipping_code.delivery_service_company_requester import DeliveryServiceCompanyRequester
from main.shipping_code.resource.tracking_number_pattern import TrackingNumberPattern
from main.shipping_code.resource.tracking_url import TrackingUrl

delivery_service_requester = DeliveryServiceCompanyRequester()
class TrackingNumberService:
    pass

    def get_shipping_info(self, tracking_number):
        delivery_service_company_list = self.find_delivery_service_company_by_tracking_number(tracking_number)

        for delivery_service_company in delivery_service_company_list:
            self.get_tracking_info_response(tracking_number, delivery_service_company)

    def find_delivery_service_company_by_tracking_number(self, tracking_number) -> list:
        matched_companies = set()
        tracking_number_patterns = TrackingNumberPattern.tracking_number_patterns
        for company, pattern in tracking_number_patterns.items():
            if re.match(pattern, tracking_number):
                matched_companies.add(company)
        return list(matched_companies)

    def get_tracking_info_response(self, tracking_number, company):

        return delivery_service_requester.get_delivery_info(tracking_number, company)
