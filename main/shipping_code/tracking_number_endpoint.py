from flask import Blueprint

from main.shipping_code.tracking_number_service import TrackingNumberService

tracking_number_blueprint = Blueprint("tracking_number", __name__, url_prefix="/tracking_number")

tracking_service = TrackingNumberService()


@tracking_number_blueprint.route("/<tracking_number>", methods=['GET'])
def find_ship_info_by_shipping_code(tracking_number):

    tracking_service.get_shipping_info(tracking_number)
    company_set = tracking_service.find_delivery_service_company_by_tracking_number(tracking_number)
    return company_set


# app.register_blueprint(shipping_code_blueprint)
#