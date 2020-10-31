
# * made this file to make database functions  that will work upon the mail
#!BETTER CoMMENTS TO BE USED DOWNLOAD IT HERE -> https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments


def check_if_key_is_valid(ids):
    from datetime import datetime, timedelta, timezone
    for id in ids.objects.all():
        # print(ids.objects.all())
        if datetime.now(tz=timezone.utc) - \
                id.time_created > timedelta(hours=2):
            p = id.unique_id
            pk = id.pk
            id.delete()
            print(f"ID {pk} with unique id -{p} has been deleted")
            return False
        else:
            # print("ID IS VALID")
            return True
