from django.shortcuts import render

# Create your views here.
def interface(request):
    # result = 0

    # if request.method == "POST":
    #     try:
    #         num1 = float(request.POST.get("num1",0))
    #         num2 = float(request.POST.get("num2",0))
    #         operation = str(request.POST.get('operation', 'add'))
    #     except ValueError:
    #         result = "Invalid input"

    #     if operation == 'add':
    #         result = num1 + num2
    #     elif operation == 'subtract':
    #         result = num1 - num2
    #     elif operation == 'multiply':
    #         result = num1 * num2
    #     elif operation == 'divide':
    #         result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    #     else:
    #         result = "Invalid operation"


    #     return render(request,"Simple_calculator/interface.html",{"result" : result})
    
    return render(request,"Simple_calculator/interface.html")
 