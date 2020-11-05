from .models import *

notification_details = ["Tayo liked your post on Instagram.", "Funmilayo unfollowed you.", "Bidemi ate your bread."]

def populate():
    for detail in notification_details:
        Notification.objects.create(details=detail)
        print(f"created notification --- {notification_details.index(detail)} -- successful")