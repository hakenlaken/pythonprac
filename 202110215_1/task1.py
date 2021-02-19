from bottle import route, error, post, get, run, static_file, abort, redirect, response, request, template
import pyfiglet 

@route('/')
@get('/')
def upload_view():
    return template("""
    	<h1>Made by hakenlaken</h1>
        <form action="/" method="post">
          <label for="string">String:</label>
          <input type="text" id="string" name="string"">
          <label for="font">Font in Pyfiglet:</label>
          <select id="font" name="font">
          	<option disabled>Select font</option>
          	% for c in fonts:
				<option value={{c}}>{{c}}</option>
			% end
   		  </select>
          <input type="submit" name="submit" value="Upload" />
        </form>
        <a href="https://github.com/hakenlaken/pythonprac/">Visit the origin!</a>
        <p>© All rights reserved!</p>
        """, fonts = pyfiglet.FigletFont.getFonts())


@post('/')
def do_upload():
    string = request.forms.get('string')
    font = request.forms.get('font')
    print(string,font)
    if string is not None and font is not None:
    	result = pyfiglet.figlet_format(string, font = font )
    	return template("""
    		<p></p>
    		<pre>{{result}}</pre>
    		<p></p>
    	""", result=result)
    return "You missed a field."

run(host='localhost', port=8080, reloader=True)
