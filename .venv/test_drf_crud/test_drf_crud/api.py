from rest_framework import routers
from api_crud.views import M1Viewset, M2Viewset, BorrowedViewset

router = routers.DefaultRouter()
router.register(r'M1Viewset', M1Viewset)
router.register(r'M2Viewset', M2Viewset)
router.register(r'BorrowedViewset', BorrowedViewset)