#!/bin/bash

namespace=$1
deployment=$2


last=$(kubectl -n $namespace get deployments | grep $deployment | awk '{print $2}' | cut -d '/' -f 1)


#kubectl -n sandbox get pod  --output-watch-events --watch | awk '/nginx/ && /Running/'


 -o, --output='': 
 Output format. 
 One of: 
 json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|jsonpath-as-json|jsonpath-file|custom-columns-file|custom-columns|wide See custom columns [https://kubernetes.io/docs/reference/kubectl/overview/#custom-columns] , 
 golang template [http://golang.org/pkg/text/template/#pkg-overview] and 
 jsonpath template [https://kubernetes.io/docs/reference/kubectl/jsonpath/].