
Usage: python3 CPtripPlanner.py -sS <startStation> -eS <endStation> 

Options: 
	
	-sD <startDate> (search only after <startDate> value inclusive |ex: -sD 2020-05-29|)
	
	-eD <endDate>   (search only until <endDate> value inclusive   |ex: -eD 2020-05-30|)
	
	-al (search for alfa trains)
	
	-ic (search for intercities trains)
	
	-in (search for international trains)
	
	-re (search for regionals trains)
	
	-ub (search for urbans trains)

Note: When only <startStation> <endStation> specifyed, <startDate> will be set as the current day, and <endDate> as the maximum allowed by CP (60 days).
      By default the program will search for all types of trains.

