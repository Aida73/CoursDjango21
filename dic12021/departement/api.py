from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from .models import *
from users.models import *
from .serializers import listeEtudiantsSerializers, LoginUserSerializer, UserLoginSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import BasicAuthentication
from knox.views import LoginView as KnoxLoginView
from knox.auth import AuthToken
from rest_framework.authentication import BasicAuthentication

class LoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication]


@api_view(['GET'])
@permission_classes([IsAuthenticated,])
@authentication_classes([BasicAuthentication,])
def getListeClasse(request,niveau,departement,annee):
    try:
        classe = Classe.objects.get(niveau__niveau=niveau,dept__nom_dept=departement)
    except:
        return Response({"message":"Veuillez verifier les paramètres passés"})
    queryset = Etudiant_Classe.objects.filter(classe=classe,annee_scolaire=annee)
    serializer = listeEtudiantsSerializers(queryset, many=True)
    return Response(serializer.data)
    


@api_view(['POST'])
@permission_classes([AllowAny,])
def myLoginAPI(request):
    
    serializer = LoginUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data
        return Response({
            "user": UserLoginSerializer(user).data,
            "token": AuthToken.objects.create(user)[1]
        })
    else: 
        return Response({
            "message": "Username ou mot de passe incorrect"
        })

@api_view(['GET'])
@authentication_classes([BasicAuthentication,])
def myLoginAPI2(request, format=None):
    content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
    return Response(content)

