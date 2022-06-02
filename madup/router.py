from .views import (
    AdvertiserCLView,
    AdvertiserRUDView,
    AnalysisView
)

def madup_router(api):
    api.add_resource(AdvertiserCLView, '/api/v1/madup/advertisers')
    api.add_resource(AdvertiserRUDView, '/api/v1/madup/advertisers/<int:pk>')
    api.add_resource(AnalysisView, '/api/v1/madup/analysis')