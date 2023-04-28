from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode
from urllib.parse import urlunparse
from django.utils import timezone
from social_core.exceptions import AuthForbidden
import requests
import shutil
from .models import DealUserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    api_url = urlunparse(('https',
                          'api.vk.com',
                          '/method/users.get',
                          None,
                          urlencode(OrderedDict(
                              fields=','.join(('about', 'bdate', 'sex',
                                               'photo_200')),
                              access_token=response['access_token'],
                              v='5.131')),
                          None
                          ))

    resp = requests.get(api_url)
    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]

    if data['sex']:
        user.dealuserprofile.gender = DealUserProfile.MALE if \
            data['sex'] == 2 else DealUserProfile.FEMALE

    if data['about']:
        user.dealuserprofile.aboutMe = data['about']

    # if data['photo_200']:
    #     # pass
    #     # user.dealuserprofile.aboutMe = data['photo_200']
    #     # user.avatar = data['photo_200']
    #     url = data['photo_200']
    #     print(url)
    #
    #     r = requests.get(url, stream=True)
    #     with open('/media/user_avatars/' + str(data['id']) + '.png',
    #               'wb') as out_file:
    #         shutil.copyfileobj(r.raw, out_file)
    #     del r

    if data['bdate']:
        bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()

        age = timezone.now().date().year - bdate.year
        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')

    user.save()
