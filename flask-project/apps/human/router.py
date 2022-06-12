from .views import (
    ResearchCLView,
    ResearchRUDView
)

def human_router(api):
    api.add_resource(ResearchCLView, '/api/v1/madup/researches')
    api.add_resource(ResearchRUDView, '/api/v1/madup/researches/<int:pk>')