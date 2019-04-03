import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('echo', help='Display this string')
argparser.add_argument('--caps', help='when turned on, program displays string in caps', action='store_true')
args = argparser.parse_args()
if args.caps:
	print(args.echo.upper())
else:
	print(args.echo)

