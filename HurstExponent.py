# A function to estimate the Hurst Exponent of a Time Series through Detrended Fluctuation Analysis
# TimeSeries: Calculate Hurst Exp for given series
# Range: List of different window sizes for log-log plot

def DFA_Hust( TimeSeries, Range ):
	
	Fluctuation= []

	for window in Range:

		# Total intervals of time series for given window size
		Intervals= len(TimeSeries)/window
		Size= Intervals*window
		
		Mean= np.mean(TimeSeries[0:Size])
		CumSeries= []
		YFit= []

		# Cumulative Time Series
		for i in range(1, Size + 1 ):
			CumSeries.append( np.sum( TimeSeries[0:i] - Mean ) )

		# Fitting Least Square Fit line in each interval for given window size	
		for _iter in range(0, Intervals): 

			start=_iter*window
			end= (_iter+1)*window

			XRange= range( 1, window + 1 )
			Y= CumSeries[ start : end ]

			# Fitting staright line for time series data in current interval
			Param= np.polyfit( XRange , Y, 1)

			for val in XRange:
				YFit.append( Param[1] + Param[0]*val )

		# Detrending by removing linear trend from Time Series		
		YFit= np.array( YFit )
		Fluctuation.append( np.std( CumSeries - YFit ) )

	# Plotting Fluctuatin for different window sizes on log-log plot. 
	HurstExp= np.polyfit( np.log(Range), np.log(Fluctuation), 1 )

	# Slope on log-log plot is an estimate of Hurst Exponent
	return round( HurstExp[0], 2)