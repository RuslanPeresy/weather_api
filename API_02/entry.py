import argparse
import asyncio
import aiohttp
from weather import create_app
from weather.settings import load_config
#something important
#something more impourtant

try:
	import uvloop
	asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
	print('Library uvloop is not available')

parser = argparse.ArgumentParser(description="Weather API")

parser.add_argument(
	'--reload', 
	action='store_true', 
	help='Autoreload code on change')

parser.add_argument('-c', '--config', type=argparse.FileType('r'),
	help='Path to configuration file')

args = parser.parse_args()

app = create_app(config=load_config(args.config))

if args.reload:
	print('Start with code reload')
	import aioreloader
	aioreloader.start()

if __name__ == '__main__':
	aiohttp.web.run_app(app)
