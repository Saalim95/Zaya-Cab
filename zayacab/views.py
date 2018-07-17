from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

def index(request):
    return render(request, 'zayacab/index.html')

# URL: zayacab/driver/register
# POST Params: [username, password]
class RegisterDriver(APIView):

    def post(self, request):
        serializer = UserSerializer(data = request.data)     
        if serializer.is_valid():
            data = serializer.data
            try:
                user = User.objects.create_user(username=data['username'], password=['password'])
                user.save()
            except:
                return Response({"error": "Username already exists"})
            driver = Driver.objects.create(name=data['username'], user=user)
            driver.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Invalid Params or username may already exist"})

# URL: zayacab/user/register 
# POST Params: [username, password]
class RegisterUser(APIView):

    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            data = serializer.data
            try:
                user = User.objects.create_user(username=data['username'], password=['password'])
                user.save()
            except:
                return Response({"error": "Username already exists"})
            commuter = Commuter.objects.create(name=data["username"], user=user)
            commuter.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Invalid Params or username may already exist"})


#URL: zayacab/booking/<commuter_id>/<driver_id>
#POST: Params [source, destination, fare]
@api_view(['POST'])
def BookCab(request, commuter_id, driver_id):
    try:
        commuter = Commuter.objects.get(id=commuter_id)
    except:
        return Response({"error": "Commuter with this ID does not exist"})
    try:
        driver = Driver.objects.get(id=driver_id)
    except:
        return Response({"error": "Driver with this ID {} does not exist".format(driver_id)})
    if driver.status == "AV":
        driver.status = "BK"
        driver.save()
        trip = Trip.objects.create(commuter=commuter, driver=driver)
        serializer = TripSerialier(trip, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"error": "Invalid params"})
    elif driver.status == "BK":
        return Response({"error": "Driver with {} is already booked".format(driver_id)})
    else:
        return Response("Driver with {} is Offline".format(driver_id))


#URL: /zayacab/driver/available
@api_view(['GET'])
def DiversAvailable(request):
    if request.method == 'GET':
        drivers = Driver.objects.filter(status="AV")
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data)


#URL: /zayacab/user/<commuter_id>/history
@api_view(['GET'])
def TripHistoryUser(request, commuter_id):
    if request.method == 'GET':
        try:
            commuter = Commuter.objects.get(id=commuter_id)
        except:
            return Response({"error": "Driver with ID {} is unavailable".format(commuter_id)})
        trips = Trip.objects.filter(commuter=commuter)
        serializer = TripUserSerializer(trips, many=True)
        return Response(serializer.data)


# URL: /zayacab/driver/<driver_id>/history
@api_view(['GET'])
def TripHistoryDriver(request, driver_id):
    if request.method == 'GET':
        try:
            driver = Driver.objects.get(id=driver_id)
        except:
            return Response({"error": "Driver with ID {} is unavailable".format(driver_id)})
        trips = Trip.objects.filter(driver=driver)
        serializer = TripDriverSerializer(trips, many=True)
        return Response(serializer.data)


# URL: /zayacab/update/<driver_id>
# POST Params: [status]
# status choices: ['AV', 'BK', 'OFF]
@api_view(['POST'])
def ChangeStatus(request, driver_id):
    if request.method == 'POST':
        try:
            d = Driver.objects.get(id=driver_id)
        except:
            return Response({"error": "Driver with ID {} does not exist".format(driver_id)})
        serializer = DriverSerializer(d, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"error": "Invalid params"})


# URL: /zayacab/user/location/commuter_id
# POST Params [lat, long]
@api_view(['GET', 'POST'])
def UserLocation(request, commuter_id):
    try:
        commuter = Commuter.objects.get(id=commuter_id)
    except:
        return Response({"error": "commuter with ID {} does not exist".format(commuter_id)})
    if request.method == 'GET':
        serializer = UserLocationSerializer(commuter)
        return Response(serializer.data)
    else:
        serializer = UserLocationSerializer(commuter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"error": "Invalid params"})

