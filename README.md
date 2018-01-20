# Ninja-Coder_Anmol-varshney Explanation of Python program to generate 73% biased random numbers in a range

This program generates 'N' random numbers in the range [min, max] which are guaranteed to be 73% biased to the higher number i.e. 'max'.


It prompts user to enter a range (space seperated). Then it asks for how many random numbers(N) are to be generated in that range.
It prints "two lists" on the console:

	1.First list contains all the numbers which are high biased i.e. 73% of N which are greater or equal to the 'middle of [min, max]'.
	2.Second list contains all the numbers which are low biased i.e. 27% of N which are less than 'middle of [min, max]'.


-------------------------------------------------------------------------------------------------------------------
It uses "Multiplicative Congruential Generator" algorithm to genererate random numbers.
Multiplicative Congruential Generator is a varient of Linear congruential Generator where increment = 0
It has the form:
    
	X_next = (Multiplier * X_previous) mod Modulus
    where, X0 = Seed value
  
Seed value can be user defined OR default seed value is the current time in seconds since epoch.
	
	Modulus = (2^31) - 1 and
	Multiplier = 16807

About the modulus:

	[(2^31)-1] is a mersenne prime which is used in many random number generator algorithm because its calculation is relatively cheap and it gives a longer sequence of random numbers.

About the nultiplier:

	16807 = 7^5 is a primitive root of 2^31... So this multiplier gives you the longest period of random numbers i.e. it generates the numbers in the range [0, 2^31-1] without repeating the sequence.
	And this multiplier is also used by many random number generator algorithms.
    
Now X_next becomes the next seed value.
To ensure that next random number remains <= 'max', it takes modulus of X_next by 'max' i.e.

	next = X_next mod max

To ensure that 'next' >= 'min', it does

	if next < min then
		next = next + (max-min)

Then we return this 'next' as a random number

-----------------------------------------------------------------------------------------------------------------------

I have defined a python class with the name 'Random' which has a constructor and two methods: seed() and nextRandom().

The seed method is called to set user defined seed value.

The nextRandom() method does all the calculation explained in the above portion.

The constructor intializes the vales of 'min', 'max', 'Multiplier', 'Modulus' and also default 'seed' value.

------------------------------------------------------------------------------------------------------------------------

The main() method which is outside the class 'Random' is where all the biasing happens.

It creates an object 'rand' of type 'Random' with the default seed value.

Inside the while loop it repeatedly fills both the lists (list_high and list_low) until they are full by calling the rand.nextRandom() function.
Once they are full it exits the while loop and prints both the lists on the console.

The sizees of the list_high and list_low are calculated as:
	
	high_biased_numbers = ceil( 73% of N )
	low_biased_numbers = N - high_biased_numbers
	
	where N = Total nuber of random numbers to be generated
	for e.g. if N=100, high_biased_numbers = 73 and so low_biased_numbers = 100 - 73
	if N=10, high_biased_numbers = 8 (not 7) and so low_biased_numbers = 10 - 8
	
	
