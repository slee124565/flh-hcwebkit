
from django.views.generic import View
from django.http import HttpResponse, Http404

import logging
logger = logging.getLogger(__name__)

from django.conf import settings
import requests
from requests.auth import HTTPBasicAuth

class ApiSceneView(View):

    def get(self, request, name=None, *args, **kwargs):
        #logger.debug('%s' % settings.FIBARO_HOMECENTER['scenes'])
        try:
            name = name.lower()
            logger.info('start scene name: %s ...' % str(name))
            if name in settings.FIBARO_HOMECENTER['scenes'].keys():
                scene_id = settings.FIBARO_HOMECENTER['scenes'][name]['id']
                hostname = settings.FIBARO_HOMECENTER['hostname']
                account = settings.FIBARO_HOMECENTER['account']
                password = settings.FIBARO_HOMECENTER['password']
                api_path = 'http://%s/api/sceneControl?id=%s&action=start' % (
                                                                        hostname,
                                                                        scene_id)
                r = requests.get(api_path, 
                             auth=HTTPBasicAuth(account, password))
                logger.info('request response %s, %s' % (r.status_code, r.text))
                
                return HttpResponse('OK')
            else:
                logger.warning('scene name [%s] not found' % name)
                #raise Http404
                return HttpResponse('Fail')
        except:
            logger.error('exception', exc_info=True)
            #raise Http404
            return HttpResponse('Exception')

class ApiGoodbyeView(View):
    
    def get(self, request, *args, **kwargs):
        scene_id = 150
        hostname = settings.FIBARO_HOMECENTER['hostname']
        account = settings.FIBARO_HOMECENTER['account']
        password = settings.FIBARO_HOMECENTER['password']
        api_path = 'http://%s/api/sceneControl?id=%s&action=start' % (
                                                                hostname,
                                                                scene_id)
        r = requests.get(api_path, 
                     auth=HTTPBasicAuth(account, password))
        logger.info('request response %s, %s' % (r.status_code, r.text))
        
        return HttpResponse('OK')
        
#Disarm the system
class ApiDisarmSystemView(View):
    
    def get(self, request, *args, **kwargs):
        scene_id = 149
        hostname = settings.FIBARO_HOMECENTER['hostname']
        account = settings.FIBARO_HOMECENTER['account']
        password = settings.FIBARO_HOMECENTER['password']
        api_path = 'http://%s/api/sceneControl?id=%s&action=start' % (
                                                                hostname,
                                                                scene_id)
        r = requests.get(api_path, 
                     auth=HTTPBasicAuth(account, password))
        logger.info('request response %s, %s' % (r.status_code, r.text))
        
        return HttpResponse('OK')
