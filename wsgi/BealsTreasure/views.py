from django.db import connection
from django.shortcuts import HttpResponse
from django.shortcuts import render
import gmpy

from models import *  # @UnusedWildImport
import lzstring


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


def getwork(request):
    m, n, x, uuid = getNewWork(10000, request.GET["username"])
    response = ""
    response += str(m)
    response += "," + str(n)
    if x != 0:
        response += "," + str(x)

    response += "," + str(uuid)

    return HttpResponse(response)


def getExpValues():
    count = checkBlock()
    maxs = findMax()
    exp_m = maxs + 1
    exp_n = maxs + 1
    for x in xrange(3, maxs + 1):
        for y in xrange(3, maxs + 1):
            try:
                count[x][y]
            except IndexError:
                exp_m = x
                exp_n = y
                return exp_m, exp_n


def getNewWork(max_base, user_id):

    base_x = 0
    value_id = getUnfinishedBlock()

    if value_id is None:
        exp_m, exp_n = getExpValues()

        values_model = Values(exp_m=exp_m,
                              exp_n=exp_n,
                              max_base=max_base,
                              base_x=base_x)

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

    return exp_m, exp_n, base_x, AttemptKey


def checkBlock():
    cursor = connection.cursor()

    cursor.execute(
        '''SELECT COUNT(v.id) as count, a.ValueKey as ValueKey
            FROM verifys v,
            attempts a WHERE v.AttemptKey = a.id
            GROUP BY v.id
            ORDER BY COUNT(v.id)''')

    count = [[]]
    for row in cursor.fetchall():
        count[row['exp_m']][row['exp_n']] = row['count']

    return count


def getUnfinishedBlock():
    cursor = connection.cursor()

    cursor.execute(
        '''SELECT AttemptKey FROM verifys
            WHERE AttemptKey IN (SELECT AttemptKey FROM
            (SELECT COUNT(id) as count, AttemptKey FROM verifys
                WHERE AttemptKey IN (SELECT v.AttemptKey FROM verifys v
                JOIN attempts a ON a.id = v.AttemptKey)
            GROUP BY AttemptKey) AS t)''')

    AttemptKey = cursor.fetchone()

    if AttemptKey == 0:
        AttemptKey = None

    return AttemptKey


def findMax():
    cursor = connection.cursor()

    cursor.execute(
        'SELECT MAX(exp_m) as exp_m, MAX(exp_n) as exp_n FROM exp_values')
    row = cursor.fetchone()

    if row[0] == None and row[1] == None:
        return 3

    return max(row[0], row[1])


def Populate(request):
    cursor = connection.cursor()
    count_by = 10

    cursor.execute(
        'SELECT MAX(exp_m) as exp_m, MAX(exp_n) as exp_n FROM exp_values')
    row = cursor.fetchone()

    if row[0] == None and row[1] == None:
        y = 3
        x = 3
    else:
        y = row[0]
        x = row[1]

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

    # render(request, "BealsTreasure/completed.html")

    return HttpResponse(blocks)
