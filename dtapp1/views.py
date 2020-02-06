from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def wish(request):
    date = datetime.datetime.now()
    msg = 'Hello Guest !!! Very Very good '
    h = int(date.strftime('%H'))
    if h < 12:
        msg += 'Morning!'
    elif h < 16:
        msg += 'Afternoon!!'
    elif h < 21:
        msg += 'Evening!!!'
    else:
        msg ='Hello Guest !!!! Very Very Good Night!!'
    my_dict = {'insert_date': date, 'insert_msg': msg}
    return render(request, 'wish.html', context=my_dict)