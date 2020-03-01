from rest_framework import routers
from rental import api_views as rental_views

router = routers.DefaultRouter()
router.register(r'friends', rental_views.FriendView)
router.register(r'belongings', rental_views.BelongingViewSet)
router.register(r'borrowings', rental_views.BorrowedViewSet)