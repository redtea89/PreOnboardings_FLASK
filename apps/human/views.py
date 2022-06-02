from flask_restful import Resource


class ResearchCLView(Resource):
    """
    [GET] : 임상정보 리스트 보기
    [POST] : 임상정보 추가
    """
    pass


class ResearchRUDView(Resource):
    """
    [GET] : id로 개별 임상정보 보기
    [PUT] : id로 개별 임상정보 정보 업데이트
    [DELETE] : id로 개별 임상정보 삭제
    """
    pass