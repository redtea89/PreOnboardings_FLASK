from flask_restful import Resource


class AnalysisView(Resource):
    """
    [GET] 광고주 id와 기간으로 매체별 통계량 리턴
     - params = "advertiser_id", "start_date", "end_date"
    """
    def get(self):
        pass


class AdvertiserCLView(Resource):
    """
    [GET] : 광고주 리스트 보기
    [POST] : 광고주 추가
    """
    def get(self):
        pass

    def post(self):
        pass


class AdvertiserRUDView(Resource):
    """
    [GET] : id로 개별 광고주 보기
    [PUT] : id로 개별 광고주 정보 업데이트
    [DELETE] : id로 개별 광고주 삭제
    """
    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
