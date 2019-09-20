from aiohttp import web
import json
import pathlib

async def handle(request):
	response_obj = {
		'about': 'Weather JSON API',
		'usage': 'Specify a post request'
	}

	return web.Response(text=json.dumps(response_obj), status=200)

app = web.Application()
conf = load_config(str(pathlib.Path('.') / 'config.yaml'))
app['config'] = conf

app.router.add_get('/', handle)

web.run_app(app)