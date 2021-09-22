from flask_restful import Resource, reqparse
import whois
from utils.return_response import  return_json
import json
from flask import current_app, jsonify, request


class Domain(Resource):

    def post(self):
        try:
            # Validate form
            parser = reqparse.RequestParser()
            parser.add_argument(
                'domain', type=str, required=True, location='json')
           
            body = parser.parse_args()
        except ValueError:
            print(f"[Error] {ValueError}")
             # Returns error
            return return_error_json(status=400, json= {
                "status": False,
                "error": "F001",
                "message": "Missing some required field."
            })

        d = whois.whois(body['domain'])

        """ result = {
            "domainName": d['domain_name'][1],
            "creationDate": d['creation_date'][0],
            "expirationDate": d['expiration_date'][0],
            "updatedDate": d['updated_date'][0],
            "registrar": d['registrar'],
            "owner": d['name'],
            "whoisServer": d['whois_server'],
            "country": d["country"],
            "state": d['state'],
            "city": d['city'],
            "address": d['address']

        }"""

        return  jsonify(d);
