from django.db import connection
from django.shortcuts import HttpResponse
from django.shortcuts import render
import gmpy
import json

from bealstreasure.models import Values, Attempts, Verifys
from bealstreasure import lzstring


# Create your views here.
def index(request):
    return render(request, "bealstreasure/home.html")


def status(request):
    return render(request, "bealstreasure/status.html")


def faq(request):
    return render(request, "bealstreasure/faq.html")


def about(request):
    return render(request, "bealstreasure/about.html")


def contact(request):
    return render(request, "bealstreasure/contact.html")


def faq_prize(request):
    return render(request, "bealstreasure/faq/prize.html")


def faq_conjecture_what(request):
    return render(request, "bealstreasure/faq/conjecture-what.html")


def faq_what_if_conjecture_true(request):
    return render(request, "bealstreasure/faq/what-if-conjecture-true.html")


def faq_why_do_you_need_me(request):
    return render(request, "bealstreasure/faq/why-do-you-need-me.html")


def faq_will_slow_down_my_computer(request):
    return render(request, "bealstreasure/faq/will-slow-down-my-computer.html")


def faq_download_data(request):
    return render(request, "bealstreasure/faq/download-data.html")


def faq_are_you_a_hacker(request):
    return render(request, "bealstreasure/faq/are-you-a-hacker.html")


def faq_do_i_need_to_know_math(request):
    return render(request, "bealstreasure/faq/do-i-need-to-know-math.html")


def faq_how_can_i_join(request):
    return render(request, "bealstreasure/faq/how-can-i-join.html")


def faq_i_found_something(request):
    return render(request, "bealstreasure/faq/i-found-something.html")


def faq_donations(request):
    return render(request, "bealstreasure/faq/donations.html")


def getwork(request):
    x, y, base, uuid = getNewWork(10000, request.GET["username"])
    
    response = {
        'x': x,
        'y': y,
        'base': base,
        'uuid': uuid
    };

    return HttpResponse(json.dumps(response), content_type="application/json")


def getExpValues():
    counts = checkBlock()
    maxs = max(findMaxs())
    exp_x = maxs
    for exp_y in range(3, maxs + 1):
        try:
            counts[exp_x][exp_y]
        except IndexError:
            return exp_x, exp_y

    return exp_x, 3

def getNewWork(max_base, user_id):

    base = 0
    value_id = getUnfinishedBlock()

    if value_id is None:
        exp_x, exp_y = getExpValues()

        values_model = Values(exp_x=exp_x,
                              exp_y=exp_y,
                              max_base=max_base,
                              base=base)

        values_model.save()

        value_id = values_model.id

        attempt_model = Attempts(valuekey=values_model)
        attempt_model.save()

        AttemptKey = attempt_model.id

    else:
        values_model = Values.objects.filter(pk=value_id)

        attempt_model = Attempts(ValueKey=values_model)
        attempt_model.save()

        AttemptKey = attempt_model.id

    return exp_x, exp_y, base, AttemptKey


def checkBlock():
    cursor = connection.cursor()

    cursor.execute(
        '''SELECT COUNT(Verifys.id) as count, attempts.ValueKey as ValueKey
            FROM Verifys,
            attempts WHERE Verifys.AttemptKey = attempts.id
            GROUP BY Verifys.id
            ORDER BY COUNT(Verifys.id)''')

    count = [[]]
    for row in cursor.fetchall():
        count[row['exp_x']][row['exp_y']] = row['count']

    return count


def getUnfinishedBlock():
    cursor = connection.cursor()

    cursor.execute(
        '''SELECT AttemptKey FROM Verifys
            WHERE AttemptKey IN (SELECT AttemptKey FROM
            (SELECT COUNT(id) as count, AttemptKey FROM Verifys
                WHERE AttemptKey IN (SELECT v.AttemptKey FROM Verifys v
                JOIN attempts a ON a.id = v.AttemptKey)
            GROUP BY AttemptKey) AS t)''')

    AttemptKey = cursor.fetchone()

    if AttemptKey == 0:
        AttemptKey = None

    return AttemptKey


def findMaxs():
    cursor = connection.cursor()

    cursor.execute(
        'SELECT MAX(exp_x) as exp_x, MAX(exp_y) as exp_y FROM exp_values')
    row = cursor.fetchone()

    if row[0] == None and row[1] == None:
        return 3, 3

    return row[0], row[1]


def Populate(request):
    count_by = 10

    y, x = findMaxs()

    for exp in xrange(1, max(y, x) + count_by):
        try:
            with open('data/' + str(exp) + '.txt'):
                pass
        except IOError:
            x = lzstring.LZString()

            value = ""
            for base in xrange(1, 10000):
                value += "%s,%s\n" % (str(base), str(gmpy.mpz(base)**exp))

            output = open('data/' + str(exp) + '.txt', 'w')
            output.write(x.compressToBase64(value))
            output.close()

    return HttpResponse("success")


def Completed(request):
    blocks = checkBlock()

    # render(request, "bealstreasure/completed.html")

    return HttpResponse(blocks)
