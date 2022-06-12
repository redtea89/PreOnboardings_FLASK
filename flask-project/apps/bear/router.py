from .views import (
    GroupCLView,
    GroupRUDView,
    RestaurantCLView,
    RestaurantRUDView,
    KpiPerRestaurantView,
    KpiPerPaymentView,
    KpiPerPartysizeView
)

def bear_router(api):
    api.add_resource(GroupCLView, '/api/v1/bear/groups')
    api.add_resource(GroupRUDView, '/api/v1/bear/groups/<int:pk>')
    api.add_resource(RestaurantCLView, '/api/v1/bear/restaurants')
    api.add_resource(RestaurantRUDView, '/api/v1/bear/restaurants/<int:pk>')
    api.add_resource(KpiPerRestaurantView, '/api/v1/bear/kpi/restaurant')
    api.add_resource(KpiPerPaymentView, '/api/v1/bear/kpi/payment')
    api.add_resource(KpiPerPartysizeView, '/api/v1/bear/kpi/partysize')