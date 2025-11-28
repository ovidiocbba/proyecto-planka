


class AssertionStatusCode:    

    @staticmethod
    def assert_status_code_200(response):
        assert response.status_code == 200


    @staticmethod
    def assert_status_code_400(response):
        assert response.status_code == 400

    @staticmethod
    def assert_status_code_401(response):
        assert response.status_code == 401

    @staticmethod
    def assert_status_code_404(response):
        assert response.status_code == 404

    @staticmethod
    def assert_status_code_400_or_404(response):
        assert response.status_code == 400 or response.status_code == 404