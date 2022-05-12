from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("view_categories", views.view_categories, name="view_categories"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("add_listing", views.add_listing, name="add_listing"),
    path("<int:listing_id>/edit_listing", views.edit_listing, name="edit_listing"),
    path("<int:listing_id>", views.view_listing, name="view_listing"),
    path("<int:listing_id>/submit_bid", views.submit_bid, name="submit_bid"),
    path("<int:listing_id>/close_listing", views.close_listing, name="close_listing"),
    path("<int:listing_id>/add_comment", views.add_comment, name="add_comment")


]
