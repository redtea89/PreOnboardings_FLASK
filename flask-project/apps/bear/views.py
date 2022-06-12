from flask_restful import Resource


class KpiPerRestaurantView(Resource):
    """
    [GET] time window와 그룹이름과 기간과 가격범위로 레스토랑별 총 매출 리턴
     - params[필수] = "time_window", "start_time", "end_time"
     - params[옵션] = "start_price", "end_price", "Restaurant_group"
    """
    def get(self):
        pass


class KpiPerPaymentView(Resource):
    """
    [GET] time window와 그룹이름과 기간과 가격범위로 레스토랑별 총 매출 리턴
     - params = "time_window", "number_of_party", "start_time", "end_time"
                "start_price", "end_price", "group_name"
    """
    def get(self):
        pass


class KpiPerPartysizeView(Resource):
    """
    [GET] time window와 그룹이름과 기간과 가격범위로 레스토랑별 총 매출 리턴
     - params = "time_window", "number_of_party", "start_time", "end_time"
                "start_price", "end_price", "group_name"
    """
    def get(self):
        pass


class GroupCLView(Resource):
    """
    [GET] : 프랜차이즈 그룹 리스트 보기
    [POST] : 프랜차이즈 그룹 추가
    """
    def get(self):
        pass

    def post(self):
        pass


class GroupRUDView(Resource):
    """
    [GET] : id로 개별 프랜차이즈 그룹 보기
    [PUT] : id로 개별 프랜차이즈 그룹 정보 업데이트
    [DELETE] : id로 개별 프랜차이즈 그룹 삭제
    """
    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class RestaurantCLView(Resource):
    """
    [GET] : 점포 리스트 보기
    [POST] : 점포 추가
    """
    def get(self):
        pass

    def post(self):
        pass


class RestaurantRUDView(Resource):
    """
    [GET] : id로 개별 점포 보기
    [PUT] : id로 개별 점포 정보 업데이트
    [DELETE] : id로 개별 점포 삭제
    """
    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass