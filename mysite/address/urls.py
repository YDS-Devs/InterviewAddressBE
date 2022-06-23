from rest_framework_nested import routers

from .views import AreaViewSet, StateViewSet

router = routers.DefaultRouter()
router.register('states', StateViewSet, basename='states')
state_group_router = routers.NestedSimpleRouter(router, 'states', lookup='state')
state_group_router.register('areas', AreaViewSet, basename='state-areas')
urlpatterns = router.urls+state_group_router.urls