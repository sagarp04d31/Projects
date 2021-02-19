name=$1
id=$2
country () {
	printf "Country Name:		ID:\n"
	printf "Australia		AUS\n"
	printf "Bangladesh 		BAN\n"
	printf "Nepal 			NEP\n"
	printf "India 			IND\n"
	printf "England 		ENG\n\n"
	sleep 0.3
	printf "Guess the best team\n"
	printf "$ "
	read best
	if [ $best == 'ENG' ]
	then
		printf "\n**************************************************\n"
		printf "Correct Guess\n"
		printf "It has won the 2019 World Cricket Championship"
		printf "\n**************************************************\n\n"
	else
		printf "\n**************************************************\n"
		printf "Wrong guess. Please try again"
		printf "\n**************************************************\n\n"
	fi
}


# Users data and date/time info
profile () {
	printf "Name:		ID:\n"
	printf "$name 		$id\n"
	sleep 0.3
	printf "\nDate and time of execution is $now \n\n"
	sleep 0.3
}



# command line interface
choose () {
	printf "$ "
	read input
   	if [[ $input = "quit" ]] || [[ $input = "QUIT" ]]
   	then
		echo quitting..
		sleep 0.2
		exit 1

   	fi
}

# For loop for the secret key
for ((i = 0 ; i <= 6; i ++)); do
	printf "Enter the key\n"
	printf "$ "
	read key
	if [ $key = "12345" ]
	then
		profile
		choose
	elif [ $i = 5 ]
	then
		echo Wrong Key
		sleep 0.4
		echo exiting..
		sleep 0.2
		exit 1
	else
		echo try again
	fi
done


