from notifications.models import Notification

def get_notific_nao_lidas(user):
    unread_notifications = Notification.objects.unread().filter(recipient=user)

    return unread_notifications