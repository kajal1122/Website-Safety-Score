from rest_framework import generics
from .serializer import SiteSerializer
from .models import SiteModel
from rest_framework.views import APIView
from rest_framework.response import Response
from .url_search import search_url
#from .serializer import SiteSerializer


class SiteView(generics.ListCreateAPIView):
    queryset = SiteModel.objects.all()
    serializer_class = SiteSerializer


class SiteSearchAPIView(APIView):

    def get(self, request):
        print(self.request.query_params)
        #hm kre?
        # ha ji
        print("hjgjhghjgjghjghjhghjg")
        #serializer_class=SiteSearchSerializer
        param = self.request.query_params
        url_get = param['url']
        #print(url)
        result= search_url(url_get)
        data={};
        data['url'] = result[0]
        data['score'] = result[1]
        return Response(data)
        # abhi kuch reteurn nhi krte hai.
