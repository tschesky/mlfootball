import json
import urllib
import operator
import datetime

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from social_django.models import UserSocialAuth

from application_content.forms import RegistrationForm
from application_content.models import *

def index(request):
    """
    index.html is returned in response with no context currently
    :param request: HttpRequest object
    :return: http response with context rendered on template
    """
    template = loader.get_template('home_page/index.html')
    today = datetime.date.today()
    start_date = today.strftime("%Y-%m-%d")
    end_date = (today + datetime.timedelta(days=31)).strftime("%Y-%m-%d")

    query_result = Matches.objects.filter(date__range=[start_date, end_date])
    ordered = sorted(query_result, key=operator.attrgetter('date'))

    modes = {}
    for record in ordered:
        res_list = [record.cart_res, record.nb_res, record.svm_res]
        modes[int(record.match_id)] = max(set(res_list), key=res_list.count)

    print modes

    context = {
        "matches" : ordered[:30],
        "modes" : modes
    }
    return HttpResponse(template.render(context, request))

@login_required
def results(request):
    """
    index.html is returned in response with no context currently
    :param request: HttpRequest object
    :return: http response with context rendered on template
    """
    template = loader.get_template('results/results.html')
    today = datetime.date.today()
    query_result = Matches.objects.exclude(result=None)
    ordered = sorted(query_result, key=operator.attrgetter('date'))

    ok = {}
    modes = {}
    for record in ordered:
        res_list = [record.cart_res, record.nb_res, record.svm_res]
        mode = max(set(res_list), key=res_list.count)
        modes[int(record.match_id)] = mode
        if mode == record.result:
            ok[int(record.match_id)] = 1
        else:
            ok[int(record.match_id)] = 0

    print ok

    context = {
        "matches" : ordered[:30],
        "ok" : ok,
        "modes": modes
    }
    return HttpResponse(template.render(context, request))

@login_required
def profile(request):
    """
    profile.html is returned in response with no context currently
    :param request: HttpRequest object
    :return: http response with context rendered on template
    """

    user = request.user

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    social_user = request.user.social_auth.filter(
        provider='facebook',
    ).first()
    if social_user:
        url = u'https://graph.facebook.com/v2.9/' \
              u'me?fields=id,name,website,birthday,locale' \
              u'&access_token={0}'.format(
            social_user.extra_data['access_token']
        )
        data = json.loads(urllib.urlopen(url).read())
        context = {
            'data': data,
            'facebook_login': facebook_login,
            'github_login': github_login,
            'can_disconnect': can_disconnect
        }
    else:
        context = {

        }
    template = loader.get_template('user_profile/profile.html')

    return HttpResponse(template.render(context, request))


def login(request):
    """
    login.html is returned in response with no context currently
    :param request: HttpRequest object
    :return: http response with context rendered on template
    """
    template = loader.get_template('registration/login.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def logout_page(request):
    """
    login.html is returned in response with no context currently
    :param request: HttpRequest object
    :return: http response with context rendered on template
    """
    logout(request)
    return HttpResponseRedirect("/login")


def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            user.save()
            # if form.cleaned_data['log_on']:
            #     user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            #     # login(request, user)
            #     template = loader.get_template("home_page/index.html")
            #     context = {'user': user}
            #     return HttpResponseRedirect(template.render(context, request))
            # else:
            template = loader.get_template("registration/register_success.html")
            context = {'username': form.cleaned_data['username']}
            return HttpResponse(template.render(context, request))
    else:
        form = RegistrationForm()
    template = loader.get_template("registration/register.html")
    context = {'form': form}
    return HttpResponse(template.render(context, request))


@login_required
def settings(request):
    """
    trial of  authentication to:
     * facebook
     * github
     login is required to proceed
    :param request: HttpRequest object
    :return: http response with context rendered on template
    """
    user = request.user

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'registration/settings.html', {
        'facebook_login': facebook_login,
        'github_login': github_login,
        'twitter_login': twitter_login,
        'can_disconnect': can_disconnect
    })


@login_required
def password(request):
    """
    Validation of form and changing password
    login is required to proceed
    :param request: HttpRequest object
    :return: http response with context rendered on template,
            form with registration data
    """
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('settings')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'registration/password.html', {'form': form})



def news(request):
    """
    news.html is returned in response with no context currently
    :param request: HttpRequest object
    :return: http response with context rendered on template
    """
    template = loader.get_template('news/news.html')
    context = {'tweets': get_tweets()

               }
    return HttpResponse(template.render(context, request))


def get_tweets():
    """
    internal function - not called from a URL
    function initially prepared to parse tweets content,
    it was replaced by tweeter widget displaying twitter timeline
    may be used for future processing
    :return: table with text of tweets from specified site
    """

    tweets = []
    try:
        import twitter
        api = twitter.Api(consumer_key='vJGrMWYuGe9d9Wohxj6nFh0mv',
                          consumer_secret='qzyER5Y0kuKmmnEJmuWy5PT5DHpoeJDsMWHpAxSFrlH0LbTt8t',
                          access_token_key='866322307740028933-GogzPQhoHMrCDhSKnoev5GorTFmqi1h',
                          access_token_secret='kSPEhATZzYYImWh2ZwwMOR3J0dtadxF4cSVDiVJ06Ty94')

        latest = api.GetUserTimeline(screen_name='mlfootball_test', exclude_replies=True, include_rts=False)
        for tweet in latest:
            status = tweet.text
            tweet_date = tweet.created_at
            tweets.append({'status': status, 'date': tweet_date})
    except:
        tweets.append({'status': 'Follow football events', 'date': 'just now2'})
    return tweets
