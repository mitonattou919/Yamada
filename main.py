
# coding: utf-8

# import modules
import os
import json
import random
import datetime
from flask import Flask, request
from dateutil.relativedelta import relativedelta

# import private modules
import myfirestore
import myslackbot
import myslackpayload


# read configuration file
with open('config.json', 'r') as f:
    data = f.read()
config = json.loads(data)

token  = config.get('BOT_TOKEN')            # Bot User OAuth Access Token
secret = config.get('SIGNING_SECRET')       # Signing Secret


# read greet settings file
with open('greet.json', 'r') as f:
    data = f.read()
greet = json.loads(data)

#         1         2         3         4         5         6         7
#1234567890123456789012345678901234567890123456789012345678901234567890123456789


app = Flask(__name__)

my_slackbot = myslackbot.MySlackBot(token, secret)
my_fs  = myfirestore.MyFireStore('users')


# [START event_api]
@app.route('/event_api', methods=['POST'])
def do_post_req():

    # Get content-type header option from request.
    try:
        content_type = request.headers['Content-type']
    except KeyError as e:
        print(e)
        return 'Invalid request'

    # Get request body for authentication..
    body = request.get_data(as_text=True)

    # Get headers from request.
    try:
        x_slack_signature = request.headers['X-Slack-Signature']
        x_slack_request_ts = request.headers['X-Slack-Request-Timestamp']
    except KeyError as e:
        print(e)
        return 'Invalid request'

    # Verify request by Signing Secret and X-Slack-Signature.
    try:
        my_slackbot.verify_auth(body, x_slack_signature, x_slack_request_ts)
    except ValueError as e:
        print(e)
        return 'Authorization failed.', 200

    # Get current date and time with jst timezone.
    dt_now = datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=9))
    )

    # Event API
    if content_type == 'application/json':

        body_json = request.get_json(silent=True)

        # for Slack URL verification.
        try:
            if body_json['type'] == 'url_verification':
                return body_json['challenge'], 200
        except KeyError as e:
            print(e)
            return 'Invalid request'

        # Get slack event from request.
        try:
            channel_id = body_json['event']['channel']
            event_text = body_json['event']['text']
            team_id    = body_json['team_id']
            user_id    = body_json['event']['user']
        except KeyError as e:
            print(e)
            return 'Invalid request'

        # omit bot id from event text.
        user_text = event_text[14:].lstrip()

        # Get slack rich payload.
        my_slack_payload = myslackpayload.MySlackPayload(channel_id, user_id)

        # When user said good morning.
        if user_text in greet.get('list_gm'):
            reply_text = random.choice(greet.get('reply_gm'))
            my_fs.set_time('start', user_id, dt_now)
            my_slackbot.send_simplemsg(channel_id, f'{reply_text}')

        # When user said good bye.
        elif user_text in greet.get('list_gb'):
            reply_text = random.choice(greet.get('reply_gb'))
            my_fs.set_time('end', user_id, dt_now)
            my_slackbot.send_simplemsg(channel_id, f'{reply_text}')

        # When user said report.
        elif user_text in greet.get('list_rp'):
            reply_text = random.choice(greet.get('reply_ot'))
            reports = my_fs.get_time(user_id, dt_now)
            reply_payload = my_slack_payload.get_report(
                reply_text, reports[0], reports[1], reports[2], reports[3])
            my_slackbot.send_payload(reply_payload)

        # When user said thank you.
        elif user_text in greet.get('list_ty'):
            reply_text = random.choice(greet.get('reply_ty'))
            my_slackbot.send_simplemsg(channel_id, f'{reply_text}')

        else:
            reply_text = random.choice(greet.get('reply_ot'))
            my_fs.set_teamid(user_id, team_id)
            reply_payload = my_slack_payload.get_menu(reply_text)
            print(reply_payload)
            my_slackbot.send_payload(reply_payload)

    # Interactive Message
    elif content_type == 'application/x-www-form-urlencoded':

        request_payload = request.form.get('payload')
        body_json = json.loads(request_payload)

        # Get slack event from request.
        try:
            action_id  = body_json['actions'][0]['action_id']
            channel_id = body_json['channel']['id']
            team_id    = body_json['team']['id']
            user_id    = body_json['user']['id']
            user_name  = body_json['user']['name']
            message_ts = body_json['message']['ts']
        except KeyError as e:
            print(e)
            return 'Invalid request'

        my_slack_payload = myslackpayload.MySlackPayload(channel_id, user_id)

        # User canceld.
        if action_id == 'yamada9901':
            my_slackbot.delete_message(channel_id, message_ts)

            reply_text = 'やらないんかーい'
            my_slackbot.send_simplemsg(channel_id, f'{reply_text}')

        elif action_id == 'yamada0101':
            user_rep  = body_json['actions'][0]['selected_user']
            my_fs.set_common(user_id, u'report_user', user_rep)

        # User selected target report month.
        elif action_id =='yamada0102':
            report_diff  = body_json['actions'][0]['selected_option']['value']
            dt_rep = dt_now - relativedelta(months=(int(report_diff)))
            my_fs.set_common(user_id, u'report_month', dt_rep)

        elif action_id =='yamada0103':
            my_slackbot.delete_message(channel_id, message_ts)
            reply_text = random.choice(greet.get('reply_ot'))
            modify_dict =my_fs.get_various(user_id)

            if 'report_month' in modify_dict.keys():
                dt_rep = modify_dict['report_month']
            else:
                dt_rep = dt_now

            if 'report_user' in modify_dict.keys():
                user_id_rep = modify_dict['report_user']
            else:
                user_id_rep = user_id

            reports = my_fs.get_time(user_id_rep, dt_rep)
            reply_payload = my_slack_payload.get_report(
                                reply_text, reports[0], reports[1], reports[2], reports[3])
            my_slackbot.send_payload(reply_payload)
            my_fs.init_various(user_id)
    
        elif action_id == 'yamada0201':
            user_rep  = body_json['actions'][0]['selected_user']
            my_fs.set_common(user_id, u'modify_user', user_rep)

        elif action_id =='yamada0202':
            mod_type  = body_json['actions'][0]['selected_option']['value']
            my_fs.set_common(user_id, u'modify_type', mod_type)

        elif action_id =='yamada0203':
            target_date  = body_json['actions'][0]['selected_date']
            my_fs.set_common(user_id, u'modify_date', target_date)

        elif action_id =='yamada0204':
            target_hour  = body_json['actions'][0]['selected_option']['value']
            my_fs.set_common(user_id, u'modify_hour', target_hour)

        elif action_id =='yamada0205':
            target_min  = body_json['actions'][0]['selected_option']['value']
            my_fs.set_common(user_id, u'modify_min', target_min)

        elif action_id == 'yamada0206':
            my_slackbot.delete_message(channel_id, message_ts)
            reply_text = random.choice(greet.get('reply_do'))
            modify_dict =my_fs.get_various(user_id)

            if 'modify_type' in modify_dict.keys():
                mod_type = modify_dict['modify_type']
            else:
                mod_type = 'start'

            if 'modify_user' in modify_dict.keys():
                mod_user = modify_dict['modify_user']
            else:
                mod_user = user_id

            if 'modify_date' in modify_dict.keys():
                mod_date = modify_dict['modify_date']
            else:
                mod_date = dt_now.strftime('%Y-%m-%d')

            if 'modify_hour' in modify_dict.keys():
                mod_hour = modify_dict['modify_hour']
            else:
                mod_hour = '09'

            if 'modify_min' in modify_dict.keys():
                mod_min = modify_dict['modify_min']
            else:
                mod_min = '00'

            tstr = mod_date + ' ' + mod_hour + ':' + mod_min + ':00 +0900'
            target_dt = datetime.datetime.strptime(tstr, '%Y-%m-%d %H:%M:%S %z')

            my_fs.set_time(mod_type, mod_user, target_dt)
            my_fs.set_teamid(mod_user, team_id)
            my_slackbot.send_simplemsg(channel_id, f'{reply_text}')
            my_fs.init_various(user_id)

            my_fs.set_common(user_id, u'user_name', user_name)


    return 'OK', 200


@app.route('/health_check', methods=['GET'])
def do_get():
    
    user_id = 'health_check'

    # Get current date and time with jst timezone.
    dt_now = datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=9))
    )

    my_fs.set_time('start', user_id, dt_now)

    return 'OK', 200


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))

