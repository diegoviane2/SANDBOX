#!/bin/bash

# kubernetes-scale_pods.sh load-test sts jmeter-master 1

namespace=$1
kind=$2
resource=$3
replicas=$4

#echo "[ TASK: SCALE PODS ]"
echo "  [ Initializing task - Scale pods ]"
# Get pods status
last_active=`kubectl -n $namespace get $kind $resource --no-headers | awk '{print $2}' | cut -d "/" -f 1 | tr -d '\n'`

echo "  [ Scaling $resource pods from $last_active to $replicas ... ]"

result=`kubectl -n $namespace scale $kind $resource --replicas=$replicas`

echo "  [ $result ... `kubectl -n $namespace get $kind $resource --no-headers | awk '{print $2}' | cut -d "/" -f 1 | tr -d '\n'` pod(s) running ... ] [ OK ]"

echo "  [ Scale pods ... ] [DONE]"
#echo "[ TASK: SCALE PODS ] [ COMPLETED! ]"