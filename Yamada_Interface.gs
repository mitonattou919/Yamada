// Global
var ResponseWord = "なんやねん";
var CommandAim = "/yamada";


//generate json payload
var Payload = function (Channel, Username) {
  this.Channel = Channel;
  this.Username = Username;
};

Payload.prototype = {

  // Button format.
  createButton : function() {

    const SlackPayload = {
      "response_type": "in_channel",
      "channel"      : this.Channel,
      "blocks": [
        {
          "type": "section",
          "text": {
            "type": "mrkdwn",
            "text": "<@" + this.Username + "> " + ResponseWord
          }
        },
        {
          "type": "actions",
          "block_id":"section1234",
          "elements": [
            {
              "type": "button",
              "text": {
                "type": "plain_text",
                "emoji": true,
                "text": ":sun_with_face: In"
              },
              "value": "pin"
            },
            {
              "type": "button",
              "text": {
                "type": "plain_text",
                "emoji": true,
                "text": ":new_moon_with_face: Out"
              },
              "value": "pout"
            },
            {
              "type": "button",
              "text": {
                "type": "plain_text",
                "emoji": true,
                "text": ":full_moon_with_face: Dayoff"
              },
              "value": "poff"
            },
            {
              "type": "button",
              "text": {
                "type": "plain_text",
                "emoji": true,
                "text": ":clipboard: Report"
              },
              "value": "prep"
            }
          ]
        }

      ]
    };
    
    return SlackPayload;

  }

}



function doPost(e) {

  const VerToken = PropertiesService.getScriptProperties().getProperty('VERIF_TOKEN');
  if (e.parameter.token != VerToken) { return; };

  var MyPayload = new Payload(e.parameter.channel_id, e.parameter.user_name); 
  return ContentService.createTextOutput(JSON.stringify(MyPayload.createButton())).setMimeType(ContentService.MimeType.JSON);

}
