<html>
    <head>
	<title>Question Engine</title>
    </head>
    <body>
    {{message}}<br/>
	<form method="POST" action="/quiz/{{question_id}}">
        <input type="hidden" name="name" value="{{name}}" /><br />
        <input type="hidden" name="choice" value="{{choice}}" /><br />
        <strong>{{question}}</strong><br/>
        <input type="text" name="answer" value="" /><br />
        <input type="submit" value="submit" />
	</form>
    </body>
</html>
