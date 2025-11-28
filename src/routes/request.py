import requests


class PlankaRequests:
    @staticmethod
    def post(url,headers,payload=None):
        response = requests.post(url, headers=headers, json=payload)
        return response

    @staticmethod
    def get(url,headers):
        response = requests.get(url, headers=headers)
        return response
    
    @staticmethod
    def delete(url,headers):
        response = requests.delete(url, headers=headers)
        return response