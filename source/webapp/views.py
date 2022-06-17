from django.shortcuts import render


# Create your views here.

def index(request):
    global result
    if request.method == "GET":
        return render(request, "index.html")
    else:
        first = int(request.POST.get("firstnum"))
        second = int(request.POST.get("secondnum"))
        symbol = request.POST.get("symbol")
        if symbol == "+":
            result = first + second
        if symbol == "-":
            result = first - second
        if symbol == "*":
            result = first * second
        if symbol == "/":
            result = first / second

        context = {
            "firstnum": request.POST.get("firstnum"),
            "secondnum": request.POST.get("secondnum"),
            "symbol": symbol,
            "result": result,
        }

        return render(request, "result_view.html", context)
