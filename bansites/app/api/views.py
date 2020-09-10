from rest_framework import generics
from .serializer import SiteSerializer
from ..models import SiteModel
from rest_framework.views import APIView
from rest_framework.response import Response
from .url_search import search_url

class SiteView(generics.ListCreateAPIView):
    queryset = SiteModel.objects.all()
    serializer_class = SiteSerializer


class SiteSearchAPIView(APIView):

    def get(self, request):
        #print(self.request.query_params)
        #hm kre?
        # ha ji
        param = self.request.query_params
        url = param['url']
        print(url)
        search_url(url)
        # abhi kuch reteurn nhi krte hai.
