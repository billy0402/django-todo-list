from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def root(request):
    s = '<h1>Hello World</h1>'
    return HttpResponse(s)


def request_test(request):
    # http://127.0.0.1:8000/tutorial/request_test/?s1=Hello&s2=World
    s1 = request.GET.get('s1')
    s2 = request.GET.get('s2')
    return HttpResponse('<h1>{} {}</h1>'.format(s1, s2))


def render_test(request,n1,n2):
    score = n1 + n2
    return render(request,'render_test.html', {
        'score': score
    })


def homework(request, start, stop, base):
    num_array = []
    is_reversed = False

    if start > stop:
        # x = start
        # start = stop
        # stop = x
        start, stop = stop, start
        is_reversed = True

    num_range = range(start,stop+1)
    if is_reversed:
        num_range = reversed(num_range)

    if base == 1:
        for num in num_range:
            if num%2 == 1:
                num_array.append(num)
    else:
        for num in num_range:
            if num%2 == 0:
                num_array.append(num)

    return render(request,'homework.html',{
        'num_array': num_array
    })
