from main.models import URLTracker


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        return response


class URLTrackerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # # counter = 10
        # url_tracker = URLTracker.objects.filter(path=request.path).last()
        # if url_tracker.exists():
        #     from time import sleep
        #     sleep(10)
        #     # user_1: counter = 10
        #     # user_2: counter = 10
        #     url_tracker.counter += 1
        #     url_tracker.save()
        #     # counter = 11
        # else:
        #     url_tracker = URLTracker(path=request.path, counter=1)
        #     url_tracker.save()

        # from annoying.functions import get_object_or_None
        # url_tracker = get_object_or_None(URLTracker, path=request.path)
        # if url_tracker:
        #     url_tracker.counter += 1
        #     url_tracker.save()
        # else:
        #

        # from django.db.models import F
        # from annoying.functions import get_object_or_None
        # url_tracker = get_object_or_None(URLTracker, path=request.path)
        # if url_tracker:
        #     # update url_tracker set counter = counter + 1
        #     url_tracker.counter = F('counter') + 1
        #     url_tracker.save()
        # else:
        #     URLTracker.objects.create(path=request.path, counter=1)

        from django.db.models import F
        url_tracker, created = URLTracker.objects.get_or_create(
            path=request.path
        )
        # created       - new: counter = 1
        # not created   - old: counter = 10
        if not created:
            # update url_tracker set counter = counter + 1
            url_tracker.counter = F('counter') + 1
            url_tracker.save()

        return response
