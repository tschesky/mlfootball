from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User



from social_django.models import UserSocialAuth

from application_content.forms import RegistrationForm


def index(request):
    template = loader.get_template('home_page/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


@login_required
def profile(request):
    template = loader.get_template('user_profile/profile.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template('registration/login.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def logout_page(request):
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

    return render(request, 'registration/settings.html', {
        'facebook_login': facebook_login,
        'github_login': github_login,
        'can_disconnect': can_disconnect
    })


@login_required
def password(request):
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
    template = loader.get_template('news/news.html')
    context = {'tweets': get_tweets()

    }
    return HttpResponse(template.render(context, request))


def get_tweets():
    """internal function - not called from a URL"""
    tweets = []
    try:
        import twitter
        api = twitter.Api(consumer_key='vJGrMWYuGe9d9Wohxj6nFh0mv',
                          consumer_secret='qzyER5Y0kuKmmnEJmuWy5PT5DHpoeJDsMWHpAxSFrlH0LbTt8t',
                          access_token_key='866322307740028933-GogzPQhoHMrCDhSKnoev5GorTFmqi1h',
                          access_token_secret='kSPEhATZzYYImWh2ZwwMOR3J0dtadxF4cSVDiVJ06Ty94')

        latest =  api.GetUserTimeline(screen_name='mlfootball_test', exclude_replies=True, include_rts=False)
        for tweet in latest:
            status = tweet.text
            tweet_date = tweet.created_at
            tweets.append({'status': status, 'date': tweet_date})
    except:
        tweets.append({'status': 'Follow football events', 'date': 'just now2'})
    return tweets
