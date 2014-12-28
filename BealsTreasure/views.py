from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "BealsTreasure/home.html")

def status(request):
    return render(request, "BealsTreasure/status.html")

def faq(request):
    return render(request, "BealsTreasure/faq.html")

def about(request):
    return render(request, "BealsTreasure/about.html")

def contact(request):
    return render(request, "BealsTreasure/contact.html")

def faq_prize(request):
    return render(request, "BealsTreasure/faq/prize.html")

def faq_conjecture_what(request):
    return render(request, "BealsTreasure/faq/conjecture-what.html")

def faq_what_if_conjecture_true(request):
    return render(request, "BealsTreasure/faq/what-if-conjecture-true.html")

def faq_why_do_you_need_me(request):
    return render(request, "BealsTreasure/faq/why-do-you-need-me.html")

def faq_will_slow_down_my_computer(request):
    return render(request, "BealsTreasure/faq/will-slow-down-my-computer.html")

def faq_download_data(request):
    return render(request, "BealsTreasure/faq/download-data.html")

def faq_are_you_a_hacker(request):
    return render(request, "BealsTreasure/faq/are-you-a-hacker.html")

def faq_do_i_need_to_know_math(request):
    return render(request, "BealsTreasure/faq/do-i-need-to-know-math.html")

def faq_how_can_i_join(request):
    return render(request, "BealsTreasure/faq/how-can-i-join.html")

def faq_i_found_something(request):
    return render(request, "BealsTreasure/faq/i-found-something.html")

def faq_donations(request):
    return render(request, "BealsTreasure/faq/donations.html")