pod=5
declare -a res=()

#echo "jmeter-test-1-0   1/1     CrashLoopBackOff   4          2m38sbad-frontend-4s58z   0/1     CrashLoopBackOff   4          2m38s" | awk '{print $2}' | cut -d "/" -f 1
#echo "jmeter-test-1-0   1/1     CrashLoopBackOff   4          2m38sbad-frontend-4s58z   0/1     CrashLoopBackOff   4          2m38s" | awk '{print $2}' | cut -d "/" -f 1
#echo "jmeter-test-1-0   1/1     CrashLoopBackOff   4          2m38sbad-frontend-4s58z   0/1     CrashLoopBackOff   4          2m38s" | awk '{print $2}' | cut -d "/" -f 1
#echo "jmeter-test-1-0   1/1     CrashLoopBackOff   4          2m38sbad-frontend-4s58z   0/1     CrashLoopBackOff   4          2m38s" | awk '{print $2}' | cut -d "/" -f 1
it=$(seq $pod)

for i in $it;
do
res+=($(echo "jmeter-test-1-0   1/1     CrashLoopBackOff   4          2m38sbad-frontend-4s58z   0/1     CrashLoopBackOff   4          2m38s" | awk '{print $2}' | cut -d "/" -f 1))


done

echo ${res[@]}

for a in $(seq ${#res[@]});
do
total_pods=`echo $total_pods + ${res[a]} | bc`
done

echo $total_pods