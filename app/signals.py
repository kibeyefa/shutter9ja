from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Entry
from django.conf import settings

@receiver(post_save, sender=Entry)
def send_confirmation_email(sender, instance, created, **kwargs):
    if created:
        subject = "Photo Entry Confirmation – Shutter9ja"
        message = f"""
Hello {instance.full_name},

Thank you for registering for the Shutter 9ja Photo Contest — we’re excited to have you on board! 📸
However, this is a gentle reminder that incomplete registrations will be removed.

To remain eligible for the contest, kindly ensure you've:

✅ Followed us on Instagram: https://instagram.com/shutter_9ja
✅ Liked our Facebook page: 
https://facebook.com/profile.php?id=61575508222447&mibextid=wwXIfr&mibextid=wwXIfr

Failure to complete these steps before May 10th, 2025, will result in your account being deleted from the contest.

Let’s make this exciting and fair for everyone.
If you’ve already completed these steps — you’re all set! 🙌

Thank you for being part of the movement!

Here is your entry link, feel free to share it with others. https://shutter9ja.org/entries/{instance.id}

Special Hint: Because you registered early you can start sharing your link to your friends, family and people to vote for you so that you can get the required amount of votes early enough to move into the next phase of the competition 😉.

Warm regards,

– The Shutter9ja Team
"""
        recipient = instance.email

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient],
            fail_silently=False,
        )
