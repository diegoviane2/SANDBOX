pod=6
declare -a res=()

it=$(seq $pod)


#Scan SatefulSet status and store running pods values
for i in $it;
do
res+=($(echo "jmeter-test-1-0   1/1     CrashLoopBackOff   4          2m38sbad-frontend-4s58z   0/1     CrashLoopBackOff   4          2m38s" | awk '{print $2}' | cut -d "/" -f 1))
done


for a in $(seq ${#res[@]});
do
sum=$(IFS=+; echo "$((${res[*]}))")
done


echo $sum
des=10


if [ $sum -le $des ]; then
    echo "Parametro 1 ($sum) é Menor a 2 ($des)."
else
    echo "Parametro 1 ($sum) é Maior a 2 ($des)."
fi

