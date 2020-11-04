#         1         2         3         4         5         6         7
#1234567890123456789012345678901234567890123456789012345678901234567890123456789

# coding: utf-8

import datetime
import dts


class MySlackPayload:

    def __init__(self, channel, user_id):
        self.channel = channel
        self.user_id  = user_id

    def get_menu_x(self, reply_text):

        dt_now = datetime.datetime.now()
        fmt_dt = dt_now.strftime('%Y-%m-%d')
        print(fmt_dt)

        payload = {
            "channel": self.channel,
            "text": "ok",
            "blocks": [
        		{
		            "type": "datepicker",
        			"action_id": "yamada0202",
        			"initial_date": fmt_dt,
        				"placeholder": {
		        			"type": "plain_text",
        					"text": "Select a date"
                        }
                }
                
            ]
        }
        
        return payload


    def get_menu(self, reply_text):

        dt_now = datetime.datetime.now()
        fmt_dt = dt_now.strftime('%Y-%m-%d')
        
        payload = {
            "channel": self.channel,
            "user": self.user_id,
        	"blocks": [
            	{
			        "type": "section",
			        "text": {
				        "type": "plain_text",
				        "text": reply_text
			        }
		        },
        		{
        			"type": "header",
        			"text": {
        				"type": "plain_text",
        				"text": ":calendar: 勤務表"
        			}
        		},
        		{
		        	"type": "actions",
			        "elements": [
				        {
        					"type": "users_select",
		        			"action_id": "yamada0101",
				        	"placeholder": {
        						"type": "plain_text",
		        				"text": "誰の？"
        					},
                            "initial_user": self.user_id
		        		},
				        {
        					"type": "static_select",
		        			"action_id": "yamada0102",
				        	"placeholder": {
        						"type": "plain_text",
		        				"text": "いつの？"
        					},
                            "initial_option":
                                {"text": {"type": "plain_text","text": "今月"},"value": "0"},
		        			"options": [
        						{"text": {"type": "plain_text","text": "今月"},"value": "0"},
		        				{"text": {"type": "plain_text","text": "先月"},"value": "1"},
				        		{"text": {"type": "plain_text","text": "2ヶ月前"},"value": "2"},
        						{"text": {"type": "plain_text","text": "3ヶ月前"},"value": "3"},
		        				{"text": {"type": "plain_text","text": "4ヶ月前"},"value": "4"},
        						{"text": {"type": "plain_text","text": "5ヶ月前"},"value": "5"},
        						{"text": {"type": "plain_text","text": "6ヶ月前"},"value": "6"},
		        				{"text": {"type": "plain_text","text": "7ヶ月前"},"value": "7"},
				        		{"text": {"type": "plain_text","text": "8ヶ月前"},"value": "8"},
        						{"text": {"type": "plain_text","text": "9ヶ月前"},"value": "9"},
		        				{"text": {"type": "plain_text","text": "10ヶ月前"},"value": "10"},
				        		{"text": {"type": "plain_text","text": "11ヶ月前"},"value": "11"},
        						{"text": {"type": "plain_text","text": "12ヶ月前"},"value": "12"}
        					]
		        		}
        			]
        		},
		        {
        			"type": "actions",
		        	"elements": [
        				{
		        			"type": "button",
				        	"action_id": "yamada0103",
        					"text": {
		        				"type": "plain_text",
				        		"text": "表示"
        					},
                            "style": "primary",
        					"value": "click_me_123"
		        		}
        			]
        		},
        		{
        			"type": "divider"
        		},
        		{
		        	"type": "header",
        			"text": {
        				"type": "plain_text",
        				"text": ":alarm_clock: 出退勤時刻の修正"
        			}
        		},
        		{
        			"type": "actions",
        			"elements": [
				        {
        					"type": "users_select",
		        			"action_id": "yamada0201",
				        	"placeholder": {
        						"type": "plain_text",
		        				"text": "誰の？"
        					},
                            "initial_user": self.user_id
		        		},
		        		{
        					"type": "static_select",
        					"action_id": "yamada0202",
        					"placeholder": {
		        				"type": "plain_text",
        						"text": "どっち？"
		        			},
                            "initial_option":
                                {"text": {"type": "plain_text","text": "出勤"},"value": "start"},
        					"options": [
        						{"text": {"type": "plain_text","text": "出勤"},"value": "start"},
		        				{"text": {"type": "plain_text","text": "退勤"},"value": "end"}
        					]
        				},
        				{
		        			"type": "datepicker",
        					"action_id": "yamada0203",
		        			"initial_date": fmt_dt,
        					"placeholder": {
		        				"type": "plain_text",
        						"text": "Select a date"
        					}
        				},
		        		{
        					"type": "static_select",
		        			"action_id": "yamada0204",
				        	"placeholder": {
				        		"type": "plain_text",
				        		"text": "時"
					        },
                            "initial_option":
                                {"text": {"type": "plain_text","text": "9時"},"value": "09"},
        					"options": [
		        				{"text": {"type": "plain_text","text": "0時"},"value": "00"},
        						{"text": {"type": "plain_text","text": "1時"},"value": "01"},
        						{"text": {"type": "plain_text","text": "2時"},"value": "02"},
		        				{"text": {"type": "plain_text","text": "3時"},"value": "03"},
        						{"text": {"type": "plain_text","text": "4時"},"value": "04"},
        						{"text": {"type": "plain_text","text": "5時"},"value": "05"},
        						{"text": {"type": "plain_text","text": "6時"},"value": "06"},
		        				{"text": {"type": "plain_text","text": "7時"},"value": "07"},
				        		{"text": {"type": "plain_text","text": "8時"},"value": "08"},
        						{"text": {"type": "plain_text","text": "9時"},"value": "09"},
		        				{"text": {"type": "plain_text","text": "10時"},"value": "10"},
				        		{"text": {"type": "plain_text","text": "11時"},"value": "11"},
						        {"text": {"type": "plain_text","text": "12時"},"value": "12"},
        						{"text": {"type": "plain_text","text": "13時"},"value": "13"},
		        				{"text": {"type": "plain_text","text": "14時"},"value": "14"},
				        		{"text": {"type": "plain_text","text": "15時"},"value": "15"},
        						{"text": {"type": "plain_text","text": "16時"},"value": "16"},
		        				{"text": {"type": "plain_text","text": "17時"},"value": "17"},
				        		{"text": {"type": "plain_text","text": "18時"},"value": "18"},
        						{"text": {"type": "plain_text","text": "19時"},"value": "19"},
		        				{"text": {"type": "plain_text","text": "20時"},"value": "20"},
				        		{"text": {"type": "plain_text","text": "21時"},"value": "21"},
        						{"text": {"type": "plain_text","text": "22時"},"value": "22"},
				        		{"text": {"type": "plain_text","text": "23時"},"value": "23"}
        					]
		        		},
        				{
		        			"type": "static_select",
        					"action_id": "yamada0205",
		        			"placeholder": {
        						"type": "plain_text",
        						"text": "分"
				        	},
                            "initial_option":
                                {"text": {"type": "plain_text","text": "00分"},"value": "00"},
        					"options": [
		        				{"text": {"type": "plain_text","text": "00分"},"value": "00"},
        						{"text": {"type": "plain_text","text": "01分"},"value": "01"},
		        				{"text": {"type": "plain_text","text": "02分"},"value": "02"},
        						{"text": {"type": "plain_text","text": "03分"},"value": "03"},
        						{"text": {"type": "plain_text","text": "04分"},"value": "04"},
		        				{"text": {"type": "plain_text","text": "05分"},"value": "05"},
        						{"text": {"type": "plain_text","text": "06分"},"value": "06"},
        						{"text": {"type": "plain_text","text": "07分"},"value": "07"},
		        				{"text": {"type": "plain_text","text": "08分"},"value": "08"},
        						{"text": {"type": "plain_text","text": "09分"},"value": "09"},
        						{"text": {"type": "plain_text","text": "10分"},"value": "10"},
		        				{"text": {"type": "plain_text","text": "11分"},"value": "11"},
        						{"text": {"type": "plain_text","text": "12分"},"value": "12"},
        						{"text": {"type": "plain_text","text": "13分"},"value": "13"},
		        				{"text": {"type": "plain_text","text": "14分"},"value": "14"},
        						{"text": {"type": "plain_text","text": "15分"},"value": "15"},
        						{"text": {"type": "plain_text","text": "16分"},"value": "16"},
        						{"text": {"type": "plain_text","text": "17分"},"value": "17"},
		        				{"text": {"type": "plain_text","text": "18分"},"value": "18"},
        						{"text": {"type": "plain_text","text": "19分"},"value": "19"},
		        				{"text": {"type": "plain_text","text": "20分"},"value": "20"},
        						{"text": {"type": "plain_text","text": "21分"},"value": "21"},
		        				{"text": {"type": "plain_text","text": "22分"},"value": "22"},
				        		{"text": {"type": "plain_text","text": "23分"},"value": "23"},
        						{"text": {"type": "plain_text","text": "24分"},"value": "24"},
		        				{"text": {"type": "plain_text","text": "25分"},"value": "25"},
				        		{"text": {"type": "plain_text","text": "26分"},"value": "26"},
						        {"text": {"type": "plain_text","text": "27分"},"value": "27"},
        						{"text": {"type": "plain_text","text": "28分"},"value": "28"},
		        				{"text": {"type": "plain_text","text": "29分"},"value": "29"},
				        		{"text": {"type": "plain_text","text": "30分"},"value": "30"},
						        {"text": {"type": "plain_text","text": "31分"},"value": "31"},
        						{"text": {"type": "plain_text","text": "32分"},"value": "32"},
		        				{"text": {"type": "plain_text","text": "33分"},"value": "33"},
				        		{"text": {"type": "plain_text","text": "34分"},"value": "34"},
						        {"text": {"type": "plain_text","text": "35分"},"value": "35"},
        						{"text": {"type": "plain_text","text": "36分"},"value": "36"},
		        				{"text": {"type": "plain_text","text": "37分"},"value": "37"},
				        		{"text": {"type": "plain_text","text": "38分"},"value": "38"},
						        {"text": {"type": "plain_text","text": "39分"},"value": "39"},
        						{"text": {"type": "plain_text","text": "40分"},"value": "40"},
		        				{"text": {"type": "plain_text","text": "41分"},"value": "41"},
				        		{"text": {"type": "plain_text","text": "42分"},"value": "42"},
						        {"text": {"type": "plain_text","text": "43分"},"value": "43"},
        						{"text": {"type": "plain_text","text": "44分"},"value": "44"},
		        				{"text": {"type": "plain_text","text": "45分"},"value": "45"},
				        		{"text": {"type": "plain_text","text": "46分"},"value": "46"},
						        {"text": {"type": "plain_text","text": "47分"},"value": "47"},
        						{"text": {"type": "plain_text","text": "48分"},"value": "48"},
		        				{"text": {"type": "plain_text","text": "49分"},"value": "49"},
				        		{"text": {"type": "plain_text","text": "50分"},"value": "50"},
						        {"text": {"type": "plain_text","text": "51分"},"value": "51"},
        						{"text": {"type": "plain_text","text": "52分"},"value": "52"},
		        				{"text": {"type": "plain_text","text": "53分"},"value": "53"},
				        		{"text": {"type": "plain_text","text": "54分"},"value": "54"},
						        {"text": {"type": "plain_text","text": "55分"},"value": "55"},
        						{"text": {"type": "plain_text","text": "56分"},"value": "56"},
		        				{"text": {"type": "plain_text","text": "57分"},"value": "57"},
				        		{"text": {"type": "plain_text","text": "58分"},"value": "58"},
        						{"text": {"type": "plain_text","text": "59分"},"value": "59"}
		        			]
        				}
		        	]
        		},
		        {
        			"type": "actions",
		        	"elements": [
        				{
		        			"type": "button",
				        	"action_id": "yamada0206",
        					"text": {
		        				"type": "plain_text",
				        		"text": "修正"
        					},
                            "style": "primary",
        					"value": "click_me_123"
		        		}
        			]
        		},
		        {
        			"type": "divider"
        		},
		        {
        			"type": "actions",
		        	"elements": [
        				{
		        			"type": "button",
				        	"action_id": "yamada9901",
        					"text": {
		        				"type": "plain_text",
				        		"text": "やっぱやめる"
        					},
                            "style": "danger",
        					"value": "click_me_123"
		        		}
        			]
        		}
	        ]
        }
    
        return payload


    def get_report(self, reply_text, target_month, report_text, total_secs, working_days):

        if not report_text:
            report_text = 'なし'
        
        payload = {
            "channel": self.channel,
            "user": self.user_id,
            "text": "<@" + self.user_id + ">",
        	"blocks": [
            	{
			        "type": "section",
			        "text": {
				        "type": "mrkdwn",
				        "text": reply_text
			        }
		        },
        		{
        			"type": "section",
        			"text": {
        				"type": "mrkdwn",
        				"text": ":calendar: *勤務表* " + target_month
        			}
        		},
        		{
        			"type": "divider"
        		},
            	{
			        "type": "section",
			        "text": {
				        "type": "plain_text",
				        "text": report_text
			        }
		        },
        		{
        			"type": "divider"
        		},
        		{
		        	"type": "section",
        			"fields": [
                        {
                            "type": "mrkdwn",
                            "text": "*日数:* " + format(working_days, '2d') + "日"
                        },
                        {
                            "type": "mrkdwn",
                            "text": "*合計:* " + format((total_secs/60/60), '4.2f') + "時間"
                        },
                        {
                            "type": "mrkdwn",
                            "text": "*平均:* " + format(((total_secs/working_days)/60/60), '4.2f') + "時間"
                        }
                    ]
        		}
	        ]
        }
    
        return payload

