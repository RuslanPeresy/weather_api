import aiohttp
import json
from requests import Request, Session

async def index(request):
	url = request.app['config'].get('url')
	params = request.app['config'].get('params')

	#could specify some optional parameters for the request
	timeout = 1
	
	with Session() as s:
		req = Request('POST', url, params=params)

		prepped = s.prepare_request(req)

		#could do something with prepped.body/prepped.headers here
		#...

		r = s.send(prepped,
			timeout=timeout)
	
	return aiohttp.web.json_response(json.loads(r.content))
