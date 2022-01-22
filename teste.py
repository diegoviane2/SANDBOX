import argparse
parser = argparse.ArgumentParser(description = "Which Message?")
parser.add_argument("namespace", type=int)
parser.add_argument("pod", type=int)
parser.add_argument("timestamp", type=int)
args = parser.parse_args()

calc = args.namespace + args.pod * args.timestamp
print(f'{calc}' + " teste")