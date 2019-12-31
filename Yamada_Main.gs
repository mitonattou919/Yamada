function doPost(e) {

  const VerToken = PropertiesService.getScriptProperties().getProperty('VERIF_TOKEN');

  const eParameter=e.parameter;
  const eData = eParameter.payload;
  const eJson = JSON.parse(decodeURIComponent(eData));

  if (eJson.token != VerToken) { return; };

  var doc = DocumentApp.create('JSON_Of_Debug'); 
  var body = doc.getBody();
  body.appendParagraph(eJson.actions[0].action_id);
  body.appendParagraph(eJson.actions[0].block_id);
  body.appendParagraph(eJson.actions[0].value);
  body.appendParagraph(eJson.token);
  body.appendParagraph(eJson.api_app_id);
  body.appendParagraph(eJson.user.name);
  body.appendParagraph(eJson.user.username);
  body.appendParagraph(eJson.channel.name);
  body.appendParagraph(eJson.team.id);
  body.appendParagraph(eJson.team.domain);
  


}

