#!/bin/bash
set -efu -o pipefail

SCALE="$1"
GRAPH="fixed-s${SCALE}.net"

VXCNT="$(bc <<< "2^${SCALE}")"
while : ; do
	EDGES="$(bc <<< "16 * ${VXCNT}")"
	./kron_generator "$EDGES" "$SCALE" 0 0 > "$GRAPH"
	VXCNT="$(./graph_utils.py "$GRAPH" | grep 'VERTEX_COUNT' | egrep -o '[[:digit:]]+')"

	NOFIT="$(bc -l <<< "(${EDGES}/${VXCNT} - 16.0) > 0.1")"
	[ "$NOFIT" -eq 1 ] || break
done

echo "$EDGES"
